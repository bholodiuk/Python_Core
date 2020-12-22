"""
Given an array of integers.

Return an array, where the first element is the count of positives
numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""

def count_positives_sum_negatives(arr):
    if arr:
        positive_count = len([digit for digit in arr if digit > 0])
        negative_sum = sum([digit for digit in arr if digit < 0])
        return [positive_count, negative_sum]
    else:
        return []

if __name__ == '__main__':
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
    print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
    print(count_positives_sum_negatives([1]), [1, 0])
    print(count_positives_sum_negatives([-1]), [0, -1])
    print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
    print(count_positives_sum_negatives([]), [])