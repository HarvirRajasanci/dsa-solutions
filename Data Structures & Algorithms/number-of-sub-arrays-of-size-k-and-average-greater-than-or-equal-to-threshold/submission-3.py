class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = curr_sum = subarrays = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                curr_sum -= arr[L]
                L += 1
            curr_sum += arr[R]
            if R - L + 1 == k and (curr_sum / k) >= threshold:
                subarrays += 1
        return subarrays