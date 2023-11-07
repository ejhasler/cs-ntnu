# Divide and Conquer - Assignments

<b> 1 Recurrences </b> Use both the recursion tree method and the (partial) substitution method to solve each of the following recurrences.

## Exercise 1

### 1.1

Unrolling the reccurence: $T(n)<= 2T(n/4) + c\sqrt{(n)}$

Level 0: ${c\sqrt{(n)}}$

Level 1: ${c\sqrt{(n)}}\over 2$

Level 2: ${c\sqrt{(n)}}\over 4$

Level k: ${c\sqrt{(n)}}\over 2^k$

<i>Identifying a pattern: </i> At level j of the recursion, the number of subproblems has doubled j times, so there are now a total of $2^j$. Each has correspondingly shrunk in size by a factor of two j times, and so each has  ${c\sqrt{(n)}}\over 2^k$.

<i>Summing over all levels of recusion: </i> The number of times the input must be halved in order to reduce its size from n to 2 is $log_2n$. So summing the ${c\sqrt{(n)}}$ work over $logn$ levels of recursion, the total running time will be $O({n\sqrt{n}})$

### 1.2

Unrolling the reccurence: $T(n)<= 2T(n/4) + cn$

Level 0: $cn$

Level 1: $cn\over 2$

Level 2: $cn\over 4$

Level k: $cn\over 2^k$

### 1.3

Unrolling the reccurence: $T(n)<= 2T(n/4) + cn^2$

Level 0: $cn^2$

Level 1: $cn^2\over 2$

Level 2: $cn^2\over 4$

Level k: $cn^2\over 2^k$

### 1.4

Unrolling the reccurence: $T(n)<= T(3n/4) + cn$

Level 0: $cn$

Level 1: $3cn\over 4$

Level 2: $9cn\over 16$

Level k: $3^kcn\over4^k$

### 1.5

Unrolling the reccurence: $T(n)<= T(n/2) + T(n/3) + T(n/6) + cn$

Level 0: $cn$

Level 1: $cn\over 2$ $+$ $cn\over 3$ $+$ $cn\over 6$

Level 2: $cn\over 4$ $+$ $cn\over 6$ $+$ $cn\over 12$

Level k: $cn\over 2^k$ $+$ $cn\over 3^k$ $+$ $cn\over 6^k$

## Exercise 2

Let's say A and B are the two databases and $A(i), B(i)$ are i-th smallest elements of A, B. First, let us compare the medians of the two databases. Let $k$ be $[$ $1\over 2 $ $n$ $]$, then $A(k)$ and $B(k)$ are the medians of the two databases. Suppose $A(k) < B(k)$ (the case when $A(k) > B(k)$ would be the same with interchange of the role of A and B). Then one can see that $ B(k) $ is greater than the first $ k $ elements of A. Also $ B(k) $ is always greater than the first $ k - 1 $ elements of B. Therefore $B(k)$ is at least 2k-th elemnt in the combine databases. Since $2k >= n$, all elements that are greater than $B(k)$ are greater than the median and we can eliminate the second part of the B database. Let $B'$ be the half of $B$.

Similarly, the first $[$ $1\over 2 $ $n$ $]$ elements of A are less than $B(k)$, and thus, are less then the last $n-k+1$ elements of B Also they are less then the last $[$ $1\over 2 $ $n$ $]$ elements of A. So, they are less than at least $n-k+1+$ $[$ $1\over 2 $ $n$ $]$ $- n +1$ elements of the combine database. It means that they are less than the median and we can eliminate them as well. Let $A'$ be the remaining parts of A.

Now we eliminate $[$ $1\over 2 $ $n$ $]$ elements that are less than the median, and the same number of elements that are greater than median. It is clear that the median of the remaining elements is the same as the median of the original set of element. We can find a median in the remaining set using recursion for $A'$ and $B'$. Note that we can't delete elements from the databases. However, we can access i-th smallest elements of $B'$ is i-th smallest elements of B.

Formally, the algorithm is the following We write recursive function medain (n, a, b) that takes integers n, a and b and find the median of the union of the two segments $A[a+1;a+n]$ and $B[b+1;b+n]$.

```
median(n, a, b)
    if n=1 then return min (A(a+k), B(b+k)) // base case
    k=[(1/2)*n]
    if A(a+k)<B(b+k)
        then return median (k, a + [(1/2)*n], b)
        else return median (k, a, b + [(1/2)*n])
```

