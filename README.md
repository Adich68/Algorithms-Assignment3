# Programming Assignment 3: Highest Value Common Subsequence
**Names:** Peyton Hecht (99580280), Adi Chauhan (78721054)  
**Course:** COP4533  
**Date:** April 6, 2026  

---

**Execution Instructions:**  
Navigate to the root directory of this repository in terminal. Run the `hvlcs.py` script located in the `src` folder, and pass the path to your input file as a command-line argument.

**Example Command:**
```bash
python src/hvlcs.py data/example.in
```

---

## Question 1: Empirical Comparison

The runtime grows as string length increases, consistent with the expected O(m×n) behavior.

**Results:**
| Test File | String Length | Runtime (seconds) |
|-----------|--------------|-------------------|
| test1.in  | 25           | 0.0399            |
| test2.in  | 50           | 0.0405            |
| test3.in  | 100          | 0.0411            |
| test4.in  | 200          | 0.0473            |
| test5.in  | 300          | 0.0500            |
| test6.in  | 400          | 0.0599            |
| test7.in  | 500          | 0.0817            |
| test8.in  | 600          | 0.1203            |
| test9.in  | 700          | 0.1280            |
| test10.in | 800          | 0.1659            |

![Runtime Graph](image.png)

## Question 2: Recurrence Equation

**Base Cases:**
* `OPT(i, 0) = 0`
* `OPT(0, j) = 0`

**Recurrence:**
* If `A[i] == B[j]`: `OPT(i, j) = OPT(i-1, j-1) + v(A[i])`
* If `A[i] != B[j]`: `OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1))`

**Explanation:** Let `OPT(i, j)` represent the maximum value of a common subsequence for the prefix of A up to index `i` and the prefix of B up to index `j`. For the base cases, if either string prefix is empty (length = 0), they can't share any characters, so the max val is 0. 

For the recurrence, if the current characters match (`A[i] == B[j]`), append to the optimal common subsequence of the prior characters. To maximize the score, we add the matching character's value, `v(A[i])`, to the optimal score of the remaining prefixes `OPT(i-1, j-1)`. If the characters don't match, they can't both be part of the optimal common subsequence for this step sp we must see what happens if we ignore the last character of A (`OPT(i-1, j)`) or ignore the last character of B (`OPT(i, j-1)`). We take the `max()` of the two choices to make sure we carry forward the highest possible value.

---

## Question 3: Big-Oh

**Pseudocode:**
```text
m = length of string A
n = length of string B
2D matrix 'score' with (m + 1) rows and (n + 1) columns, equal to 0
for row from 1 to m:
    for col from 1 to n:
        if A[row] = B[col]:
            char_weight = values[A[row]]
            score[row][col] = score[row-1][col-1] + char_weight
        else:
            skip_A = score[row-1][col]
            skip_B = score[row][col-1]
            score[row][col] = max(skip_A, skip_B)
return score[m][n]
```

**Runtime:** O(m × n)

**Explanation:** The algorithm uses a 2D matrix named `score` to keep track of the max values, using the lengths of the two strings for its dimensions. It uses two nested `for` loops to go through every single position in the matrix. In the loop, it only performs constant-time `O(1)` operations by checking if characters match, pulling a weight from the dict, doing a simple addition, or comparing two numbers to find the maximum. Because it does `O(1)` work exactly `m × n` times, the overall time complexity is `O(m × n)`.
