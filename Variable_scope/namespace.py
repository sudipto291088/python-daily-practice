global_var = 10

def outer_func():
    outer_var = 20
    def inner_func():
        inner_var = 30
        print(inner_var)
    print(outer_var)
    inner_func()
print(global_var)


outer_func()