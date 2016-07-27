import math
import time
class Magician():

  # def __init__(self):
  #   self.numtestNum = [];
  #   self.user = None
  #   self.user_choice = input('I am the Math Magician. What would you like me to do? ')

  def show_menu(self):

    print('I am the Math Magician. What would you like me to do? ')

    print("1. integers")
    print("2. fibonacci")
    print("3. primes")
    print("4. quit program")

    user_choice = input(">")
    if user_choice == "1":
       intNums = int(input("How many? "))
       self.create_integers(intNums)



    if user_choice == "2":
       fibNums = int(input("How many? "))
       self.create_fibonacci(fibNums)


    if user_choice == "3":
       primeNums = int(input("How many? "))
       self.create_primes(primeNums)


    if user_choice != "4":
       self.show_menu()



  def create_integers(self, testNum):


    intList = []
    for x in range(testNum):
      intList.append(x+1)
    for i in intList:
      print(i)
      time.sleep(1)
    return intList


  def create_fibonacci(self, testNum):
    fibList = []
    a,b = 1,1
    for i in range(testNum-1):
      a,b = b,a+b
      fibList.append(a)
    for i in fibList:
      print(i)
      time.sleep(1)
    return fibList

  def create_primes(self, testNum):
    i, x = 2, 1
    primeList = []

    # x starts at 2 and ends at whatever the user typed in
    # for number of numbers to display
    while x <= testNum:

      # Start by assuming it is a prime number
      isPrime = True

      # Using the range 2...(square root of current number)
      for n in range(2, int(math.sqrt(i) + 1)):

        # If there is not a remainder with modulo calculation
        # then it's not a prime number
        if i % n == 0:
          isPrime = False
          break

      # Range loop is done, check if prime got negated
      # If not then we know it's a prime number
      if isPrime:
        primeList.append(i)
        x += 1

      i += 1
    for a in primeList:
      print(a)
      time.sleep(1)
    return primeList



if __name__ == '__main__':
  mage = Magician()
  mage.show_menu()
