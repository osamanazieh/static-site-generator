class HTMLNode:
    def __init__(
            self, tag: str| None = None, value: str| None = None, children: list["HTMLNode"]| None = None, props: dict[str, str]| None = None
        ) -> None:
            self.tag = tag
            self.value = value
            self.children = children
            self.props = props
        
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self) -> str:
        prop_string: str = ""
        if self.props is None:
            return prop_string
        for k,v in self.props.items():
            prop_string += k + "=" +  "\"" + v + "\"" + " "
            
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode(<{self.tag}>, {self.value}, {self.children}, {self.props})" 