"""Tower of Hanoi is a mathematical puzzle where we have three rods
(A, B, and C) and N disks. Initially, all the disks are stacked in decreasing
value of diameter i.e., the smallest disk is placed on the top and they are on
rod A. The objective of the puzzle is to move the entire stack to another rod
(here considered C), obeying the following simple rules:
    - Only one disk can be moved at a time.
    - Each move consists of taking the upper disk from one of the stacks and
      placing it on top of another stack i.e. a disk can only be moved if it
      is the uppermost disk on a stack.
    - No disk may be placed on top of a smaller disk."""


def TowerOfHanoi(n, from_rod, to_rod, aux_rod, y):
    if n == 0:
        return y
    y = TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod, y)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    y += 1
    y = TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod, y)
    return y


if __name__ == "__main__":
    temp = TowerOfHanoi(int(input("No. of disks: ")), "A", "C", "B", 0)
    print(f"{temp} moves")
