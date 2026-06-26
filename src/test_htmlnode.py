import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "www.youtube.com",
            "target": "_blank",
        }
        children: list[HTMLNode] = [
            HTMLNode("li", "one", None, None), 
            HTMLNode("li", "two", None, props), 
            HTMLNode("li", "", None, None), 
        ]
        pragraphNode = HTMLNode("p", "Osama", None, None)
        anchorNode = HTMLNode("a", "osama", None, props)
        listNode = HTMLNode("ul", "osama", children, None)
        self.maxDiff = None
        self.assertEqual(pragraphNode.__repr__(),"HTMLNode(<p>, Osama, None, None)")
        self.assertEqual(anchorNode.__repr__(), "HTMLNode(<a>, osama, None, {'href': 'www.youtube.com', 'target': '_blank'})")
        self.assertEqual(listNode.__repr__(),'''HTMLNode(<ul>, osama, [HTMLNode(<li>, one, None, None), HTMLNode(<li>, two, None, {'href': 'www.youtube.com', 'target': '_blank'}), HTMLNode(<li>, , None, None)], None)''')               
      