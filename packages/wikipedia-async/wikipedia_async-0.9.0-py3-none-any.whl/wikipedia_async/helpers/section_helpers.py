import re
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class SectionNode(BaseModel):
    """A node representing a section in the tree structure."""

    title: str
    level: int
    content: str = ""
    children: List["SectionNode"] = []
    parent: Optional["SectionNode"] = None

    def add_child(self, child: "SectionNode"):
        """Add a child section to this section."""
        child.parent = self
        self.children.append(child)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the section node to a dictionary representation."""
        return {
            "title": self.title,
            "level": self.level,
            "content": self.content,
            "children": [child.to_dict() for child in self.children],
        }

    def __repr__(self):
        return f"SectionNode(title='{self.title}', level={self.level}, children={len(self.children)})"

    def to_string(self, with_content: bool = True, indent: int = 0) -> str:
        """Return a string representation of the section and its children."""
        indent_str = "  " * indent
        result = f"{indent_str}- {self.title} (Level {self.level})\n"
        if with_content:
            result += f"{indent_str}  Content: {self.content}\n"
        for child in self.children:
            result += child.to_string(with_content, indent + 1)
        return result

    def __str__(self):
        return self.to_string()


class SectionResult(list[SectionNode]):

    _flat_sections: List[SectionNode] = []

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        """Generate Pydantic core schema for SectionResult."""
        # Create a schema that validates as a list but preserves the custom class
        return core_schema.with_info_after_validator_function(
            cls._validate_and_convert,
            core_schema.list_schema(handler.generate_schema(SectionNode)),
        )

    @classmethod
    def _validate_and_convert(cls, value, info):
        """Convert validated list data to SectionResult instance."""
        if isinstance(value, cls):
            return value
        if isinstance(value, list):
            return cls(value)
        return cls()

    @classmethod
    def from_content(cls, content: str) -> "SectionResult":
        """Create a SectionResult from raw Wikipedia content."""
        # Return a plain list of SectionNode objects. Pydantic's custom
        # core schema will convert this list into a SectionResult during
        # validation. Returning a list avoids constructing a SectionResult
        # here and then again inside Pydantic, which caused __init__ to
        # run twice during earlier executions.
        sections = parse_sections(content)
        return sections  # type: ignore

    def __init__(self, sections: Optional[List[SectionNode]] = None):
        self.sections = sections or []
        self._flat_sections = []
        # Populate the list part with flattened sections
        flattened = list(self._iter_sections())
        super().__init__(flattened)
        self._length = len(flattened)

    def _iter_sections(self):
        """Recursively iterate through all sections (including nested ones)."""

        def _iter_recursive(sections):
            for section in sections:
                yield section
                yield from _iter_recursive(section.children)

        return _iter_recursive(self.sections)

    def get_sections_by_title(
        self,
        title: str,
        case_sensitive: bool = False,
    ) -> SectionNode | None:
        """Find a section by its title."""

        def search_recursive(nodes: List[SectionNode]) -> SectionNode | None:
            for node in nodes:
                node_title = node.title if case_sensitive else node.title.lower()
                search_title = title if case_sensitive else title.lower()

                if node_title == search_title:
                    return node

                # Search in children
                result = search_recursive(node.children)
                if result:
                    return result
            return None

        return search_recursive(self.sections)

    def tree_view(self, content_limit: int = 0) -> str:
        """Return a tree-like view of the sections, properly nested and without duplicates."""

        def render_section(section: SectionNode, level: int = 0) -> str:
            indent = "  " * level
            content_preview = section.content[:content_limit] + (
                "..." if content_limit and len(section.content) > content_limit else ""
            )
            result = f"{indent}- {section.title}"
            if content_preview:
                result += f":\n{indent} {content_preview}"
            result += "\n"
            for child in section.children:
                result += render_section(child, level + 1)
            result += "\n"
            return result

        # Only render each section once, starting from top-level sections
        return "".join(render_section(section) for section in self.sections)

    def summary(self) -> dict:
        """Get a summary of the section structure."""

        def count_sections(sections):
            total = len(sections)
            max_depth = 0
            for section in sections:
                if section.children:
                    child_count, child_depth = count_sections(section.children)
                    total += child_count
                    max_depth = max(max_depth, child_depth + 1)
            return total, max_depth

        total_sections, max_depth = count_sections(self.sections)

        return {
            "total_sections": total_sections,
            "root_sections": len(self.sections),
            "max_depth": max_depth,
            "has_nested_structure": max_depth > 0,
        }

    def to_dict(self) -> List[Dict[str, Any]]:
        """Convert the entire section tree to a list of dictionaries."""
        return [section.to_dict() for section in self.sections]

    def __getitem__(self, index):
        """Support indexing and slicing."""
        # Use the parent list's __getitem__ since we populated it in __init__
        return super().__getitem__(index)


def get_summary(content: str) -> str:
    # before headings
    pat = re.compile(r"^(={2,})\s*(.*?)\s*\1$", re.MULTILINE)
    match = pat.search(content)
    if match:
        return content[: match.start()].strip()

    return content.strip()[:500] + ("..." if len(content) > 500 else "")


def parse_sections(content: str) -> List[SectionNode]:
    """
    Parse Wikipedia content and create a tree-like structure of sections.

    Args:
        content: The Wikipedia page content as a string

    Returns:
        List of root-level SectionNode objects representing the section hierarchy
    """
    # Match section headers with varying levels (==, ===, ====, etc.)
    pat = re.compile(r"^(={2,})\s*(.*?)\s*\1$", re.MULTILINE)
    matches = list(pat.finditer(content))

    if not matches:
        # No sections found, return the entire content as a single section
        return [SectionNode(title="Content", level=0, content=content.strip())]

    sections = []
    stack: list[SectionNode] = []  # Stack to keep track of parent sections

    for i, match in enumerate(matches):
        # Calculate section level based on number of equals signs
        equals_count = len(match.group(1))
        level = equals_count - 1  # Level 1 for ==, Level 2 for ===, etc.
        title = match.group(2).strip()

        # Extract content for this section
        start_pos = match.end()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_content = content[start_pos:end_pos].strip()

        # Create new section node
        section = SectionNode(title=title, level=level, content=section_content)

        stack.append(section)

    sections.append(
        SectionNode(
            title="Summary", level=0, content=content[: matches[0].start()].strip()
        )
    )

    for i, s in enumerate(stack):
        if s.level > 1:
            sections[-1].add_child(s)
        else:
            sections.append(s)

    return sections
