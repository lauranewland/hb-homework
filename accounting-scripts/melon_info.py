"""Print out all the melons in our inventory."""


from melons import melon


def print_melon(melon):
    """Print each melon with corresponding attribute information."""
    
    for key, value in melon.items():
        print(key)
        for value1, value2 in value.items():
            print(f"     {value1} : {value2}")
            


print_melon(melon)
