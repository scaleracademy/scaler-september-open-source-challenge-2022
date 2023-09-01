/*    Copyright (c) 2022, <Tridib Bag>
 *    All rights reserved
 */
#include <iostream>

int main() {
  int rows;

  std::cout << "Enter number of rows: ";
  std::cin >> rows;

  for (int i = rows; i >= 1; --i) {
    for (int j = 1; j <= i; ++j) {
      std::cout << j << " ";
    }
    std::cout << std::endl;
  }

  return 0;
}
