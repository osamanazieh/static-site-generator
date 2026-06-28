from enum import Enum
import re
class BlockType(Enum):
   PARAGRAPH = "paragraph"
   CODE = "code"
   UNORDERED_LIST = "unordered_list"
   ORDERED_LIST = "ordered_list"
   HEADING = "heading"
   QUOTE = "quote"

def block_to_block_type(markdown_block: str):
    if re.search(r"^#{1,6} ", markdown_block) is not None:
      return BlockType.HEADING
    elif re.search(r"^`{3}\n.*?`{3}$" ,markdown_block, re.S) is not None:
      return BlockType.CODE
    elif re.search(r"^> ?.*", markdown_block, re.S) is not None:
       return BlockType.QUOTE
    elif re.search(r"^-{1} .+", markdown_block, re.M) is not None:
       return BlockType.UNORDERED_LIST
    elif re.search(r"^\d+\. .+", markdown_block, re.M) is not None:
       return BlockType.ORDERED_LIST
    else:
       return BlockType.PARAGRAPH