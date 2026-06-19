class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        summ=0
        max_n=0
        arr=[]
        for i in range(len(gain)):
            summ+=gain[i]
            arr.append(summ)
        max_n=max(arr)
        if max_n>0:
            return max_n
        else:
            return 0

        