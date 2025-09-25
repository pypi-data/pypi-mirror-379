"""Go language mapping for unified parser architecture.

This module provides Go-specific tree-sitter queries and extraction logic
for the universal concept system. It maps Go's AST nodes to universal
semantic concepts used by the unified parser.
"""

from typing import Any

from tree_sitter import Node

from chunkhound.core.types.common import Language
from chunkhound.parsers.mappings.base import BaseMapping
from chunkhound.parsers.universal_engine import UniversalConcept


class GoMapping(BaseMapping):
    """Go-specific tree-sitter mapping for universal concepts."""

    def __init__(self) -> None:
        """Initialize Go mapping."""
        super().__init__(Language.GO)

    # BaseMapping required methods
    def get_function_query(self) -> str:
        """Get tree-sitter query pattern for function definitions."""
        return """
        (function_declaration
            name: (identifier) @func_name
        ) @func_def
        """

    def get_class_query(self) -> str:
        """Get tree-sitter query pattern for struct definitions (Go's equivalent of classes)."""
        return """
        (type_declaration
            (type_spec
                name: (type_identifier) @struct_name
                type: (struct_type) @struct_type
            )
        ) @struct_def
        """

    def get_comment_query(self) -> str:
        """Get tree-sitter query pattern for comments."""
        return """
        (comment) @comment
        """

    def extract_function_name(self, node: Node | None, source: str) -> str:
        """Extract function name from a function definition node."""
        if node is None:
            return self.get_fallback_name(node, "function")

        # Find the function name child
        name_node = self.find_child_by_type(node, "identifier")
        if name_node:
            return self.get_node_text(name_node, source).strip()

        return self.get_fallback_name(node, "function")

    def extract_class_name(self, node: Node | None, source: str) -> str:
        """Extract struct name from a struct definition node."""
        if node is None:
            return self.get_fallback_name(node, "struct")

        # Navigate to the type_spec and find the type_identifier
        for child in self.walk_tree(node):
            if child and child.type == "type_identifier":
                return self.get_node_text(child, source).strip()

        return self.get_fallback_name(node, "struct")

    # LanguageMapping protocol methods
    def get_query_for_concept(self, concept: UniversalConcept) -> str | None:
        """Get tree-sitter query for universal concept in Go."""

        if concept == UniversalConcept.DEFINITION:
            return """
            (function_declaration
                name: (identifier) @name
            ) @definition
            
            (method_declaration
                receiver: (parameter_list
                    (parameter_declaration
                        type: (_) @receiver_type
                    )
                )
                name: (field_identifier) @name
            ) @definition
            
            (type_declaration
                (type_spec
                    name: (type_identifier) @name
                    type: (struct_type)
                )
            ) @definition
            
            (type_declaration
                (type_spec
                    name: (type_identifier) @name
                    type: (interface_type)
                )
            ) @definition
            
            (type_declaration
                (type_spec
                    name: (type_identifier) @name
                    type: (_)
                )
            ) @definition
            """

        elif concept == UniversalConcept.BLOCK:
            return """
            (block) @definition
            
            (if_statement
                condition: (_)
                consequence: (block) @block
            ) @definition
            
            (for_statement
                body: (block) @block
            ) @definition
            
            (expression_switch_statement
                (expression_case) @case
            ) @definition
            """

        elif concept == UniversalConcept.COMMENT:
            return """
            (comment) @definition
            """

        elif concept == UniversalConcept.IMPORT:
            return """
            (import_declaration
                (import_spec
                    path: (interpreted_string_literal) @import_path
                ) @import_spec
            ) @definition
            
            (package_clause
                (package_identifier) @package_name
            ) @definition
            """

        elif concept == UniversalConcept.STRUCTURE:
            return """
            (source_file
                (package_clause) @package
                (import_declaration)* @imports
            ) @definition
            """

        # All cases handled above
        return None

    def extract_name(
        self, concept: UniversalConcept, captures: dict[str, Node], content: bytes
    ) -> str:
        """Extract name from captures for this concept."""

        # Convert bytes to string for processing
        source = content.decode("utf-8")

        if concept == UniversalConcept.DEFINITION:
            # Try to get the name from various capture groups
            if "name" in captures:
                name_node = captures["name"]
                name = self.get_node_text(name_node, source).strip()

                # For methods, prepend receiver type
                if "receiver_type" in captures:
                    receiver_type_node = captures["receiver_type"]
                    receiver_type = self.get_node_text(
                        receiver_type_node, source
                    ).strip()
                    # Remove pointer indicators for cleaner names
                    receiver_type = receiver_type.lstrip("*")
                    return f"{receiver_type}.{name}"

                return name

            return "unnamed_definition"

        elif concept == UniversalConcept.BLOCK:
            # Use location-based naming for blocks
            if "definition" in captures:
                node = captures["definition"]
                line = node.start_point[0] + 1
                return f"block_line_{line}"

            return "unnamed_block"

        elif concept == UniversalConcept.COMMENT:
            # Use location-based naming for comments
            if "definition" in captures:
                node = captures["definition"]
                line = node.start_point[0] + 1
                return f"comment_line_{line}"

            return "unnamed_comment"

        elif concept == UniversalConcept.IMPORT:
            if "import_path" in captures:
                path_node = captures["import_path"]
                path = self.get_node_text(path_node, source).strip()
                # Remove quotes from string literal
                path = path.strip('"')
                # Extract package name from path
                parts = path.split("/")
                if parts:
                    return f"import_{parts[-1]}"
                return "import_unknown"
            elif "package_name" in captures:
                pkg_node = captures["package_name"]
                pkg_name = self.get_node_text(pkg_node, source).strip()
                return f"package_{pkg_name}"

            return "unnamed_import"

        elif concept == UniversalConcept.STRUCTURE:
            return "file_structure"

        # All cases handled above
        return "unnamed"

    def extract_content(
        self, concept: UniversalConcept, captures: dict[str, Node], content: bytes
    ) -> str:
        """Extract content from captures for this concept."""

        # Convert bytes to string for processing
        source = content.decode("utf-8")

        if "definition" in captures:
            node = captures["definition"]
            return self.get_node_text(node, source)
        elif captures:
            # Use the first available capture
            node = list(captures.values())[0]
            return self.get_node_text(node, source)

        return ""

    def extract_metadata(
        self, concept: UniversalConcept, captures: dict[str, Node], content: bytes
    ) -> dict[str, Any]:
        """Extract Go-specific metadata."""

        source = content.decode("utf-8")
        metadata = {}

        if concept == UniversalConcept.DEFINITION:
            # Extract function/method specific metadata
            def_node = captures.get("definition")
            if def_node:
                metadata["node_type"] = def_node.type

                # For functions, extract parameters and return type
                if def_node.type == "function_declaration":
                    metadata["kind"] = "function"
                    params = self._extract_function_parameters(def_node, source)
                    metadata["parameters"] = params
                    return_type = self._extract_function_return_type(def_node, source)
                    if return_type:
                        metadata["return_type"] = return_type

                # For methods, extract receiver info
                elif def_node.type == "method_declaration":
                    metadata["kind"] = "method"
                    params = self._extract_function_parameters(def_node, source)
                    metadata["parameters"] = params
                    return_type = self._extract_function_return_type(def_node, source)
                    if return_type:
                        metadata["return_type"] = return_type

                    if "receiver_type" in captures:
                        receiver_node = captures["receiver_type"]
                        metadata["receiver_type"] = self.get_node_text(
                            receiver_node, source
                        ).strip()

                # For type definitions, extract type kind
                elif def_node.type == "type_declaration":
                    metadata["kind"] = "type"
                    # Find the actual type (struct, interface, etc.)
                    for child in self.walk_tree(def_node):
                        if child and child.type in ["struct_type", "interface_type"]:
                            metadata["type_kind"] = child.type
                            break

        elif concept == UniversalConcept.IMPORT:
            if "import_path" in captures:
                path_node = captures["import_path"]
                import_path = self.get_node_text(path_node, source).strip().strip('"')
                metadata["import_path"] = import_path

                # Extract package name from import path
                parts = import_path.split("/")
                if parts:
                    metadata["package_name"] = parts[-1]

            elif "package_name" in captures:
                pkg_node = captures["package_name"]
                metadata["package_name"] = self.get_node_text(pkg_node, source).strip()

        elif concept == UniversalConcept.COMMENT:
            if "definition" in captures:
                comment_node = captures["definition"]
                comment_text = self.get_node_text(comment_node, source)

                # Determine comment type
                if comment_text.startswith("//"):
                    metadata["comment_type"] = "line"
                elif comment_text.startswith("/*"):
                    metadata["comment_type"] = "block"

                # Check if it's a doc comment (starts with specific patterns)
                clean_text = self.clean_comment_text(comment_text)
                is_doc = False
                if clean_text:
                    if clean_text.startswith("Package "):
                        is_doc = True
                    else:
                        for prefix in ["TODO:", "FIXME:", "NOTE:", "HACK:"]:
                            if clean_text.startswith(prefix):
                                is_doc = True
                                break

                if is_doc:
                    metadata["is_doc_comment"] = True

        return metadata

    def _extract_function_parameters(self, func_node: Node, source: str) -> list[str]:
        """Extract parameter types from a Go function node."""
        parameters = []

        # Find parameter_list node
        param_list = None
        for child in self.walk_tree(func_node):
            if child and child.type == "parameter_list":
                param_list = child
                break

        if param_list:
            # Find parameter_declaration nodes
            param_declarations = self.find_children_by_type(
                param_list, "parameter_declaration"
            )
            for param_decl in param_declarations:
                # Find the type node
                type_node = None
                for i in range(param_decl.child_count):
                    potential_child = param_decl.child(i)
                    if potential_child is not None and potential_child.type not in [
                        "identifier",
                        ",",
                    ]:
                        type_node = potential_child
                        break

                if type_node:
                    param_type = self.get_node_text(type_node, source).strip()
                    parameters.append(param_type)

        return parameters

    def _extract_function_return_type(self, func_node: Node, source: str) -> str | None:
        """Extract return type from a Go function node."""

        # Look for the result part (return type) after parameters
        for i in range(func_node.child_count):
            child = func_node.child(i)
            if child and child.type == "parameter_list":
                # Check if there's a result node after this parameter list
                if i + 1 < func_node.child_count:
                    next_child = func_node.child(i + 1)
                    if next_child and next_child.type != "block":
                        # This might be the return type
                        return self.get_node_text(next_child, source).strip()

        return None
