import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from textnode import text_node_to_leaf_node, TextNode, TextType
import re 


def set_text_type_for_old_nodes(node_result: list[TextNode], texts: list[str], text_type: TextType, old_node: TextNode, remainder: int):
    for i in range(len(texts)):
        
        if texts[i] == "":
            continue
        if i % 2 == remainder:
            node_result.append(TextNode(text=texts[i], text_type=text_type))
        else:
            print("suppose here")
            node_result.append(TextNode(text=texts[i], text_type=old_node.text_type))

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result: list[TextNode] = []
    for node in old_nodes:
       
        node_result = []
        if node.text_type != TextType.TEXT:
            node_result.append(TextNode(text=node.text.strip(delimiter), text_type=node.text_type))

        else:

            texts = node.text.split(delimiter)
            delimiter_count = len(re.findall(re.escape("[`_*{2}]") ,node.text))
            if delimiter_count % 2 != 0:
                raise Exception("missing closing delimiter")
            if node.text == "":
                continue
            
            for i, text in enumerate(texts):
                if text == "":
                    continue
                if i % 2 == 0:
                    result.append(TextNode(text=text, text_type=node.text_type))
                else:
                    result.append(TextNode(text=text, text_type=text_type))
        
        result.extend(node_result)


    return result

md = "_An unpopular opinion, I know._"
md2 = "now it's not at the beginnig _An unpopular opinion, I know._"
node = TextNode(md, TextType.TEXT)
result = split_nodes_delimiter([node], '_',TextType.ITALIC)
print(result)
node2 = TextNode(md2, TextType.TEXT)
result = split_nodes_delimiter([node2], '_',TextType.ITALIC)
print(result)




def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matching_list: list[tuple[str, str]] = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matching_list


def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    matching_list: list[tuple[str,str]] = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matching_list


def split_nodes_link(old_nodes):
    per_node_result_list: list[TextNode] = []
    new_nodes: list[TextNode] = [] 
    text_nodes: list[str] = []
    for node in old_nodes:
        text_nodes = []
        matching_list: list[tuple[str,str]] = extract_markdown_links(node.text)    
        if len(matching_list) == 0:
            new_nodes.append(node)
            continue
        text_nodes = re.split(r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)", node.text)
        text_nodes = list(filter(lambda x: x != "" ,text_nodes))
        if len(text_nodes) != 0:
            zipped_text_links_nodes = zip(matching_list, text_nodes)


            for (alt, url), iter_text_nodes in zipped_text_links_nodes:

                per_node_result_list.append(TextNode(iter_text_nodes, TextType.TEXT))
                per_node_result_list.append(TextNode(alt, TextType.LINK, {"href": url}))
        else:
            for (alt, url) in matching_list:
                per_node_result_list.append(TextNode(alt, TextType.LINK, {"href": url}))

        new_nodes.extend(per_node_result_list)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]):
    per_node_result_list: list[TextNode] = []
    new_nodes: list[TextNode] = [] 
    text_nodes: list[str] = []
    for node in old_nodes:
        
        text_nodes = []
        matching_list: list[tuple[str,str]] = extract_markdown_images(node.text)    
        if len(matching_list) == 0:
            new_nodes.append(node)
            continue
        
        text_nodes = re.split(r"!\[[^\[\]]*\]\([^\(\)]*\)", node.text)
        text_nodes = list(filter(lambda x: x != "" ,text_nodes))

        if len(text_nodes) != 0:
            zipped_text_links_nodes = zip(matching_list, text_nodes)


            for (alt, url), iter_text_nodes in zipped_text_links_nodes:
                
                per_node_result_list.append(TextNode(iter_text_nodes, TextType.TEXT))
                per_node_result_list.append(TextNode("", TextType.IMAGE, {"alt":alt ,"src": url}))
        else:
            for (alt, url) in matching_list:

                per_node_result_list.append(TextNode("", TextType.IMAGE, {"alt":alt ,"src": url}))

        new_nodes.extend(per_node_result_list)
    return new_nodes


def text_to_textnode(mk_text: str):
    result = [] 
    result =split_nodes_delimiter([TextNode(mk_text, TextType.TEXT)], "**", TextType.BOLD)
    
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    
    result = split_nodes_link(result)

    result = split_nodes_image(result)
    # print(f"result: {result}")
    return result
    
    
    
   
