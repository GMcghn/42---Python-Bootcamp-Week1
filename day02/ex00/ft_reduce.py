def ft_reduce(function_to_apply, list_of_inputs):
    x = list_of_inputs[0]
    for i in range(len(list_of_inputs)-1):
        y = function_to_apply(x, list_of_inputs[i+1])
        x = y
    return x

def smallest(x, y):
    if x < y:
        return x

    else:
        return y


# list1 = [1, -2, 3, 4, 5, 78]

# a = ft_reduce(smallest, list1)
# print(a)