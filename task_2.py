def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if low < len(arr):
        return (iterations, arr[low])
    else:
        return (iterations, None)

# Тестуємо двійковий пошук:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target_value = 4.4

result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (3, 4.4)
