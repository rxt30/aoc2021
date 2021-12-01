const fs = require('fs')

const readFiles = (fileName) => {
  return fs.readFileSync(fileName).toString().split('\n')
}

const countIncreases = (numbers) => {
  let increases = 0
  let firstWindow = 0
  let secondWindow = 0
  for(i=0; i <= numbers.length; i++) {
    if(Number(numbers[i]) < Number(numbers[i+3])){
      increases++
    }
  }
  return increases
}

numbers = readFiles("./input0101.txt")
increases = countIncreases(numbers)
console.log(`The number of incresease is ${increases}`)
