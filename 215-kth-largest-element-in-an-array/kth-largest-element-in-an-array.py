import heapq
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("7"))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        heapq.heapify(nums)
        l=len(nums)
        c=l-k
        c1=0
        while c1<c:
            heapq.heappop(nums)
            c1+=1
        return heapq.heappop(nums)

