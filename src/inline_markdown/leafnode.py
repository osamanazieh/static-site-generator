import os 
import sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__), ".."))

from htmlnode import HTMLNode 
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag=tag, value=value,props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("You must Enter a value to the leaf node")
        if self.tag is None:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>" if self.props is not None else f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>" if self.props is not None else f"<{self.tag}>{self.value}</{self.tag}>"
        