def my_loop(counter):
  # numbers is an empty list
  i = 0
  numbers = []
  # do a loop from 0 to 5
  for i in range(0, counter):
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
  return numbers

total = 6
numbers = my_loop(total)  
  
print "The numbers: "
  
# loop through the numbers list 
for num in numbers:
  print num

