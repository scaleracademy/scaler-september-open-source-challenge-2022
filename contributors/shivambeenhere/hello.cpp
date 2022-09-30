/*    Copyright (c) 2022, <Shivam Kumar>
 *    All rights reserved
 */
#include <iostream>
int search(int array[], int n, int x) {
  for (int i = 0; i < n; i++)
    if (array[i] == x)
      return i;
  return -1;
}
int main() {
  int array[] = {2, 4, 0, 1, 9};
  int x = 1;
  int n = sizeof(array) / sizeof(array[0]);
  int result = search(array, n, x);
  if (result != -1)
    std::cout << "Found!";
  std::cout << std::endl;
  return 0;
}
