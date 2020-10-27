def ft_filter(function_to_apply, list_of_inputs):
    
    new_list = [x for x in list_of_inputs if function_to_apply(x) == True]
    return new_list



def positive(x):
    return x > 0


list1 = [1,-2,3]


print(ft_filter(positive, list1))