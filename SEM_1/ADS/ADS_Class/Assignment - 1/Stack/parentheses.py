from UnlimitedStack import UnlimitedStack

def match_parentheses(expression, lefty='([{', righty=')]}'):
    stack = UnlimitedStack()
    matching = dict(zip(righty, lefty))  # Create a mapping for closing to opening

    for char in expression:
        if char in lefty:
            stack.stackPush(char)
        elif char in righty:
            if stack.isEmpty() or stack.stackPeek() != matching[char]:
                print("Parentheses are not balanced.")
                return False
            stack.stackPop()

    if stack.isEmpty():
        print("Parentheses are balanced.")
        return True
    else:
        print("Parentheses are not balanced.")
        return False

def main():
    # Prompt user for input
    expression = input("Enter an expression to check for balanced parentheses: ")

    # Check if the expression has balanced parentheses
    match_parentheses(expression)

if __name__ == "__main__":
    main()