// Bubble sort algorithm in javascript

// bubble sort function
function bubbleSorting (arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j + 1]
        arr[j + 1] = arr[j]
        arr[j] = temp
      }
    }
  }
  console.log(arr)
}

// calling the above function
bubbleSorting([1, 20, 8, 8, 15, 30, 2, 4, 5])
