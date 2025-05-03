import random
import bisect

class Solution:

    def __init__(self, weights):
        self.cumulative_weights = []
        
        total = 0
        for weight in weights:
            total += weight
            self.cumulative_weights.append(total)
        self.total_sum = total
        
    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.cumulative_weights, target)

weights = [
    1,
    2,
    3,
    4
]
obj = Solution(weights)
result = obj.pickIndex()
print(f'Result: {result}')