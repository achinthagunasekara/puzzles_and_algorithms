# Word Order

You are given  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

## Constraints:

* The sum of the lengths of all the words do not exceed

## Input Format

The first line contains the integer, .
The next  lines each contain a word.

## Output Format

On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

## Example

### Sample Input

```
4
bcdef
abcdefg
bcde
bcdef
```

### Sample Output

```
3
2 1 1
```

## Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions.

The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
