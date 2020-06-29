import heapq


def word_frequency(words):
    res = {}
    for word in words:
        res[word] = res.get(word, 0) + 1
    return res


def most_common_words(freqs):
    values = list(freqs.values())
    most = max(values)
    words = [key for key, val in freqs.items() if val == most]
    return words, most


def top_k1(nums, k):
    freq = word_frequency(nums)
    freq_heap = []
    for key in freq.keys():
        heapq.heappush(freq_heap, (-freq[key], key))
    topk = []
    for i in range(min(len(freq_heap), k)):
        topk.append(heapq.heappop(freq_heap)[1])
    return topk


def top_k2(nums, k):
    freq = word_frequency(nums)
    freq_heap = []
    for key in freq.keys():
        heapq.heappush(freq_heap, (freq[key], key))
        if len(freq_heap) > k:
            heapq.heappop(freq_heap)
    topk = []
    for i in range(min(len(freq_heap), k)):
        topk.append(heapq.heappop(freq_heap)[1])
    topk.reverse()
    return topk


def is_palindromic(word):
    freq = word_frequency(word)
    odd_count = 0
    for key in freq.keys():
        if freq[key] % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


def nearest_repeat(array):
    word_index = {}
    dist = float("inf")
    for i in range(len(array)):
        if array[i] in word_index:
            dist = min(dist, i - word_index[array[i]])
        word_index[array[i]] = i
    return dist


def longest_contained_range(array):
    unprocessed = set(array)
    max_len = 0
    while unprocessed:
        elem = unprocessed.pop()
        lower = elem - 1
        while lower in unprocessed:
            unprocessed.remove(lower)
            lower -= 1
        upper = elem + 1
        while upper in unprocessed:
            unprocessed.remove(upper)
            upper += 1
        max_len = max(max_len, upper - lower - 1)
    return max_len


if __name__ == "__main__":
    words1 = ["a", "a", "a", "b", "b"]
    histo1 = word_frequency(words1)
    print(histo1)

    m1 = most_common_words(histo1)
    print(m1)