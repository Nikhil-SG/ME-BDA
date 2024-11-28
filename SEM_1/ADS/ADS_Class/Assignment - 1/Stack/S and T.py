from UnlimitedStack import UnlimitedStack

def transfer(S, T):
    # Create an auxiliary stack
    auxiliary = UnlimitedStack()
    
    # Transfer elements from S to auxiliary stack
    while not S.isEmpty():
        auxiliary.stackPush(S.stackPop())
    
    # Transfer elements from auxiliary stack to T
    while not auxiliary.isEmpty():
        T.stackPush(auxiliary.stackPop())

def main():
    # Create stacks
    S = UnlimitedStack()
    T = UnlimitedStack()
    
    # Push elements onto stack S
    S.stackPush(1)
    S.stackPush(2)
    S.stackPush(3)
    
    print("Stack S before transfer:", S)
    print("Stack T before transfer:", T)
    
    # Transfer elements from S to T
    transfer(S, T)
    
    print("Stack S after transfer:", S)
    print("Stack T after transfer:", T)

if __name__ == "__main__":
    main()


