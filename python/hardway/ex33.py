i = 0
total = 6
# numbers is an empty list
numbers = []

# do a loop from 0 to 5
while i < total:
  print "At the top i is %d" % i
  numbers.append(i)
  
  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i
  
  
print "The numbers: "
  
# loop through the numbers list 
for num in numbers:
  print num
