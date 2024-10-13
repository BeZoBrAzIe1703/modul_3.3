def print_params(a = 1, b = 'line', c = True):
    print (a, b, c)
print_params ()
print_params (b = 25)
print_params (c = [1, 2, 3])

values_list = [17.03, 'city', False]
values_dict = {'a': False, 'b': 45.073, 'c': 'BeZ'}

print_params (*values_list)
print_params(**values_dict)

values_list_2 = [742.907, 'Hello, World!']
print_params(*values_list_2, 576)