# Calculates the probability of 'lucky' public ticket number occurence
# Tickets with a 6 digit serial number are considered 'lucky'
# when the sum of first and last 3 digits of the serial number are equal  

import time # to measure execution speed

class LuckyNumberCounter:

  def __init__(self, digitCount):
    self.digitCount = digitCount
    self.numberCount = 1
    
  def get_maximum(self, digitCount):
    x = int("9" * digitCount) 
    return x

  def get_splitter(self, digitCount):
    return int(digitCount / 2) if digitCount % 2 == 0 else False 

  def getRightNumberFormat(self, number):
    digits = [x for x in str(number)]
    while len(digits) != self.digitCount:
      digits.insert(0, '0')

    return "".join(digits)

  def isLuckyNumber(self, number):
    number = self.getRightNumberFormat(number)
    split = self.get_splitter(self.digitCount)

    if split == False:
      return "not splittable to 2 same halfs"
    
    first_half = sum([int(x) for x in number[:split]])
    second_half = sum([int(x) for x in number[split:]])
    
    return True if first_half == second_half else False

  def getLuckyNumberCount(self):
    maximum = self.get_maximum(self.digitCount)
    count = 0
    
    for i in range(maximum + 1):
      if self.isLuckyNumber(i) == True:
        count += 1

    return count  

digits = 4
lnc = LuckyNumberCounter(digits)

t_start= time.time_ns()                           # to measure execution speed
luckyNumbersTotal = lnc.getLuckyNumberCount()

print(luckyNumbersTotal)
print(f"Time elapsed: {(time.time_ns() - t_start) / 1e9} s") # to measure execution speed

# 1234

# 001 234

# luckyNumbersProbab = luckyNumbersTotal / lnc.numberCount

# print(lnc.digitCount, "digit lucky numbers count:", luckyNumbersTotal)
# print("Probability of getting a lucky number is:", luckyNumbersProbab, end=" ")
# print("so chance is 1 in", 1 / luckyNumbersProbab)



