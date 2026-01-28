def ft_count_harvest_recursive():
    max_days = int(input("Days until harvest: "))

    def recursion(current_day):
        if current_day <= max_days:
            print(f"Day {current_day}")
            recursion(current_day + 1)
        else:
            print("Harvest time!")

    recursion(1)

# defining a function inside another to grab the input
# without being re-prompted