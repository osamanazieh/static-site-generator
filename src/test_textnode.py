import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):  
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):  
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is an italic node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node =  TextNode("This is an italic node", TextType.ITALIC, None)
        if node.text_type in [TextType.IMAGE, TextType.LINK]:
            self.assertNotEqual(node.url, None)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("img", TextType.IMAGE, url="testing.com")
        html_node = text_node_to_html_node(node)
        image_node = text_node_to_html_node(node2)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(image_node.value, None)
        
        
if __name__ == "__main__":
    unittest.main()