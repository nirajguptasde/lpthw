# This program tells me that how much percent of the book I've read and how much is remaining
# It accepts two command line arguments pages_i_have_read total_pages_in_book
# It is part of the study drill for exercise 3 from the book learn python the hard way

import sys

pages_read = int(sys.argv[1])
total_pages = int(sys.argv[2])

def validate_query(read, total):
    if(read < total):
        return True
    else:
        return False

def find_remaining_book(read, total):
    remaining = (read /total) * 100
    return remaining





if(validate_query(pages_read, total_pages)):
    result = find_remaining_book(pages_read, total_pages)
    print("You have read", round(result, 2), "% of the book")
else:
    print("please check your input")




