import os 
import sys

from fetch_title import fetch_title
from generate_page import generate_page

def generate_pages_recursive(from_path, template_path, dest_path):
    
    for file_path in os.listdir(from_path):
        src_abs_file_path = os.path.join(from_path, file_path)
        
        print(f"file: {src_abs_file_path}")
        if not os.path.isdir(os.path.abspath(src_abs_file_path)):
            generate_page(src_abs_file_path, template_path, dest_path)
        
        else: 
            # print(f"is dir: {file_path}")
            dest_abs_file_path = os.path.join(dest_path, file_path)
            generate_pages_recursive(os.path.join(from_path, file_path), template_path, dest_abs_file_path)



tom_path = "/".join(os.path.dirname(__file__).split("/")[:-2]) +"/content"

dest_path = "/".join(os.path.dirname(__file__).split("/")[:-2])+"/public"

template_path = "/".join(os.path.dirname(__file__).split("/")[:-2])+"/template.html"

