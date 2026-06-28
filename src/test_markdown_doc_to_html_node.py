import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))
from markdown_to_html_node import * 

class TestMarkdownDocToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph 
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_doc_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_doc_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )    
    def test_heading(self):
        md = """
        # h1\n
            ## h2\n
        ### h3\n
        #### h4\n
        ##### h5\n
        ###### h6\n
        """
        node = markdown_doc_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>h1</h1><h2>h2</h2><h3>h3</h3><h4>h4</h4><h5>h5</h5><h6>h6</h6></div>"
        )
    def test_olblock(self):
                
        md = """
            1. first item of unordered list
            2. second  item of unordered list
            3. third item of unordered list
        """

        node = markdown_doc_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item of unordered list</li><li>second  item of unordered list</li><li>third item of unordered list</li></ol></div>"
        )
    def test_ulblock(self):
                
        md = """
            - first item of unordered list
            - second  item of unordered list
            - third item of unordered list
        """

        node = markdown_doc_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>first item of unordered list</li><li>second  item of unordered list</li><li>third item of unordered list</li></ul></div>"
        )

