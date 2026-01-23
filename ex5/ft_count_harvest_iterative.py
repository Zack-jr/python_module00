def ft_count_harvest_iterative():
    max = int(input('Days until harvest: '))
    i = 1
    for i in range(1, max + 1):
        print(f'Day {i}')
        if i == max:
            print('Harvest time!')
