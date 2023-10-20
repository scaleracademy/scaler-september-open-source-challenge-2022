/*    Copyright (c) 2022, <Srijoy Paul>
 *    All rights reserved
 */
#include <iostream>

int main() {
  int num;

  std::cout << "Enter number of times to repeat: ";
  std::cin >> num;

  for (int i = num; i >= 1; i--) {
    std::cout << "Focussed" << std::endl;
  }

  return 0;
}
