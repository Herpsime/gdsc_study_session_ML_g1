import numpy as np

number = [9,5,2,3,7]
num = np.array(number)

mean = np.mean(num)
max = np.max(num)
sum = np.sum(num)

print(f"the numbers are {number}")
print(f"their mean is {mean}")
print(f"their max is {max}")
print(f"their sum is {sum}")