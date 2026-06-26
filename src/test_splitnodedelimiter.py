import unittest
from split_node_delimeters import *
from textnode import *


class TestSplitNodeDelimiter(unittest.TestCase):
    def test(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), TextNode(" word", TextType.TEXT, None)])
    
    def test_images_and_links(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images_metadata = extract_markdown_images(text)
        links_metadata = extract_markdown_links(text)
        self.assertEqual(images_metadata, [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(links_metadata, [('to boot dev', 'https://www.boot.dev')])
    
    def test_markdown_image_and_links_to_HTMLNode(self):
        
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def markdown_elements_to_textnode(self):
        text_node = text_to_textnode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual([
                                TextNode("This is" , TextType.TEXT, None), 
                                TextNode("text", TextType.BOLD, None), 
                                TextNode(" with an ", TextType.TEXT, None), 
                                TextNode("italic", TextType.ITALIC, None), 
                                TextNode(" word and a ", TextType.TEXT, None), 
                                TextNode("code block", TextType.CODE, None), 
                                TextNode(" and an ", TextType.TEXT, None), 
                                TextNode("obi wan image", TextType.IMAGE," https://i.imgur.com/fJRm4Vk.jpeg"), 
                                TextNode("link", TextType.LINK, "https://boot.dev")
                            ], text_node)
