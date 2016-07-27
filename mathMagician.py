import math
import time
class Magician():

  # def __init__(self):
  #   self.numCount = [];
  #   self.user = None
  #   self.user_choice = input('I am the Math Magician. What would you like me to do? ')

  def show_menu(self):

    print('I am the Math Magician. What would you like me to do? ')

    print("1. integers")
    print("2. fibonacci")
    # print("3. primes")
    print("4. quit program")

    user_choice = input(">")
    if user_choice == "1":
       intNums = int(input("How many? "))
       self.create_integers(intNums)



    if user_choice == "2":
       fibNums = int(input("How many? "))
       self.create_fibonacci(fibNums)


    # if user_choice == "3":
    #    primeNums = input("How many? ")
    #    self.create_primes(primeNums)


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

  # def create_primes(self, testNum):
  #   primeList = []
  #   count = testNum

  #   while True:
  #       isprime = True

  #       for x in range(2, int(math.sqrt(count) + 1)):
  #           if count % x == 0:
  #               isprime = False
  #               break

  #       if isprime:
  #           print (count)
  #           print(isprime)

  #       count += 1
  #       primeList.append(is)

  #       return primeList



if __name__ == '__main__':
  mage = Magician()
  mage.show_menu()
