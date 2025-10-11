class SortingAlgorithm:

    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def quicksort(self, arr):  # Add 'self' parameter for instance method
        # Base case: arrays with 0 or 1 element are already sorted
        if len(arr) <= 1:
            return arr

        # Choose pivot (middle element)
        pivot = arr[len(arr) // 2]

        # Partition: elements less than, equal to, and greater than pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sort left and right, then combine
        return self.quicksort(left) + middle + self.quicksort(right)

    def sort_numbers(self):
        # Example usage
        sorted_numbers = self.quicksort(self.numbers)
        print(f"Original: {self.numbers}")
        print(f"Sorted:   {sorted_numbers}")
        return sorted_numbers


# Usage
sorter = SortingAlgorithm()
sorter.sort_numbers()