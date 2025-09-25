"""Python language mapping for unified parser architecture.

This module provides Python-specific tree-sitter queries and extraction logic
for mapping Python AST nodes to semantic chunks.
"""

from typing import TYPE_CHECKING, Any

from chunkhound.core.types.common import Language
from chunkhound.parsers.mappings.base import BaseMapping

if TYPE_CHECKING:
    from tree_sitter import Node as TSNode

try:
    from tree_sitter import Node as TSNode

    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    TSNode = Any  # type: ignore


class PythonMapping(BaseMapping):
    """Python-specific tree-sitter mapping implementation.

    Handles Python's unique language features including:
    - Function definitions with decorators and async support
    - Class definitions with inheritance
    - Method definitions within classes
    - Module, function, and class docstrings
    - Type hints and annotations
    - Import statements
    - Comments
    """

    def __init__(self) -> None:
        """Initialize Python mapping."""
        super().__init__(Language.PYTHON)

    def get_function_query(self) -> str:
        """Get tree-sitter query pattern for Python function definitions.

        Captures both regular and async functions with their names.

        Returns:
            Tree-sitter query string for finding Python function definitions
        """
        return """
            (function_definition
                name: (identifier) @function_name
            ) @function_def
        """

    def get_class_query(self) -> str:
        """Get tree-sitter query pattern for Python class definitions.

        Captures class name and optional superclasses.

        Returns:
            Tree-sitter query string for finding Python class definitions
        """
        return """
            (class_definition
                name: (identifier) @class_name
                superclasses: (argument_list)? @superclasses
            ) @class_def
        """

    def get_method_query(self) -> str:
        """Get tree-sitter query pattern for Python method definitions.

        Methods are function definitions within class bodies.

        Returns:
            Tree-sitter query string for finding Python method definitions
        """
        return """
            (class_definition
                body: (block
                    (function_definition
                        name: (identifier) @method_name
                    ) @method_def
                )
            )
        """

    def get_comment_query(self) -> str:
        """Get tree-sitter query pattern for Python comments.

        Returns:
            Tree-sitter query string for finding Python comments
        """
        return """
            (comment) @comment
        """

    def get_docstring_query(self) -> str:
        """Get tree-sitter query pattern for Python docstrings.

        Captures module, function, and class docstrings.

        Returns:
            Tree-sitter query string for finding Python docstrings
        """
        return """
            (module . (expression_statement (string) @module_docstring))
            (function_definition
                body: (block .
                    (expression_statement (string) @function_docstring)
                )
            )
            (async_function_definition
                body: (block .
                    (expression_statement (string) @async_function_docstring)
                )
            )
            (class_definition
                body: (block .
                    (expression_statement (string) @class_docstring)
                )
            )
        """

    def get_import_query(self) -> str:
        """Get tree-sitter query pattern for Python import statements.

        Returns:
            Tree-sitter query string for finding Python import statements
        """
        return """
            (import_statement) @import
            (import_from_statement) @import_from
        """

    def extract_function_name(self, node: "TSNode | None", source: str) -> str:
        """Extract function name from a Python function definition node.

        Args:
            node: Tree-sitter function definition node
            source: Source code string

        Returns:
            Function name or fallback name if extraction fails
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return self.get_fallback_name(node, "function")

        # Look for the name child node
        name_node = self.find_child_by_type(node, "identifier")
        if name_node:
            name = self.get_node_text(name_node, source).strip()
            if name:
                return name

        return self.get_fallback_name(node, "function")

    def extract_class_name(self, node: "TSNode | None", source: str) -> str:
        """Extract class name from a Python class definition node.

        Args:
            node: Tree-sitter class definition node
            source: Source code string

        Returns:
            Class name or fallback name if extraction fails
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return self.get_fallback_name(node, "class")

        # Look for the name child node
        name_node = self.find_child_by_type(node, "identifier")
        if name_node:
            name = self.get_node_text(name_node, source).strip()
            if name:
                return name

        return self.get_fallback_name(node, "class")

    def extract_parameters(self, node: "TSNode | None", source: str) -> list[str]:
        """Extract parameter names from a Python function/method node.

        Handles regular parameters, default parameters, *args, **kwargs,
        and keyword-only parameters.

        Args:
            node: Tree-sitter function/method definition node
            source: Source code string

        Returns:
            List of parameter names
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return []

        parameters: list[str] = []

        # Find the parameters node
        params_node = self.find_child_by_type(node, "parameters")
        if not params_node:
            return parameters

        # Walk through parameter children
        for i in range(params_node.child_count):
            child = params_node.child(i)
            if not child:
                continue

            param_name = ""

            if child.type == "identifier":
                # Simple parameter
                param_name = self.get_node_text(child, source).strip()
            elif child.type == "default_parameter":
                # Parameter with default value
                name_child = child.child(0)
                if name_child and name_child.type == "identifier":
                    param_name = self.get_node_text(name_child, source).strip()
            elif child.type == "typed_parameter":
                # Parameter with type annotation
                name_child = self.find_child_by_type(child, "identifier")
                if name_child:
                    param_name = self.get_node_text(name_child, source).strip()
            elif child.type == "typed_default_parameter":
                # Parameter with type annotation and default value
                name_child = self.find_child_by_type(child, "identifier")
                if name_child:
                    param_name = self.get_node_text(name_child, source).strip()
            elif child.type == "list_splat_pattern":
                # *args parameter
                name_child = self.find_child_by_type(child, "identifier")
                if name_child:
                    param_name = "*" + self.get_node_text(name_child, source).strip()
            elif child.type == "dictionary_splat_pattern":
                # **kwargs parameter
                name_child = self.find_child_by_type(child, "identifier")
                if name_child:
                    param_name = "**" + self.get_node_text(name_child, source).strip()

            # Add valid parameter names (skip commas and parentheses)
            if (
                param_name
                and param_name != ","
                and param_name != "("
                and param_name != ")"
                and param_name != "self"  # Optionally skip 'self'
                and param_name != "cls"
            ):  # Optionally skip 'cls'
                parameters.append(param_name)

        return parameters

    def extract_decorators(self, node: "TSNode | None", source: str) -> list[str]:
        """Extract decorator names from a Python function or class node.

        Args:
            node: Tree-sitter function/class definition node
            source: Source code string

        Returns:
            List of decorator names
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return []

        decorators = []

        # Look for decorator nodes as siblings before the function/class
        # In tree-sitter, decorators are typically child nodes
        decorator_nodes = self.find_children_by_type(node, "decorator")

        for decorator_node in decorator_nodes:
            decorator_text = self.get_node_text(decorator_node, source).strip()
            if decorator_text and decorator_text.startswith("@"):
                decorators.append(decorator_text)

        return decorators

    def extract_inheritance(self, node: "TSNode | None", source: str) -> list[str]:
        """Extract superclass names from a Python class definition.

        Args:
            node: Tree-sitter class definition node
            source: Source code string

        Returns:
            List of superclass names
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return []

        superclasses: list[str] = []

        # Find the superclasses argument list
        superclasses_node = self.find_child_by_type(node, "argument_list")
        if not superclasses_node:
            return superclasses

        # Extract each superclass
        for i in range(superclasses_node.child_count):
            child = superclasses_node.child(i)
            if child and child.type == "identifier":
                superclass_name = self.get_node_text(child, source).strip()
                if (
                    superclass_name
                    and superclass_name != ","
                    and superclass_name != "("
                    and superclass_name != ")"
                ):
                    superclasses.append(superclass_name)
            elif child and child.type == "attribute":
                # Handle qualified names like package.ClassName
                superclass_name = self.get_node_text(child, source).strip()
                if superclass_name:
                    superclasses.append(superclass_name)

        return superclasses

    def extract_type_hints(self, node: "TSNode | None", source: str) -> dict[str, str]:
        """Extract type hints from a Python function definition.

        Args:
            node: Tree-sitter function definition node
            source: Source code string

        Returns:
            Dictionary mapping parameter names to their type hints
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return {}

        type_hints: dict[str, str] = {}

        # Find parameters with type annotations
        params_node = self.find_child_by_type(node, "parameters")
        if not params_node:
            return type_hints

        for i in range(params_node.child_count):
            child = params_node.child(i)
            if not child:
                continue

            if child.type in ("typed_parameter", "typed_default_parameter"):
                # Extract parameter name
                name_node = self.find_child_by_type(child, "identifier")
                if name_node:
                    param_name = self.get_node_text(name_node, source).strip()

                    # Extract type annotation
                    type_node = self.find_child_by_type(child, "type")
                    if type_node:
                        type_hint = self.get_node_text(type_node, source).strip()
                        if param_name and type_hint:
                            type_hints[param_name] = type_hint

        # Extract return type annotation
        return_type_node = None
        for i in range(node.child_count):
            child = node.child(i)
            if child and child.type == "type":
                return_type_node = child
                break

        if return_type_node:
            return_type = self.get_node_text(return_type_node, source).strip()
            if return_type:
                type_hints["return"] = return_type

        return type_hints

    def is_async_function(self, node: "TSNode | None") -> bool:
        """Check if a function node represents an async function.

        Args:
            node: Tree-sitter function definition node

        Returns:
            True if the function is async, False otherwise
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return False

        return node.type == "async_function_definition"

    def is_generator_function(self, node: "TSNode | None", source: str) -> bool:
        """Check if a function contains yield statements (is a generator).

        Args:
            node: Tree-sitter function definition node
            source: Source code string

        Returns:
            True if the function contains yield statements, False otherwise
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return False

        # Look for yield expressions in the function body
        yield_nodes = self.find_nodes_by_type(node, "yield")
        return len(yield_nodes) > 0

    def extract_import_names(
        self, node: "TSNode | None", source: str
    ) -> dict[str, str]:
        """Extract import information from an import statement.

        Args:
            node: Tree-sitter import statement node
            source: Source code string

        Returns:
            Dictionary with import information
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return {}

        import_info = {}
        import_text = self.get_node_text(node, source).strip()

        if node.type == "import_statement":
            import_info["type"] = "import"
            import_info["statement"] = import_text
        elif node.type == "import_from_statement":
            import_info["type"] = "from_import"
            import_info["statement"] = import_text

        return import_info

    def should_include_node(self, node: "TSNode | None", source: str) -> bool:
        """Determine if a Python node should be included as a chunk.

        Filters out very small functions/classes and internal methods.

        Args:
            node: Tree-sitter node
            source: Source code string

        Returns:
            True if node should be included, False otherwise
        """
        if not TREE_SITTER_AVAILABLE or node is None:
            return False

        # Get the node text to check size
        text = self.get_node_text(node, source)

        # Skip very small nodes (less than 20 characters)
        if len(text.strip()) < 20:
            return False

        # For functions and methods, check if they're just pass statements
        if node.type in ("function_definition", "async_function_definition"):
            # If the body only contains 'pass', it might be a placeholder
            body_node = self.find_child_by_type(node, "block")
            if body_node:
                body_text = self.get_node_text(body_node, source).strip()
                if body_text in ("pass", "...", "pass\n", "...\n"):
                    return False

        return True
