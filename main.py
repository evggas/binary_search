def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Найден элемент, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине
    return -1  # Если элемента нет

# Пример использования:
arr = [-8, -3, 0, 1, 5, 10]
target = 5
result = binary_search(arr, target)
print(f"Элемент {target} найден по индексу {result}" if result != -1 else "Элемент не найден")
