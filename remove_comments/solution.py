""" Solution """

# pylint: disable=invalid-name

import re

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
