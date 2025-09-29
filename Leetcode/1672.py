from typing import List

class Solution:
    def maximumWealth(self, accounts):
        return max(sum(customer) for customer in accounts)
