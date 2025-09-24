digits_1 = set(map(float, input().split()))
digits_2 = set(map(float, input().split()))

print("1. Числа, которые присутствуют в обоих наборах одновременно. ")
print(digits_1 & digits_2)

print("2. Числа из первого набора, которые отсутствуют во втором, и наоборот. ")
print(digits_1 - digits_2)
print(digits_2 - digits_1)

print("3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1. ")
print(digits_1 ^ digits_2)