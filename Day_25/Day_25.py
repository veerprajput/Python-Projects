import csv
import pandas

# with open('weather_data.csv') as csv_file:
#     data = csv.reader(csv_file)
#     temp = []
#     for row in data:
#         print(row)
#         if row[0] != 'day':
#             temp.append(int(row[1]))
#     print(temp)


# data = pandas.read_csv('weather_data.csv')
# # print(data)

# dict_data = data.to_dict()
# # print('\n\n\n\n')
# # print(dict_data)

# temp_list = data['temp'].to_list()
# print('\n\n\n\n')
# print(temp_list)

# numbers = dict_data['temp']
# print(numbers)

# sum = 0
# average_divisor = 0

# for k,v in numbers.items():
#     sum += v
#     average_divisor = k

# print(sum)
# print(average_divisor)

# average_divisor += 1

# print(f'The average temperature is {round(sum / average_divisor, 2)} Celsius')


# average = sum(temp_list) / len(temp_list)
# print(f'The average temperature is {round(average * 1.8 + 32, 2)}F')

# ht = data['temp'].max() * 1.8 + 32

# print(f"The maximum teperature is {ht}F")
# print('\n\n\n\n')
# print(data[data.temp == data['temp'].max()])



















data = pandas.read_csv('2018_Census_Squirrel.csv')

color_list = data['Primary Fur Color'].to_list()

gray_count = 0
cinnamon_count = 0
black_count = 0

for color in color_list:
    if color == 'Gray':
        gray_count += 1
    elif color == 'Cinnamon':
        cinnamon_count += 1
    elif color == 'Black':
        black_count += 1

print(gray_count)

data_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'Count': [
    str(gray_count),
    str(cinnamon_count),
    str(black_count),
    ]
}

more_data = pandas.DataFrame(data_dict)
more_data.to_csv('colors.csv')