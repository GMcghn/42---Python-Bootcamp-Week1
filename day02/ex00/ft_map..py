def ft_map(function_to_apply, list_of_inputs):
    
        zipped = zip(*list_of_inputs)
        new_list = [function_to_apply(x) for x in zipped]
        return new_list
            




