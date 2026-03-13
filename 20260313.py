# 챕터정리

print ('ABC', 'XYZ')
print ('ABC' ,'XYZ', end='') # 행의 마지막에서 개행하지 않음
print ('ABC' , 'XYZ', sep='') # 구분을 위한 공백을 제거
print()# 개행
print('ABC\n\nXYZ', sep='') # 중간에 두번 개행
print()
s = input('문자열:')
print('당신이 입력한 문자열은 {}입니다.'.format(s))
print('당신은', s, '를 입력했습니다.')
print('당신은'+ s + '를 입력했습니다.')

no = int(input('정수:'))
print ('마지막 자리의 값:', str(no%10),sep='')
print('2진수:', bin(no))
print('8진수:', oct(no))
print('10진수:', str(no))
print('16진수:', hex(no))

PI= 3.141592653589793
print('사각형과 원의 넓이를 구하겠습니다')
width= float(input('사각형의 가로:'))
height= float(input('사각형의 세로:'))
radius= float(input('원의 지름:'))

print('사각형: {}'.format(width*height))
print('원의 넓이: {}'.format(PI*(radius/2)**2))