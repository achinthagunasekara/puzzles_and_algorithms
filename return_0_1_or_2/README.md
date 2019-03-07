# Return 0, 1 and 2 with equal probability using the specified function

Write an algorithm to generate 0, 1 and 2 with equal probability using a specified function which either produces 0 or 1 with 50% probability each.

## Explanation

Lets say the specified function is `random()` which generates 0 or 1 with `50%` probability each. Then if we make two different calls to the `random()` function and store the result in two variables, say x and y, then their sum `(x + y)` can be any of `{ 0, 1, 2 }`. Here the probability of getting 0 and 2 is `25%` each and probability of getting 1 is `50%`.
