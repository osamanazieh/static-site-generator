from textnode import *
import re 


def set_text_type_for_old_nodes(node_result: list[TextNode], texts: list[str], text_type: TextType, old_node: TextNode, remainder: int):
    for i in range(len(texts)):
        if i % 2 == remainder:
            node_result.append(TextNode(text=texts[i], text_type=old_node.text_type))
        else:
            node_result.append(TextNode(text=texts[i], text_type=text_type))

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result: list[TextNode] = []
    for node in old_nodes:
        node_result = []
        if node.text_type != TextType.TEXT:
            node_result.append(TextNode(text=node.text.strip(delimiter), text_type=node.text_type))

        else:

            texts = node.text.split(delimiter)
            if len(texts) % 2 == 0:
                raise Exception("missing closing delimiter")
            
            if node.text[0] != delimiter:
                set_text_type_for_old_nodes(node_result,texts, text_type, node, 0)
            else:
                set_text_type_for_old_nodes(node_result,texts, text_type, node, 1)

                    
        result.extend(node_result)
    return result


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

        zipped_text_links_nodes = zip(matching_list, text_nodes)


        for (alt, url), iter_text_nodes in zipped_text_links_nodes:

            per_node_result_list.append(TextNode(iter_text_nodes, TextType.TEXT))
            per_node_result_list.append(TextNode(alt, TextType.LINK, url))

        new_nodes.extend(per_node_result_list)
    return new_nodes

#and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
#TextNode(This is , text, None), TextNode( with an , text, None)
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
        print(f"text_nodes: {text_nodes}")
        zipped_text_links_nodes = zip(matching_list, text_nodes)


        for (alt, url), iter_text_nodes in zipped_text_links_nodes:
            print((alt, url), iter_text_nodes)
            per_node_result_list.append(TextNode(iter_text_nodes, TextType.TEXT))
            per_node_result_list.append(TextNode(alt, TextType.IMAGE, url))

        new_nodes.extend(per_node_result_list)
    return new_nodes


def text_to_textnode(mk_text: str):
    result = [] 
    result =split_nodes_delimiter([TextNode(mk_text, TextType.TEXT)], "**", TextType.BOLD)
    
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    
    result = split_nodes_link(result)

    result = split_nodes_image(result)
    print(result)
    return result
    
    
    
   

text_to_textnode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
# node = TextNode(
# "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
# TextType.TEXT,
# )
# new_nodes = split_nodes_image([node])
# print(new_nodes)