# Divide and Conquer - Assignments

<b> 1 Recurrences </b> Use both the recursion tree method and the (partial) substitution method to solve each of the following recurrences.

### Exercise 1.1

Unrolling the reccurence: $T(n)<= 2T(n/4) + c\sqrt{(n)}$

Level 0: ${c\sqrt{(n)}}$

Level 1: ${c\sqrt{(n)}}\over 2$

Level 2: ${c\sqrt{(n)}}\over 4$

Level k: ${c\sqrt{(n)}}\over 2^k$

<i>Identifying a pattern: </i> At level j of the recursion, the number of subproblems has doubled j times, so there are now a total of $2^j$. Each has correspondingly shrunk in size by a factor of two j times, and so each has  ${c\sqrt{(n)}}\over 2^k$.

<i>Summing over all levels of recusion: </i> The number of times the input must be halved in order to reduce its size from n to 2 is $log_2n$. So summing the ${c\sqrt{(n)}}$ work over $logn$ levels of recursion, the total running time will be $O(n*logn)$