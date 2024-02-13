import unittest
from GenerateNumber import gnome_sort, archiveNumbers, merge_sort, shell_sort, selection_sort, countingSort, radixSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        # Se inicializa la lista de números ordenada y desordenada
        self.sorted_numbers = list(range(3000))
        self.random_numbers = archiveNumbers.copy()

    def test_gnome_sort_sorted_list(self):
        sorted_list = gnome_sort(self.sorted_numbers)
        self.assertEqual(sorted_list, self.sorted_numbers)

    def test_gnome_sort_random_list(self):
        sorted_list = gnome_sort(self.random_numbers)
        self.assertEqual(sorted_list, sorted(self.random_numbers))

    def test_merge_sort_sorted_list(self):
        sorted_list = merge_sort(self.sorted_numbers)
        self.assertEqual(sorted_list, self.sorted_numbers)

    def test_merge_sort_random_list(self):
        sorted_list = merge_sort(self.random_numbers)
        self.assertEqual(sorted_list, sorted(self.random_numbers))

    def test_shell_sort_sorted_list(self):
        sorted_list = shell_sort(self.sorted_numbers)
        self.assertEqual(sorted_list, self.sorted_numbers)

    def test_shell_sort_random_list(self):
        sorted_list = shell_sort(self.random_numbers)
        self.assertEqual(sorted_list, sorted(self.random_numbers))

    def test_selection_sort_sorted_list(self):
        sorted_list = self.sorted_numbers.copy()
        selection_sort(sorted_list)
        self.assertEqual(sorted_list, self.sorted_numbers)

    def test_selection_sort_random_list(self):
        sorted_list = self.random_numbers.copy()
        selection_sort(sorted_list)
        self.assertEqual(sorted_list, sorted(self.random_numbers))

    def test_radix_sort_sorted_list(self):
        sorted_list = self.sorted_numbers.copy()
        radixSort(sorted_list)
        self.assertEqual(sorted_list, self.sorted_numbers)

    def test_radix_sort_random_list(self):
        sorted_list = self.random_numbers.copy()
        radixSort(sorted_list)
        self.assertEqual(sorted_list, sorted(self.random_numbers))

    # Tests para Counting Sort
    def test_counting_sort_sorted_list(self):
        sorted_list = self.sorted_numbers.copy()
        countingSort(sorted_list, 1)  # Ordenamos con Counting Sort usando cualquier place
        self.assertEqual(sorted_list, self.sorted_numbers)

    def test_counting_sort_random_list(self):
        sorted_list = self.random_numbers.copy()
        countingSort(sorted_list, 1)  # Ordenamos con Counting Sort usando cualquier place
        self.assertEqual(sorted_list, sorted(self.random_numbers))



if __name__ == "__main__":
    unittest.main()


