from UnlimitedStack import UnlimitedStack

def reverse_file(input_file, output_file):
    stack = UnlimitedStack()
    
    # Read the file and push each line onto the stack
    with open(input_file, 'r') as file:
        for line in file:
            stack.stackPush(line.strip())
    
    # Pop each line from the stack and write it to the new file
    with open(output_file, 'w') as file:
        while not stack.isEmpty():
            file.write(stack.stackPop() + '\n')

def main():
    # Example usage of reverse_file
    reverse_file('Stack\Reverse.txt', 'Stack\output.txt')

if __name__ == "__main__":
    main()
