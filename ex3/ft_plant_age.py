# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zalabib- <zalabib-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 18:13:12 by zalabib-          #+#    #+#              #
#    Updated: 2026/01/16 18:19:06 by zalabib-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = int(input('Enter plant age in days: '))
    if age <= 60 :
        print('Plant needs more time to grow.')
    else :
        print('Plant is ready to harvest!')