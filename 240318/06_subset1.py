
class Solution:
    def subsets(self, nums:list[int]) -> list[list[int]]:
        result = []
        def dfs(index, subset=[]):
            result.append(subset) #공집합
            #종료조건
            for i in range(index,len(nums)): #0~2
                new_subset = subset[:] #전체복사
                new_subset.append(nums[i])
                #print(new_subset)
                dfs(i+1,new_subset)
        dfs(0)
        return result
#[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

s =Solution()
print(s.subsets([1,2,3]))

#공집합추가



#[1,2,3]반복
#[1]
#부분집합 = [1]
# 나머지[2,3]반복
#   [2]반복
#   부분집합 = [1,2]
#     부분집합  =[1,2]
#         나머지[3]반복
#         [3]
#         부분집합 = [1,2,3]
#             나머지 [] 반복
#       [3]
#        부분집합 = [1,3]
#         나머지 [] 반복
#[2]
#   부분집합 = [2]
#     나머지 [3] 반복
#         [3]
#         부분집합 = [2,3]
#             나머지 [] 반복
#[3]
#부분집합 = [3]
#   나머지 [] 반복







