import os
import sys 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from markdown_to_html_node import markdown_doc_to_html_node
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))
from fetch_title import fetch_title



def read_file(file_path) -> str:
    content = ""
    with open(file_path, "r") as f:
        content += f.read()
    return content
def generate_page(from_path, template_path, dest_path):
    # print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = read_file(from_path)
    template_content = read_file(template_path)
    node = markdown_doc_to_html_node(markdown_doc=markdown_content)
    html = node.to_html()
    title = fetch_title(markdown_content)
    
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    # print(f"writing to {dest_path}")
    with open(dest_path+"/index.html", "w") as f:
        f.write(template_content)




