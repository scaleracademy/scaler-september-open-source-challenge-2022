/*    Copyright (c) 2022, Adyasha Samal
 *    All rights reserved
 */
#include <iostream>

int main() {
  int i, n;
  bool is_prime = true;

  std::cout << "Enter a positive integer: ";
  std::cin >> n;

  if (n == 0 || n == 1) {
    is_prime = false;
  }

  for (i = 2; i <= n / 2; ++i) {
    if (n % i == 0) {
      is_prime = false;
      break;
    }
  }

  if (is_prime)
    std::cout << n << " is a prime number";
  else
    std::cout << n << " is not a prime number";

  return 0;
}
