---


---

<h3 id="description">Description:</h3>
<p>Given a positive number n &gt; 1 find the prime factor decomposition of n. The result will be a string with the following form :</p>
<pre><code> "(p1**n1)(p2**n2)...(pk**nk)"

</code></pre>
<p>with the p(i) in increasing order and n(i) empty if n(i) is 1.</p>
<pre><code>Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

</code></pre>
<p>Fundamentals</p>
<p>Mathematics</p>

---

### Explanation of `primeFactors(n)` Solution

The goal of this function is to find the prime factorization of a number `n > 1` and return the result in a specific string format. The string format is `(p1**n1)(p2**n2)...(pk**nk)`, where `p1, p2, ..., pk` are the prime factors in increasing order and `n1, n2, ..., nk` are the exponents of each prime factor. If the exponent is 1, we don't include the `**1` part.

### Approach

1. **Initialization**:
   - We initialize an empty list `factors` to store the prime factors of the number `n`.

2. **Check for divisibility by 2**:
   - Since 2 is the smallest prime number, we start by checking if `n` is divisible by 2. We repeatedly divide `n` by 2 while it’s divisible by 2 and append `2` to the `factors` list.

3. **Check for divisibility by 3**:
   - After handling 2, we check if `n` is divisible by 3, using a similar approach. We repeatedly divide `n` by 3 while it’s divisible by 3 and append `3` to the `factors` list.

4. **Check for divisibility by numbers in the form of 6k ± 1**:
   - The next step is to handle potential prime numbers that are not divisible by 2 or 3. These numbers are of the form `6k ± 1`. We loop through numbers starting from 5 and check if `n` is divisible by either `i` or `i + 2` (i.e., 6k - 1 and 6k + 1). We repeat this process while `i * i <= n`, which ensures we only check up to the square root of `n` for factors.
   - If `n` is divisible by either `i` or `i + 2`, we append these factors to the `factors` list and divide `n` by the factor until it is no longer divisible.
   - If neither of these factors divides `n`, we increment `i` by 6 to check the next pair of potential factors (6k - 1 and 6k + 1).

5. **Check if the remaining `n` is a prime**:
   - If, after the loop, `n` is still greater than 1, it must be a prime number itself. We append this value to the `factors` list.

6. **Count occurrences of each factor**:
   - After obtaining all the factors, we create a dictionary `factor_count` to store how many times each prime factor appears. This is done by iterating over the `factors` list and updating the dictionary.

7. **Format the result string**:
   - We then build the result string by iterating over the keys (prime factors) in `factor_count`, sorted in ascending order.
   - For each factor, if it appears only once, we append the factor as `(p)`. If it appears more than once, we append the factor as `(p**n)`, where `n` is the count of occurrences.
   
8. **Return the formatted result**:
   - Finally, we return the string representing the prime factorization of `n` in the required format.

---

### Example Walkthrough

For the number `n = 86240`:

- First, we handle divisibility by 2: `86240 / 2 = 43120`, `43120 / 2 = 21560`, `21560 / 2 = 10780`, `10780 / 2 = 5390`, and `5390 / 2 = 2695`. So, `2` is a factor, repeated 5 times.
- Then, we check for divisibility by 3: `2695` is not divisible by 3, so we skip this step.
- We then check divisibility by numbers of the form `6k ± 1`. We find that `2695` is divisible by 5, and we continue dividing it by 5 until `n = 539`, which is not divisible by 5 anymore.
- Next, `539` is divisible by 7, so we divide it by 7 twice until `n = 11`.
- Finally, `11` is prime, so we append `11` to the factors list.

The result is `"(2**5)(5)(7**2)(11)"`.

---

### Summary

- The solution efficiently computes the prime factorization of a number by first handling small primes (2 and 3), and then using the 6k ± 1 rule to find larger prime factors.
- It optimizes the factorization by only checking divisibility up to the square root of `n`, reducing unnecessary computations.
- The final result is formatted according to the problem’s requirements, with the prime factors in increasing order and exponents only included if they are greater than 1.

### Big O Notation for `primeFactors(n)`:

Let's break down the time complexity of the `primeFactors(n)` function:

#### 1. **Divisibility by 2**:
   - We first check if `n` is divisible by 2 and repeatedly divide it by 2 as long as it’s divisible. 
   - This operation runs in **O(log n)** time because we are continuously halving the value of `n` until it becomes odd or is no longer divisible by 2.

#### 2. **Divisibility by 3**:
   - Similarly, we check if `n` is divisible by 3 and divide it by 3 as long as it’s divisible.
   - This step also runs in **O(log n)** time because we are repeatedly dividing `n` by 3.

#### 3. **Divisibility by numbers of the form `6k ± 1`**:
   - The loop starts at `i = 5` and checks divisibility by both `i` and `i + 2` (i.e., `6k - 1` and `6k + 1`). The loop increments `i` by 6 in each iteration.
   - We only check divisibility for values of `i` up to the square root of `n`, which means the maximum number of iterations in this loop is approximately **O(√n)**.
   - For each iteration, the operations inside the loop (checking divisibility and updating `n`) take constant time **O(1)**, so the loop contributes **O(√n)** time.

#### 4. **Final Check for Prime `n`**:
   - After the loop, if `n` is still greater than 1, it must be a prime number and we append it to the list of factors.
   - This final check and append operation takes constant time **O(1)**.

#### 5. **Counting Factor Occurrences**:
   - After all factors are found, we create a dictionary `factor_count` to count how many times each factor appears. This takes **O(k)** time, where `k` is the number of unique prime factors found.
   - In the worst case, `k` can be proportional to **O(log n)** because the number of distinct prime factors of `n` is limited by its logarithmic size. (This is not a strict bound but gives a reasonable estimate for typical cases.)

#### 6. **Formatting the Result**:
   - We loop through the `factor_count` dictionary and build the result string. Sorting the keys of the dictionary takes **O(k log k)** time, where `k` is the number of unique prime factors.
   - Formatting the string itself takes **O(k)** time, so this step contributes **O(k log k)** overall.

---

### Overall Time Complexity

Combining all the steps:

- **O(log n)** for divisibility by 2 and 3.
- **O(√n)** for divisibility by numbers of the form `6k ± 1`.
- **O(k log k)** for sorting the prime factors (where `k` is the number of unique prime factors).

Thus, the overall time complexity is dominated by the **O(√n)** step for checking divisibility by numbers up to the square root of `n`, so the overall time complexity is:

**O(√n + k log k)**, where `k` is the number of unique prime factors of `n`.

In typical cases, `k` will be small relative to `n`, so the time complexity can be approximated as **O(√n)**.

---

### Space Complexity

The space complexity of the algorithm is determined by:

- The `factors` list, which stores the prime factors of `n`.
- The `factor_count` dictionary, which stores the count of occurrences of each prime factor.

The number of elements in `factors` will be proportional to the number of prime factors of `n`, which is **O(log n)** in the worst case (i.e., when `n` is a large prime number). The dictionary `factor_count` will also store at most **O(log n)** unique prime factors.

Thus, the space complexity is **O(log n)**.

---

### Summary:

- **Time Complexity**: **O(√n)** in the worst case, dominated by the loop checking for divisibility up to the square root of `n`. The additional steps contribute smaller terms.
- **Space Complexity**: **O(log n)**, due to the storage of prime factors and their counts.

This solution is quite efficient, with the time complexity being proportional to the square root of `n`.



<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

