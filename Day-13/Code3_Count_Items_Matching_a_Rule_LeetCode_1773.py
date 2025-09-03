class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_map = {"type": 0, "color": 1, "name": 2}
        idx = key_map[ruleKey]
        
        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1
        return count
