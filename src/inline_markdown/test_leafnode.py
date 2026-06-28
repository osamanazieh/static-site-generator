import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        paragraphLeaf = LeafNode("p", "osama", None)
        anchorLeaf = LeafNode("a", "linkedIn", {"href": "www.linkedin.com", "target": "_blank"})
        labelLeaf = LeafNode("label", "Enter email", {"for": "email"})
        self.assertEqual(paragraphLeaf.to_html(), "<p>osama</p>")
        self.assertEqual(anchorLeaf.to_html(), "<a href=\"www.linkedin.com\" target=\"_blank\" >linkedIn</a>")
        self.assertEqual(labelLeaf.to_html(), "<label for=\"email\" >Enter email</label>")
        
        self.assertEqual(paragraphLeaf.__repr__(), "<p>osama</p>")
        self.assertEqual(anchorLeaf.to_html(), "<a href=\"www.linkedin.com\" target=\"_blank\" >linkedIn</a>")
        self.assertEqual(labelLeaf.to_html(), "<label for=\"email\" >Enter email</label>")
        