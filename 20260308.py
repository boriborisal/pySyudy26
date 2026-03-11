a= int(input('정수 A:'))
b= int(input('정수 B:'))

if a > b:
    a, b= b, a
print('A와 B를 오름차순으로 출력합니다.')
print('A:', a)
print('B:', b) 

