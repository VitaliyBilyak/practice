#ШВИДКА САРТІРОВКА
def quisort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[element for element in arr[1:] if element <=pivot]
        greater=[element for  element in arr[1:] if element>pivot]
        return quisort(less)+[pivot]+quisort(greater)
arr = [1, 2, 7, 3, 9, 10, 5, 14, 21, 17, 39, 41, 22]
sorted_numbers = quisort(arr)

print("Відсортований рядок чисел :", sorted_numbers)