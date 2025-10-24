# Extraction of baby name from file using regex not using built-in libraries, create a sort algorithm, implement binary search., create a sort algorithm, implement binary search.
import re
with open("baby2008.html", "r", encoding="utf-8") as file:
    data = file.read()

year_match = re.search(r'Popularity\s+in\s+(\d{4})', data)
if year_match:
    print("Year:", year_match.group(1))

pattern = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
matches = re.findall(pattern, data)

for rank, boy, girl in matches:
    print(rank, boy, girl)


# selection sort algorithm (sorting algorithm)
numbers = [64, 25, 12, 22, 11]
for i in range(len(numbers)):
    min_idx = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
print("Sorted array is:", numbers)

# binary search algorithm
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right)// 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(f"binary search is at index : {binary_search(numbers, 22)}")