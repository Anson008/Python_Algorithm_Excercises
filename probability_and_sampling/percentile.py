buckets = [0 for i in range(4101)]
for url in urls:
    buckets[len(url)] += 1

num = 0.95 * 100000
total_so_far = 0
for i in range(4100):
    total_so_far += bucket[i]
    if total_so_far >= num:
        print(i)
        break