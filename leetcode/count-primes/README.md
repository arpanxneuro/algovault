# count primes

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: math, sieve, number-theory

---

## 📝 Problem Statement

Given an integer `n`, return the **number of prime numbers** that are **strictly less than** `n`.  
A prime number is an integer greater than 1 with no positive divisors other than 1 and itself. :contentReference[oaicite:1]{index=1}

---

## 📥 Input

```
n = 10
```

---

## 📤 Output

```
4
```

## ✔️ Constraints

- `0 <= n <= 5 * 10^6` — prime counting range. :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:

```
n = 0
```

**Output**:

```
0
```

**Explanation**: There are no prime numbers less than 0. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input    | Output |
| --- | -------- | ------ |
| 1   | `n = 10` | `4`    |
| 2   | `n = 0`  | `0`    |
| 3   | `n = 1`  | `0`    |

---

## 🛠️ Approach

To count primes efficiently under the constraint `0 <= n <= 5 * 10^6`, the **Sieve of Eratosthenes** is the optimal strategy:

1. Create a boolean array `is_prime` of size `n` initialized to `true` for all entries ≥ 2.
2. Mark indices 0 and 1 as non-prime.
3. For each integer `i` from `2` up to `sqrt(n)`, if `is_prime[i]` is true, then mark all multiples of `i` (starting at `i*i`) as non-prime.
4. After sieving, the count of prime numbers is the number of `true` values remaining in `is_prime` from index `2` to `n−1`. :contentReference[oaicite:4]{index=4}

This algorithm runs in **O(n log log n)** time with **O(n)** extra space and is significantly faster than naive checking. :contentReference[oaicite:5]{index=5}

### Time and Space Complexity

- **Time Complexity**: O(n log log n)
- **Space Complexity**: O(n)
