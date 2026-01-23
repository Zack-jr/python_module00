# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zalabib- <zalabib-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 18:07:17 by zalabib-          #+#    #+#              #
#    Updated: 2026/01/16 18:07:21 by zalabib-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = int(input('Enter length: '))
    width =  int(input('Enter width: '))

    area = length * width
    print(f'Plot area: {area}')
