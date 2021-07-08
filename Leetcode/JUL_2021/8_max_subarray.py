def find_length(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    dp_lens = [[0 for _ in range(len2+1)] for  _ in range(len1+1)]
    max_val = 0

    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2)+1):
            if nums1[i-1] == nums2[j-1]:
                dp_lens[i][j] = dp_lens[i-1][j-1] + 1
                max_val = max(max_val, dp_lens[i][j])
            else:
                dp_lens[i][j] = 0

    return max_val


if __name__ == "__main__":
    assert (find_length(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]) == 3)
    assert (find_length( nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]) == 5)
    assert (find_length( nums1 = [0,1,1,1,1], nums2 = [1,0,1,0,1]) == 2)
    print("All test cases passed!")