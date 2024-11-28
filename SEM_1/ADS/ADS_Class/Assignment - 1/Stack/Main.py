from UnlimitedStack import UnlimitedStack
from LimitedStack import LimitedStack

def main():
    # Test UnlimitedStack
    print("Testing UnlimitedStack:")
    unlimited_stack = UnlimitedStack()
    
    # Push items onto the unlimited stack
    unlimited_stack.stackPush(1)
    unlimited_stack.stackPush(2)
    unlimited_stack.stackPush(3)
    
    print("Stack after pushing items:", unlimited_stack)
    print("Top item:", unlimited_stack.stackPeek())
    print("Popped item:", unlimited_stack.stackPop())
    print("Count of stack:", unlimited_stack.stackCount())
    print("Is the stack empty?", unlimited_stack.isEmpty())
    print("Final stack:", unlimited_stack)
    print()

    # Test LimitedStack
    print("Testing LimitedStack:")
    limited_stack = LimitedStack(maxSize=3)

    # Push items onto the limited stack
    try:
        limited_stack.stackPush(1)
        limited_stack.stackPush(2)
        limited_stack.stackPush(3)
        limited_stack.stackPush(4)
    except OverflowError as e:
        print("Error:", e)
    print("Stack after pushing items:", limited_stack)

    print("Top element of the stack:", limited_stack.stackPeek())
    print("Popped item from the stack:", limited_stack.stackPop())
    print("Size of the stack:", limited_stack.stackCount())
    print("Is the stack empty?", limited_stack.isEmpty())
    print("Is the stack full?", limited_stack.isFull())
    print("The final stack:", limited_stack)

if __name__ == "__main__":
    main()
