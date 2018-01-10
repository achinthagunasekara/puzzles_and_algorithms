""" Questions """

# pylint: disable=invalid-name

import re

"""
Write a program which prints out all numbers between 1 and 100.
When the program would print out a number exactly divisible by 4,
print "Linked". When it would print out a number exactly divisible by 6, print "In".
When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn".
Print nothing for numbers not divisible.
"""


for integer in range(1, 101):
    output = ''
    if (integer % 4) == 0:
        output = '4In'
    if (integer % 6) == 0:
        output += '6In'
    if output:
        print output

"""
// Remove comments from main.c file
// main.c contents:
int main()
{
   // printf() displays the string inside quotation
   printf("Hello, World!");
   printf("foo"); /* More comments
And more comments
*/ return 0;
}

Expected output:
int main()
{
   printf("Hello, World!");
   return 0;
}
"""

lines_without_comments = []

with open('test.txt') as code_file:
    ignore_next_line = False
    for line in code_file:
        # Skip lines starting with //
        if not re.match(r' *//.*', line):
            # Catch multiline comments
            cleaned_line = re.sub(r'/\*.*', '', line)
            cleaned_line = re.sub(r'.*\*/', '', cleaned_line)
            if cleaned_line and not ignore_next_line:
                lines_without_comments.append(cleaned_line)
            if re.match(r'.*/\*.*', line) and not re.match(r'.*\*/.*', line):
                ignore_next_line = True
            else:
                ignore_next_line = False

for line in  lines_without_comments:
    print line

"""
Given an array of contacts with phone/emails, detect and union identical contacts.
Contacts array:
[ [ "John", "john@gmail.com", "john@linkedin.com"],
[ "Dan", "dan@gmail.com", "+1234567"],
[ "john123", "+5412312", "john123@skype.com"],
[ "john1985", "+5412312", "john@linkedin.com"] ]

We can see that john1985, John and john123 are the same person by their contact information.

Output: (0,2,3 are the same person and 1 is another one)
[[ 0, 2, 3], [1]]
"""

people_list = [
    ["John", "john@gmail.com", "john@linkedin.com"],
    ["Dan", "dan@gmail.com", "+1234567"],
    ["john123", "+5412312", "john123@skype.com"],
    ["john1985", "+5412312", "john@linkedin.com"]
]

all_unique = []

def find_unique(unique, index, people):
    """ Find unique for a given index """
    for loop_index, person in enumerate(people):
        if len(set(people[index] + person)) < 6:
            if not loop_index in unique:
                unique.append(loop_index)
                if index != loop_index:
                    unique = find_unique(unique, loop_index, people)
    return unique

for current_index, each_person in enumerate(people_list):
    if not any(current_index in index for index in all_unique):
        all_unique.append(find_unique([], current_index, people_list))

print all_unique
