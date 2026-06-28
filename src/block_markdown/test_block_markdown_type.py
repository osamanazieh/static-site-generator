import unittest
from blocktype import *

class TestBlockToBlockType(unittest.TestCase):

    # HEADING
    def test_heading_h1(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)

    def test_heading_h6(self):
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_heading_seven_hashes_is_paragraph(self):
        self.assertEqual(block_to_block_type("####### Not a heading"), BlockType.PARAGRAPH)

    def test_heading_no_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    # CODE
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nsome code\n```"), BlockType.CODE)

    def test_code_block_multiline(self):
        self.assertEqual(block_to_block_type("```\nline1\nline2\n```"), BlockType.CODE)

    def test_code_block_no_newline_is_paragraph(self):
        self.assertEqual(block_to_block_type("```no newline```"), BlockType.PARAGRAPH)

    # QUOTE
    def test_quote(self):
        self.assertEqual(block_to_block_type("> some quote"), BlockType.QUOTE)

    def test_quote_no_space(self):
        self.assertEqual(block_to_block_type(">no space"), BlockType.QUOTE)

    # UNORDERED LIST
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item one"), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiline(self):
        self.assertEqual(block_to_block_type("- item one\n- item two"), BlockType.UNORDERED_LIST)

    def test_unordered_list_no_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("-no space"), BlockType.PARAGRAPH)

    # ORDERED LIST
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. first item"), BlockType.ORDERED_LIST)

    def test_ordered_list_multiline(self):
        self.assertEqual(block_to_block_type("1. first\n2. second"), BlockType.ORDERED_LIST)

    def test_ordered_list_no_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("1.no space"), BlockType.PARAGRAPH)

    # PARAGRAPH
    def test_plain_paragraph(self):
        self.assertEqual(block_to_block_type("just some text"), BlockType.PARAGRAPH)

    def test_empty_string(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
