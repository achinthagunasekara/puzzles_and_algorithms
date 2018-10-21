# Job Assignment Problem

You are the head of a firm and you have to assign jobs to people. You have N persons working under you and you have N jobs that are to be done by these persons. Each person has to do exactly one job and each job has to be done by exactly one person. Each person has his own capability (in terms of time taken) to do any particular job. Your task is to assign the jobs to the persons in such a way that the total time taken is minimum. A job can be assigned to only one person and a person can do only one job.

## Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.  The first line of each test case contains an integer N, where N is the number of jobs and the number of persons under you. The next line contains N2 positive integers. The first N of these integers denote the time taken by the first person to do the N jobs, the next N integers denote the time taken by the second person to do the N jobs and so on till the Nth person.

## Output

For each test case in a new line, print the time taken in the best possible assignment that you can do.

## Constrains:

* 1 <= T <= 100
* 1 <= N <= 30
* 1 <= Time taken to do a job <= 100


## Example

### Input

```
Enter the number of test cases: 2
Enter the number of people: 2
Enter the efficiency for each person for each job: 3 5 10 1
Enter the number of people: 3
Enter the efficiency for each person for each job: 2 1 2 9 8 1 1 1 1
```

### Output

```
INFO:solution:Minimum time to do the job for test case 0 is: 
INFO:solution:Minimum time to do the job for test case 1 is: 3
```

### Explanation

The first person takes times 3 and 5 for jobs 1 and 2 respectively. The second person takes times 10 and 1 for jobs 1 and 2 respectively. We can see that the optimal assignment will be to give job 1 to person 1 and job 2 to person 2 for a total for 3 + 1 = 4.
