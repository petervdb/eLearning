from sys import argv

# variable script is the name of the script

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	# Go to byte 0 or to the beginning of the file
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

# open the file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# print the first line
current_line = 1
print_a_line(current_line, current_file)

# print the second line
current_line = current_line + 1
print_a_line(current_line, current_file)

# print the third line
# notice that this is another method to increase the variable
current_line += 1
print_a_line(current_line, current_file)

print"Then name of this script is %s" % script
