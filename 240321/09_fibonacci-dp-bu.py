#다이나믹 프로그래밍 :중복된하위문제+최적부분구조
#이전에 사용햇던 답이 필요하면 재활용하는것
#메모이제이션 : 하향식접근법/배열에기록하여 사용/
#타뷸레이션 : 상향식접근법/
#탑다운방식(메모이제이션) : 재귀 방식 /간결,가독성/필요한값만-메모리증가
    #큰문제를 해결하기위해 작은부분의 문제를 재귀적으로 나누어가며 해결
#바텀 업 방식(타뷸레이션):반복문 /필요없는것도 구함- 메모리사용적음
    # 반복문을 사용하여

#피보나치수열탑다운방식

class Solution:
    def fib(self, n:int) -> int:
        #바텀업방식:반복문을 사용해 작은부분문제를 풀고 그결과를 활용해 큰문제를해결
        #미리값을 구해놓고 결과이용
        #적은메모리사용,빠른속도/필요없는 값까지 계산하는 상황
        tabul = [0, 1]
        if n in tabul:
            return n
        for i in range(2, n+1): #(2,7)
            tabul.append(tabul[i-1] + tabul[i-2])
        return tabul[-1]

s = Solution()
print(s.fib(6))