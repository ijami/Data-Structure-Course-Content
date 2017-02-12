import math
import random


def counting_sort(A):
    m = max(A)
    Count = [0] * (m + 1)  # The count of each item in A
    for x in A:
        Count[x] += 1
    ans = []
    for i in range(m + 1):
        ans += [i] * Count[i]
    return ans


# Insertion Sort
def insertion_sort(A):
    ans = []
    for k in range(len(A)):  # Insert all elements 2 to n
        item = A[k]  # The k'th element to be inserted
        i = k  # i will hold the position of insertion
        ans += [0]
        while i > 0 and ans[i - 1] > item:
            ans[i] = ans[i - 1]  # Shift to right
            i -= 1
        ans[i] = item  # Insertion
    return ans


def bubble_sort(A):
    ans = list(A)
    n = len(ans)
    bubble_found = False
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if ans[j] < ans[j - 1]:
                ans[j], ans[j - 1] = ans[j - 1], ans[j]  # Swap a bubble
                bubble_found = True
        if not bubble_found:  # Stopping when array is sorted
            break
    return ans


# Selection Sort [Ali]
def selection_sort(A):
    ans = list(A)
    n = len(ans)
    for i in range(n - 1):
        index = i  # The index of min remaining item
        for j in range(i + 1, n):
            if ans[index] > ans[j]:  # Finding min remaining item
                index = j
        ans[i], ans[index] = ans[index], ans[i]  # Swap
    return ans


def get_bucket(x, r):
    return x // r


def bucket_sort(A):
    if len(A) <= 1:
        return
    max_num = max(A)
    r = 1
    while (r * 10 <= max_num):
        r = r*10  # using r will divide numbers based on their most valuable digit     
    bucket_num = 10
    buckets = [[] for i in range(bucket_num)]

    for x in A:
        buckets[get_bucket(x, r)] += [x]
    for i in range(bucket_num):
        buckets[i] = insertion_sort(buckets[i])
    ans = []
    for i in range(bucket_num):
        ans += buckets[i]
    return ans


def radix_sort(A):
    ans = list(A)
    max_num = max(ans)
    radix = 1            # Start to sort based on rightmost digit
    while radix <= max_num:
        B = [[] for i in range(10)]    # 10 buckets for 10 digits
        for i in ans:                # Move each number to a bucket
            B[(i/radix)%10] += [i]
        ans = []                                   # Clear the list
        for i in range(10):
            ans += B[i]                            # Append buckets
        radix *= 10
    return ans


def optimized_radix_sort(A):
    ans = list(A)
    if len(ans) <= 1:
        return
    mx = max(ans + [1])
    n = int(math.log(mx, 2))
    n = max(n, 2)
    maxlen = int(math.log(mx, n) + 1)
    for x in range(maxlen):
        bins = [[] for i in range(n)]
        for y in ans:
            bins[(y / n ** x) % n].append(y)
        ans = []
        for section in bins:
            ans.extend(section)
    return ans

# A = tuple(random.randrange(100) for i in range(100))
# print radix_sort(A)
