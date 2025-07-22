def say_hello(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(say_hello(name))
    else:
        print("Usage: python app.py <name>")