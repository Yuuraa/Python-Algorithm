N, M, K = map(int, input().split())
input_nums = list(map(int, input().split()))
input_nums.sort(reverse=True)

num_greatest = (M//(K + 1)) * K + M%(K+1)
num_seconds = M - num_greatest
answer = num_greatest*input_nums[0] + num_seconds*input_nums[1]
print(answer)