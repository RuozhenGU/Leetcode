
"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
"""




def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        candidates = count.keys()
        ans = sorted(candidates, key = lambda w: (-count[w], w))
        return ans[:k]


import heapq
# use pq
def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()] # (-freq, word) is a tuple and sorting in tuple looks at the first element first and then at the second element. Assuming all words are lowercase
        heapq.heapify(heap) # O(n)
        return [heapq.heappop(heap)[1] for _ in xrange(k)] # heapq.heappop(head) is O(logn)