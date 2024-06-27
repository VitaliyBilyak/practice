#Вставний (Insertion Sort)
def Insertio_sortmax(arr):
    for i in range(1,len(arr)):
        tmp=arr[i]
        max_i= i
        while max_i>0 and tmp[1]>arr[max_i-1][1]:
            arr[max_i]=arr[max_i-1]
            max_i -=1
            arr[max_i]=tmp
    return  arr
arr = [
    ("justin", 134),
    ("michael", 380),
    ("rihanna", 217),
    ("lady", 490),
    ("abba", 315),
    ("juin", 25)
]

def Insertion_sortmin(arr):
    for i in range(1,len(arr)):
        tmp=arr[i]
        min_i= i
        while min_i>0 and tmp[1]<arr[min_i-1][1]:
            arr[min_i]=arr[min_i-1]
            min_i -=1
            arr[min_i]=tmp
    return  arr
arr2 = [
    ("justin", 134),
    ("michael", 380),
    ("rihanna", 217),
    ("lady", 490),
    ("abba", 315),
    ("juin", 25)
]
sort=Insertio_sortmax(arr)
sort2=Insertion_sortmin(arr2)
print(f"Перша спосіб{sort}\n Другий спосіб{sort2}")

