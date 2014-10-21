import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)

# print each word seperately
print words
print "----------------------------"

# sort the words and print them
sorted_words = ex25.sort_words(words)
print sorted_words
print "----------------------------"

# display the first word
ex25.print_first_word(words)
print "----------------------------"

# display the last word
ex25.print_last_word(words)
print "----------------------------"

# display first word from the sorted array
ex25.print_first_word(sorted_words)
print "----------------------------"

# display last word from the sorted array
ex25.print_last_word(sorted_words)
print "----------------------------"

# display the first and last word
ex25.print_first_and_last(sentence)
print "----------------------------"

# display the first and last word of the sorted array
ex25.print_first_and_last_sorted(sentence)
print "----------------------------"
