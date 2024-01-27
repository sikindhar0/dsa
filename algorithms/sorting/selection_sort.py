def selection_sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]

arr = [3,5,2,8,1,9,55,6]
selection_sort(arr)
print(arr)  
