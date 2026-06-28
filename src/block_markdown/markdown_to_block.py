def markdown_to_blocks(markdown_doc: str) -> list[str]:
    markdown_blocks = list(map(lambda x: x.strip(), markdown_doc.split("\n\n")))
    markdown_blocks = list(filter(lambda x: x != " ", markdown_blocks))
    # print(markdown_blocks)
    return markdown_blocks


markdown_to_blocks("""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""")