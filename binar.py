#Бінарний код
def binar(arr, item):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==item:
            return mid
        elif arr[mid]<item:
            low= mid+1
        elif arr[mid]>item:
            high=mid-1


arr=list(range(0,100))
item=99

resultate=binar(arr,item)
print(f"Число яке шукаємо {item}. Знайшли на позиції {resultate}")
