def greet(name, owner):
    hello = "Hello"
    if name == owner:
        return hello + " boss"
    else:
        return hello + " guest"
