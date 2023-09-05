/*    Copyright (c) 2022, Swadesh Panda
 *    All rights reserved
 */
#include <iostream>

void bubble_sort(int *arr, int n) {
  for (int i = 0; i < n - 1; i++)
    for (int j = 0; j < n - i - 1; j++)
      if (arr[j] > arr[j + 1])
        std::swap(arr[j], arr[j + 1]);
}

void print_arr(int *arr, int n) {
  std::cout << "sorted arr: ";
  for (int i = 0; i < n; i++)
    std::cout << arr[i] << " ";
}

int main() {
  int arr[] = {10, 8, 4, 2, 1, 7};
  int n = sizeof(arr) / sizeof(int);

  bubble_sort(arr, n);
  print_arr(arr, n);

  return 0;
}
