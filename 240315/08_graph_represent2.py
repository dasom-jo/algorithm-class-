#비선형자료구조: 데이터요소가 순차적으로 배열되있지않은상태
#DFS 깊이우선탐색 /정답이 몇가지인가하는 문제에 적합/재귀/스택으로구현
#BFS 너비우선탐색/큐를이용해구현/최단경로를 찾는문제에 적합

graph ={
    1 : [2,3,4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6,7],
    6 : [],
    7 : [3],
}

import sys
node = int(sys.stdin.readline())
print(graph[node])