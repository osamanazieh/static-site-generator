from block_markdown.markdown_to_block import markdown_to_blocks
from block_markdown.blocktype import BlockType, block_to_block_type
from inline_markdown.parentnode import ParentNode
from inline_markdown.split_node_delimeters import text_to_textnode
from htmlnode import HTMLNode
from inline_markdown.textnode import TextNode, TextType, text_node_to_leaf_node
from inline_markdown.leafnode import LeafNode
import re


def text_to_children(block: str) -> list[HTMLNode]:
    inline_markdown_elements = text_to_textnode(block)
    children: list[HTMLNode] = []
    for child in inline_markdown_elements:
        children.append(text_node_to_leaf_node(child))
    return children



def format_code_node(content: str):
    content = re.sub(r"^`{3}|`{3}$", "", content, flags=re.M)
    content = re.sub(r"^\s+", "", content, flags=re.M)
    return text_node_to_leaf_node(TextNode(content, TextType.CODE))


def format_paragraph_node(content: str):
    content= content.replace("\n", " ")
    content = re.sub(r" +", " ", content)
    return content

def get_heading_level(block):
    heading_level = re.findall(r"#+", block)[0]
    return len(heading_level)

def getting_ul_children(content):
    items = content.split("\n")
    items = list(map(lambda item: item.strip("- "), items))
    items = list(filter(lambda item: item != "", items))
    children = [] 
    for item in items:
        node = text_to_children(item)
        children.append(ParentNode("li", node))
    return children

def getting_ol_children(content):
    items = content.split("\n")
    items = list(map(lambda item: re.sub(r"\d+. |^ +", "", item, flags= re.M), items))
    items = list(filter(lambda item: item != "", items))

    children = [] 
    for item in items:
        node = text_to_children(item)
        children.append(ParentNode("li",node))
    return children

def format_block_quote(block):
    block = re.sub(r"^> ?", "", block, flags=re.M)
    return block




def markdown_doc_to_html_node(markdown_doc: str):
    blocks: list[HTMLNode] = [] 
    for block in markdown_to_blocks(markdown_doc):
        if block == "":
            continue
        
        match(block_to_block_type(block)):
            case BlockType.HEADING:
                heading_level = get_heading_level(block)
                block = re.sub(r"#+ ", "", block)
                children = text_to_children(block)
                blocks.append(ParentNode(f"h{heading_level}", children))
            
            case BlockType.QUOTE:
                block = format_block_quote(block)
                children = text_to_children(block)
                blocks.append(ParentNode('blockquote', children))
            
            case BlockType.CODE:
                code_node = format_code_node(block)
                blocks.append(ParentNode("pre", [code_node]))
            
            case BlockType.ORDERED_LIST:
                children = getting_ol_children(block)
                blocks.append(ParentNode("ol", children))
            
            case BlockType.UNORDERED_LIST:
                children = getting_ul_children(block)
                blocks.append(ParentNode("ul", children))
            
            case _:
                block = format_paragraph_node(block)
                children = text_to_children(block)
                
                blocks.append(ParentNode("p", children=children))
                
    return ParentNode("div", blocks)


