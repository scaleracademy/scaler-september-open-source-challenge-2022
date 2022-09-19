// Binary Search Algorithm
function binarySearch (arr, ele) {
  let i = 0
  let j = arr.length - 1
  while (i <= j) {
    const mid = parseInt((i + j) / 2)
    if (arr[mid] === ele) return mid
    else if (arr[mid] > ele) j = mid - 1
    else i = mid + 1
  }
  return -1
}

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const search = 7
console.log(binarySearch(arr, search))
