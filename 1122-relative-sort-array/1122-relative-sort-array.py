class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        for x in arr2:
            while x in arr1:
                result.append(x)
                arr1.remove(x)

        arr1.sort()
        result.extend(arr1)

        return result