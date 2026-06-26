from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None) -> None:
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None or self.children is None:
            raise ValueError("Tag/Children must be provided in parent Nodes")
        output = f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"
        
        return output

    