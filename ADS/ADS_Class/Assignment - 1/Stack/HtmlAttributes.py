import re
from UnlimitedStack import UnlimitedStack

def match_html_tags(html_content):
    stack = UnlimitedStack()
    # Regex pattern to match HTML tags, including those with attributes
    pattern = re.compile(r'</?([a-zA-Z0-9]+)[^>]*>')
    
    for match in pattern.finditer(html_content):
        tag = match.group(0)
        if tag.startswith('</'):
            # Closing tag
            tag_name = tag[2:-1].strip().lower()  # Extract and normalize tag name
            if stack.isEmpty() or stack.stackPop() != tag_name:
                print(f"Mismatch found: Expected {tag_name}, but stack had a different tag or was empty.")
                return False
        else:
            # Opening tag
            tag_name = tag[1:-1].split()[0].strip().lower()  # Extract and normalize tag name
            # Handle self-closing tags: check if the tag ends with '/>'
            if not (tag.endswith('/>') or tag_name in ["meta", "link", "img", "br", "hr", "input", "source", "track", "param"]):
                stack.stackPush(tag_name)
        
        # Debug prints
        print(f"Processed tag: {tag}, Stack state: {stack}")

    # Ensure all tags are properly closed
    if not stack.isEmpty():
        print(f"Stack not empty at the end: {stack}")
    
    return stack.isEmpty()

def main():
    # Path to the HTML file
    file_path = r'E:\BDA_LABS_24\ADS\ADS_Lab\Stack\HtmlAttributes.txt'
    
    # Read the HTML content from the file
    with open(file_path, 'r') as file:
        html_content = file.read()
    
    # Check if HTML tags match
    result = match_html_tags(html_content)
    print(f"HTML tags match: {result}")  # Should print True or False

if __name__ == "__main__":
    main()
