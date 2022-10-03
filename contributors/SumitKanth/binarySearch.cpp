/*    Copyright (c) 2022, <Sumit Kanth>
 *    All rights reserved
 */
#include <bits/stdc++.h>

int binarysearch(int arr[], int n, int k) {
  int s = 0;
  int e = n - 1;
  while (s <= e) {
    int mid = (s + e) / 2;
    if (k == arr[mid]) {
      return mid;
    } else if (k > arr[mid]) {
      s = mid + 1;
    } else {
      e = mid - 1;
    }
  }
  return -1;
}

int main() {
  int arr[] = {11, 22, 33, 44, 55};
  int size = sizeof(arr) / sizeof(arr[0]);
  int k = 445;
  std::cout << binarysearch(arr, size, k) << std::endl;
  return 0;
}
