from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
class TextNode:
    def __init__(self, text: str, text_type: TextType, props: dict[str, str]|None = None):
        self.text = text
        self.text_type = text_type
        self.props = props
    def __eq__(self, other) -> bool:
       return (
        (self.text == other.text)
        and (self.text_type.value == other.text_type.value) 
        and (self.props == self.props)
        )


    def __repr__(self):
       return f"TextNode({self.text}, {self.text_type.value}, {self.props})"


def text_node_to_leaf_node(text_node: "TextNode") -> LeafNode:

    match(text_node.text_type.value):
        case "text":
            return LeafNode(tag=None, value=text_node.text)
        case "bold":
            return LeafNode(tag="b", value=text_node.text)
        case "italic":
            return LeafNode(tag="i", value=text_node.text)
        case "code":
            return LeafNode(tag="code", value=text_node.text)
        case "image":
            return LeafNode(tag="img", value=text_node.text, props=text_node.props)
        case "link":
            return LeafNode(tag="a", value=text_node.text, props=text_node.props)
        case _:
            raise ValueError(f"the type of {text_node} must be of TextType")