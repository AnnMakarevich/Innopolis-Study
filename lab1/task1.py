numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
strk = numbers
strk[4] = 0
numbers[4] = sum(strk)/(len(strk))
print("Измененный список:", numbers)


# q = sum(x for x in numbers if x != None)
# print(q / len(numbers)), где numbers исходный массив.