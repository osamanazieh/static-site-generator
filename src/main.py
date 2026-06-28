import os 
import sys
import shutil
from utility.fetch_title import fetch_title
from utility.generate_page import generate_page
from utility.generate_pages_recursive import generate_pages_recursive


def copy(src, dst):
    
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            # print(f"copy {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            # print(f"Entering directory: {src_path}")
            copy(src_path, dst_path) 

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"



    
    current_dirname = os.path.dirname(__file__)
    path_folders = current_dirname.split("/")[:-1]
    project_dir = "/".join(path_folders)
    dst_dir = os.path.join(project_dir, "docs")
    src_dir = project_dir + "/static"
    copy(src_dir, dst_dir)




    from_path = os.path.join("/".join(os.path.dirname(__file__).split("/")[:-1]), "content")
    print(os.path.dirname(__file__))
    template_path = os.path.join("/".join(os.path.dirname(__file__).split("/")[:-1]) ,"template.html")
    dest_path = os.path.join("/".join(os.path.dirname(__file__).split("/")[:-1]), "docs")
    
    generate_pages_recursive(from_path, template_path, dest_path, basepath)
main()