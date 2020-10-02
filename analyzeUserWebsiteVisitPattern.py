
"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.
"""


class Solution:
       def mostVisitedPattern(self, username, timestamp, website):
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)
        cnt = Counter()
        for x in by_user.values():
            cnt += Counter(set(combinations(x, 3)))
        return sorted(cnt, key=lambda k: (-cnt[k], k))[0]