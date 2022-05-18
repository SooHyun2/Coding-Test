## 큰수의 법칙 ##

n,m,k = map(int,input().split()) # 배열의 크기 N, 숫자가 더해지는 횟수 M 그리고 k 횟수
data = list(map(int,input().split()))

# 가장 큰 수 두개를 찾아야 한다.

data.sort(reverse=True)

first_n = data[0]
second_n = data[1]

# print(first_n,second_n)
result = 0
plus_number = 0

for i in range(m):
  