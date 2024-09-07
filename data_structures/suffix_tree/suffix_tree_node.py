from __future__ import annotations


class SuffixTreeNode:
    def __init__(
        self,
        children: dict[str, "SuffixTreeNode"] = None,
        is_end_of_string: bool = False,
        start: int | None = None,
        end: int | None = None,
        suffix_link: SuffixTreeNode | None = None,
    ) -> None:
        """
        Initializes a suffix tree node.

        Parameters:
            children (Dict[str, SuffixTreeNode]|None): The children of this node.
            is_end_of_string (bool): Indicates if this node represents
                                     the end of a string.
            start (int|None): The start index of the suffix in the text.
            end (int|None): The end index of the suffix in the text.
            suffix_link (SuffixTreeNode|None): Link to another suffix tree node.
        """
        self.children = children or {}
        self.is_end_of_string = is_end_of_string
        self.start = start
        self.end = end
        self.suffix_link = suffix_link
