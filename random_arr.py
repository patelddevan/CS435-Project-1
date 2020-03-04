import random

def getRandomArray(n):
  random_array = list()
  for i in range(n):
    random_int = getRandomNumber(n)
    while random_int in random_array:
      random_int = getRandomNumber(n)
    random_array.append(random_int)
  return random_array 

def getRandomNumber(n):
  return random.randint(0, n*10)

def getSortedArray(n):
  sorted_array = list()
  for i in range(n, 0, -1):
    sorted_array.append(i)
  return sorted_array



def main():
  print(getRandomArray(10))
  print(getSortedArray(10))

if __name__ == "__main__":
  main()
