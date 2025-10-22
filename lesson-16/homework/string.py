#1.Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.


import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array(my_list)
my_array

#2.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np
values=np.arange(2, 11)
matrix_3x3=values.reshape(3,3)
print("3x3 matritsa:\n", matrix_3x3)

#3.Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
import numpy as np
null_vector=np.zeros(10)
null_vector[5]=11
print("Yangilangan vektor:", null_vector)

#4.Write a NumPy program to create an array with values ranging from 12 to 38.
array=np.arange(12,39)
print("Massiv: ", array)

#5.Write a NumPy program to convert an array to a floating type.
int_array=np.array([1, 2, 3, 4, 5])
float_array=int_array.astype(float)
print("Float massiv: ", float_array)

#6.
import numpy as np

# Sample Centigrade arrays
centigrade_1 = np.array([0, 12, 45.21, 34, 99.91])
centigrade_2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0])

# Function to convert Centigrade to Fahrenheit
def c_to_f(celsius_array):
    return (9/5) * celsius_array + 32

# Convert arrays
fahrenheit_1 = c_to_f(centigrade_1)
fahrenheit_2 = c_to_f(centigrade_2)

# Print results
print("Values in Fahrenheit degrees:", fahrenheit_1)
print("Values in Centigrade degrees:", centigrade_2)
print("Values in Centigrade degrees:", centigrade_2)
print("Values in Fahrenheit degrees:", fahrenheit_2)

#7.Write a NumPy program to append values to the end of an array.

import numpy as np

# Original array
arr = np.array([10, 20, 30])

# Append qilinadigan yangi qiymatlar
new_values = [40, 50, 60, 70, 80, 90]

# Qiymatlarni array oxiriga qo'shish
appended_array = np.append(arr, new_values)

# Natijani chiqarish
print("Original array:", arr)
print("After append values to the end of the array:", appended_array)


#8.Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
import numpy as np

# 10 ta elementli tasodifiy massiv yaratish (0 va 1 orasidagi qiymatlar)
random_array = np.random.rand(10)

# O'rtacha qiymat (mean)
mean_value = np.mean(random_array)

# Mediana (median)
median_value = np.median(random_array)

# Standart og'ish (standard deviation)
std_dev = np.std(random_array)

# Natijani chiqarish
print("Tasodifiy massiv:", random_array)
print("O'rtacha qiymat (mean):", mean_value)
print("Mediana (median):", median_value)
print("Standart og'ish (std):", std_dev)


#9.Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

# 10x10 o'lchamdagi tasodifiy massiv yaratish (0 va 1 orasidagi qiymatlar)
random_array = np.random.rand(10, 10)

# Minimum qiymatni topish
min_value = np.min(random_array)

# Maksimum qiymatni topish
max_value = np.max(random_array)

# Natijani chiqarish
print("Tasodifiy 10x10 massiv:\n", random_array)
print("Minimum qiymat:", min_value)
print("Maksimum qiymat:", max_value)


#10.Create a 3x3x3 array with random values.

import numpy as np

# 10x10 o'lchamdagi tasodifiy massiv yaratish (0 va 1 orasidagi qiymatlar)
random_array = np.random.rand(10, 10)

# Minimum qiymatni topish
min_value = np.min(random_array)

# Maksimum qiymatni topish
max_value = np.max(random_array)

# Natijani chiqarish
print("Tasodifiy 10x10 massiv:\n", random_array)
print("Minimum qiymat:", min_value)
print("Maksimum qiymat:", max_value)
