import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heap = list(strings)
    heapq.heapify(heap)
    return heap

def heapify_integers(integers: List[int]) -> List[int]:
    heap = list(integers)
    heapq.heapify(heap)
    return heap


def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    result = []

    while nums:
        result.append(heapq.heappop(nums))
    return result


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
