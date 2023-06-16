def color(**kwargs):
    color = kwargs.get('color')
    
    if isinstance(color, str):
        # If `color` is a string, do something
        print(f"{color} is a string.")
    elif isinstance(color, int):
        # If `color` is an integer, do something else
        print(f"{color} is an integer.")
    else:
        # If `color` is neither a string nor an integer, raise an error
        raise TypeError("Invalid input type. Expected a string or an integer.")