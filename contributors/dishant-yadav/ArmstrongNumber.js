const checkArmstrong = (num) => {
  const copy = num
  let sumOfCubes = 0
  while (num !== 0) {
    const digit = num % 10
    sumOfCubes += Math.pow(digit, 3)
    num = parseInt(num / 10)
  }

  if (copy === sumOfCubes) {
    console.log(copy + ' is an Armstrong Number.')
  } else {
    console.log(copy + ' is not an Armstrong Number.')
  }
}

checkArmstrong(125)
// 125 is not an Armstrong Number.

checkArmstrong(153)
// 153 is an Armstrong Number.
