from collections import OrderedDict

ord_dict = OrderedDict([('banana', 1), ('cherry', 3), ('apple', 2)])
for key, value in ord_dict.items():
    print(key, value)