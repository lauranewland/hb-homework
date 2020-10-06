"""Print out all the melons in our inventory."""

from melons import melon


def print_melon(melon):
    """Print each melon with corresponding attribute information."""
    
    for key, values in melon.items(): #loops through the Key(Melon Names) with the values listed in a dictionary
        print(key)
        for attribute, value in values.items(): #loops each attribute(price, weight, flesh color, etc...)
            print(f"     {attribute} : {value}")
            
print_melon(melon)
