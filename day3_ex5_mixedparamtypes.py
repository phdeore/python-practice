import inspect

def complex_func(a, b, /, c, d=10, *args, e, f=20, **kwargs):
    pass

func_sign = inspect.signature(complex_func)
print(func_sign)
for param in func_sign.parameters.values():
    print(param, param.kind.name, "no default" if param.default is param.empty else param.default)

