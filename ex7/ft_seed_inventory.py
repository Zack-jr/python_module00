def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == 'packet':
        print(f'{seed_type} seeds: {quantity} {unit} available')
    elif unit == 'grams':
        print(f'{seed_type} seeds: {quantity} {unit} total')
    elif unit == 'area':
        print(f'{seed_type} seeds: covers {quantity} square meters')
    else:
        print('Unknown unit type')

# type hints are just there to specify the data type of the parameters
# they have no role in the compilation
# ex: seed_type: str