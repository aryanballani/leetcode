from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = defaultdict(int)

        for word in words:
            freq_dict[word] += 1
        
        freq_list = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
        print(freq_list)
        result = []
        for i in range(k):
            result.append(freq_list[i][0])

        return result
