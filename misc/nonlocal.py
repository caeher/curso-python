def outer_function():
    x = "enclosing"
    def inner_function():
        nonlocal x
        x = "local"
        print(f"inner_function: {x}")
    inner_function()
    print(f"outer_function: {x}")

outer_function()