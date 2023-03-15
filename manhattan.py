# Calculating Manhattan Distance from Scratch
# from scipy.spatial.distance import cityblock
# import sys


# def manhattan_distance(point1, point2):
#     distance = 0
#     zipped = zip(point1, point2)
#     for x1, x2 in zipped:
#         difference = x2 - x1
#         absolute_difference = abs(difference)
#         distance += absolute_difference

#     return distance


# print(manhattan_distance([100, 200, 300, 400], [200, 300, 400, 500]))

# Menggunakan fungsi cityblock di scipy unutk mendapatkan jarak Manhattan
from scipy.spatial.distance import cityblock
import sys

array_input_first = []
array_input_second = []

try:
    n = int(input("How many input?:"))
except ValueError:
    sys.exit("The input is not an integer!")


print("Input untuk array pertama")

for i in range(0, n):
    try:
        input_first = int(input("index ke - {} = ".format(i)))
    except ValueError:
        sys.exit("The input is not an integer!")

    array_input_first.append(input_first)

print("Input untuk array kedua")

for i in range(0, n):
    try:
        input_second = int(input("index ke - {} = ".format(i)))
    except ValueError:
        sys.exit("The input is not an integer!")
    array_input_second.append(input_second)

print("Hasil jarak Manhattan = ", cityblock(
    array_input_first, array_input_second))

# Mengembalikan: 105

# array_input_first = []
# array_input_second = []
# distance = 0

# try:
#     n = int(input("How many input?:"))
# except ValueError:
#     sys.exit("The input is not an integer!")


# print("Input untuk array pertama")

# for i in range(0, n):
#     try:
#         input_first = int(input("index ke - {} = ".format(i)))
#     except ValueError:
#         sys.exit("The input is not an integer!")

#     array_input_first.append(input_first)

# print("Input untuk array kedua")

# for i in range(0, n):
#     try:
#         input_second = int(input("index ke - {} = ".format(i)))
#     except ValueError:
#         sys.exit("The input is not an integer!")
#     array_input_second.append(input_second)

# zipped = zip(array_input_first, array_input_second)

# for x1, x2 in zipped:
#     difference = x2 - x1
#     absolute_difference = abs(difference)
#     distance += absolute_difference

# print("Hasil jarak Manhattan = {}".format(distance))

# # print("Hasil jarak Manhattan = ", cityblock(
# #     array_input_first, array_input_second))
