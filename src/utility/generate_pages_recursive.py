import os 


from fetch_title import fetch_title
from generate_page import generate_page

def generate_pages_recursive(from_path, template_path, dest_path, basepath):
    
    for file_path in os.listdir(from_path):
        src_abs_file_path = os.path.join(from_path, file_path)
        
       
        if not os.path.isdir(os.path.abspath(src_abs_file_path)):
            generate_page(src_abs_file_path, template_path, dest_path, basepath)
        
        else: 
            dest_abs_file_path = os.path.join(dest_path, file_path)
            generate_pages_recursive(os.path.join(from_path, file_path), template_path, dest_abs_file_path, basepath)


