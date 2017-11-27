# Queen's Attack II

This puzzle was taken from [HackerRank](https://www.hackerrank.com/challenges/queens-attack-2/problem)

A queen is standing on an n x n chessboard. The chessboard's rows are numbered from 1 to n, going from bottom to top; its columns are numbered from 1 to n, going from left to right. Each square on the board is denoted by a tuple, (r, c), describing the row, r and clumon, c, where the square is located.

The queen is standing at position (rq, cq) and, in a single move, she can attack any square in any of the eight directions (left, right, up, down, or the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from (4, 4).

![Image 1](https://raw.githubusercontent.com/achinthagunasekara/puzzles_and_algorithms/master/Queens_Attack_II/images/1.png)

There are k obstacles on the chessboard preventing the queen from attacking any square that has an obstacle blocking the the queen's path to it. For example, an obstacle at location (3, 5) in the diagram above would prevent the queen from attacking cells (3, 5), (2, 6) and (1, 7):

![Image 2](https://raw.githubusercontent.com/achinthagunasekara/puzzles_and_algorithms/master/Queens_Attack_II/images/2.png)

Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (rq, cq).

#### Input Format

The first line contains two space-separated integers describing the respective values of n (the side length of the board) and k (the number of obstacles).

The next line contains two space-separated integers describing the respective values of rq and cq, denoting the position of the queen.

Each line i of the k subsequent lines contains two space-separated integers describing the respective values of ri and ci, denoting the position of obstacle i.

#### Constraints

* 0 <= n <= 10 (power of 5)
* 0 <= k <= 10 (power of 5)
* A single cell may contain more than one obstacle; however, it is guaranteed that there will never be an obstacle at position (rq, cq) where the queen is located.

#### Subtasks

For 30% of the maximum score:

* 0 < n <= 100
* 0 <= k <= 100

For 55% of the maximum score:

* 0 < n <= 1000
* 0 <= k <= 10 (power of 5)

#### Output Format

Print the number of squares that the queen can attack from position (rq, cq).

Sample Input 0

```
4 0
4 4
```

Sample Output 0

```
9
```
