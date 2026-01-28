# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zalabib- <zalabib-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 18:07:23 by zalabib-          #+#    #+#              #
#    Updated: 2026/01/28 15:59:21 by zalabib-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = int(input('Day 1 harvest: '))
    day2 = int(input('Day 2 harvest: '))
    day3 = int(input('Day 3 harvest: '))
    total = day1 + day2 + day3
    print(f'Total harvest: {total}')
