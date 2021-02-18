class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        sub_slices = [A[i] - A[i-1] for i in range(1, len(A))]
        ans = 0
        
        prev_val = sub_slices[0]
        count, succ_counts = 1, []
        for sub_val in sub_slices[1:]:
            if prev_val == sub_val:
                count += 1
            else:
                succ_counts.append(count)
                count = 1
                prev_val = sub_val
        succ_counts.append(count)
        print(sub_slices)
        print(succ_counts)
        
        for count in succ_counts:
            if count >= 2:
                ans += count * (count - 1) // 2
        return ans
                    
                
            