import re
from UnlimitedStack import UnlimitedStack

def match_html_tags(html_content):
    stack = UnlimitedStack()
    # Regex pattern to match HTML tags
    pattern = re.compile(r'</?([a-zA-Z0-9]+)[^>]*>')
    
    for match in pattern.finditer(html_content):
        tag = match.group(0)
        if tag.startswith('</'):
            # Closing tag
            tag_name = tag[2:-1]
            if stack.isEmpty() or stack.stackPop() != tag_name:
                return False
        else:
            # Opening tag
            tag_name = tag[1:-1].split()[0]
            stack.stackPush(tag_name)
    
    return stack.isEmpty()

def main():
    file_path = 'D:/BDA_1_Sem/ADS/ADS_Lab/Stack/HTML.txt'
    
    with open(file_path, 'r') as file:
        html_content = file.read()
    

    result = match_html_tags(html_content)
    print(f"HTML tags match: {result}")  # Should print True or False

if __name__ == "__main__":
    main()
