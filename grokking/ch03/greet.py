def greet2(name):
    print(f"how are you, {name}?")

def bye():
    print("ok bye!")

def greet(name):
    print(f"hello, {name}!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("maggie")