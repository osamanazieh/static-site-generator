from textnode import TextNode, TextType
def main():
    markdown = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(markdown)
main()