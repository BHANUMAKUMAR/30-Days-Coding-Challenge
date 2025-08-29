class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1,s2):
            """if s1+s2>s2+s1:
                return -1
            if s1+s2<s2+s1:
                return 1
            return 0
        nums=map(str,nums)
        nums=sorted(nums,key=cmp_to_key(compare))
        return "0" if nums[0]=="0" else "".join(nums)"""

        nums=list(map(str,nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        result=''.join(nums)
        return str(int(result))

        
