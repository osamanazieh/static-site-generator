import re

def fetch_title(markdown: str):
    if not re.findall(r"# (.*)", markdown):
        raise Exception("There is no title for this markdown, insert a main title with '# ' prefix")                                    
    title =re.findall(r"# (.*)", markdown)[0]
    markdown = re.sub(r"# (.*)", "", markdown) 
    return title