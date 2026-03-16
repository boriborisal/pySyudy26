# 문자열 인덱싱
letters = 'python'
print (letters[0], letters[2])


# 리스트

python_score = [57,86,63, 92, 35, 79]
a = 1
for i in python_score :
    if i >= 80 :
        grade = "A"
    elif i >= 60 :
        grade = "B"
    else  :
        grade = "C"
    print(f"{a}번은 {i}점 이며, {grade}등급 입니다.")
    a += 1

 # ============================================================
#  Python 기초 함수 & 문법 정리
# ============================================================


# ──────────────────────────────────────────────
# 1. 문자열 메서드
# ──────────────────────────────────────────────

# split() : 구분자를 기준으로 문자열을 분할하여 리스트 반환
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
# → ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


# ──────────────────────────────────────────────
# 2. 반복문
# ──────────────────────────────────────────────

# for loop : 시퀀스(리스트, 튜플, 문자열 등)를 순서대로 반복
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# → apple / banana / cherry


# while loop : 조건이 참인 동안 반복 실행
i = 1
while i < 6:
    print(i)
    i += 1
# → 1 2 3 4 5


# ──────────────────────────────────────────────
# 3. 함수 정의
# ──────────────────────────────────────────────

# def : 함수 정의
def greet(name):
    print("Hello, " + name + "!")

greet("Chloe")
# → Hello, Chloe!


# return : 함수에서 값을 반환
# ※ 아래 예시는 square가 아니라 x + 2 를 반환하는 함수임 (원본 그대로 유지)
def square(x):
    return x + 2

print(square(3))
# → 5


# ──────────────────────────────────────────────
# 4. 예외 처리
# ──────────────────────────────────────────────

# try-except : 예외 발생 시 처리
try:
    x = 5 / 0
except ZeroDivisionError:
    print("division by zero")
# → division by zero


# ──────────────────────────────────────────────
# 5. lambda / map / filter
# ──────────────────────────────────────────────

# lambda : 이름 없는 간단한 함수 정의
square = lambda x: x ** 2
print(square(4))
# → 16


# map() : 함수를 시퀀스의 모든 항목에 적용
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))
# → [1, 4, 9, 16, 25]


# filter() : 조건을 만족하는 항목만 걸러냄
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))
# → [2, 4]


# ──────────────────────────────────────────────
# 6. 내장 함수 (Built-in Functions)
# ──────────────────────────────────────────────

# len() : 길이 반환
print(len("Hello, World!"))   # → 13

# type() : 자료형 반환
print(type(3.14))             # → <class 'float'>

# str() : 문자열 변환
print(str(123))               # → '123'

# int() : 정수형 변환
print(int('123'))             # → 123

# float() : 실수형 변환
print(float('3.14'))          # → 3.14

# list() : 리스트 변환
print(list("abc"))            # → ['a', 'b', 'c']

# range() : 정수 범위 생성  (0 이상 n 미만)
print(list(range(5)))         # → [0, 1, 2, 3, 4]

# enumerate() : 인덱스 + 값을 튜플로 반환
print(list(enumerate(['a', 'b', 'c'])))
# → [(0, 'a'), (1, 'b'), (2, 'c')]

# id() : 객체의 고유 식별 번호 반환
x = [1, 2, 3]
print(id(x))                  # → (실행 환경마다 다름)

# round(a, b) : 실수 a를 소수점 b자리에서 반올림
pi = 3.14159
print(round(pi, 2))           # → 3.14


# ──────────────────────────────────────────────
# 7. 리스트 메서드
# ──────────────────────────────────────────────

# pop(index) : 지정 인덱스 요소 제거 후 반환
fruits = ['apple', 'banana', 'orange']
fruits.pop(0)
print(fruits)                 # → ['banana', 'orange']


# sort() : 리스트를 오름차순 정렬 (in-place)
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)                # → [1, 1, 2, 3, 4, 5, 9]

# sorted() : 원본을 변경하지 않고 정렬된 새 리스트 반환
#            빈 리스트처럼 나중에 채워질 경우 유용
prime_numbers = [7, 3, 5, 2, 11]
print(sorted(prime_numbers))  # → [2, 3, 5, 7, 11]


# append() : 리스트 끝에 요소 1개 추가
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)                # → [1, 2, 3, 4]


# extend() : 다른 리스트의 모든 요소를 한 번에 추가
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)                # → [1, 2, 3, 4, 5]
