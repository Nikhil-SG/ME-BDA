from UnlimitedStack import UnlimitedStack

class Browser:
    def __init__(self):
        self.back_stack = UnlimitedStack()
        self.forward_stack = UnlimitedStack()
        self.current_url = None

    def visit(self, url):
        if self.current_url is not None:
            self.back_stack.stackPush(self.current_url)
        self.current_url = url
       
        self.forward_stack = UnlimitedStack()
        print(f"Visited: {self.current_url}")

    def back(self):
        if not self.back_stack.isEmpty():
            self.forward_stack.stackPush(self.current_url)
            self.current_url = self.back_stack.stackPop()
            print(f"Back to: {self.current_url}")
        else:
            print("No more history to go back to.")

    def forward(self):
        if not self.forward_stack.isEmpty():
            self.back_stack.stackPush(self.current_url)
            self.current_url = self.forward_stack.stackPop()
            print(f"Forward to: {self.current_url}")
        else:
            print("No more pages to go forward to.")

    def current(self):
        return self.current_url


def main():
    browser = Browser()
    
    # Simulate browsing
    browser.visit("https://www.example.com")
    browser.visit("https://www.google.com")
    browser.visit("https://www.github.com")
    
    # Go back
    browser.back()       
    browser.back()       
    browser.back()       
    
    # Go forward
    browser.forward()    
    browser.forward()    
    browser.forward()    

    browser.visit("https://www.stackoverflow.com")
    
    # Go back and forward again
    browser.back()       
    browser.forward()    
    
    print("Current URL:", browser.current())

if __name__ == "__main__":
    main()
