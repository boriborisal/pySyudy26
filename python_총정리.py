# ============================================================
#  파이썬 문법 총정리 노트 
# ============================================================


# ────────────────────────────────────────
# 1. 자료형 (Data Types)
# ────────────────────────────────────────

# 기본 타입
x     = 10          # int   정수
pi    = 3.14        # float 실수
name  = "클로이"    # str   문자열
flag  = True        # bool  불리언 (True / False)
empty = None        # NoneType

# 타입 확인
print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True

# 타입 변환
print(int("42"))            # 42
print(float("3.14"))        # 3.14
print(str(100))             # "100"
print(bool(0))              # False  ← 0, "", [], None 은 모두 False
print(bool(1))              # True

# 문자열 메서드
s = "Hello World"
print(s.upper())            # "HELLO WORLD"
print(s.lower())            # "hello world"
print(s.split(" "))         # ['Hello', 'World']
print(s.replace("Hello", "Hi"))  # "Hi World"
print(s.strip())            # 양쪽 공백 제거
print(s.startswith("He"))   # True
print(len(s))               # 11
print(s[0:5])               # "Hello"  (슬라이싱)
print(s[::-1])              # "dlroW olleH"  (역순)

# f-string (권장 방식!)
age = 22
print(f"이름: {name}, 나이: {age}살")


# ────────────────────────────────────────
# 2. 연산자 (Operators)
# ────────────────────────────────────────

# 산술
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...  (실수 나눗셈)
print(10 // 3)  # 3         (몫)
print(10 % 3)   # 1         (나머지)
print(2 ** 8)   # 256       (거듭제곱)

# 비교
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(5 <= 3)   # False

# 논리
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# 복합 대입
n = 10
n += 5   # n = 15
n -= 3   # n = 12
n *= 2   # n = 24
n //= 4  # n = 6
n **= 2  # n = 36

# 멤버십 & 동일성
print("a" in "apple")          # True
print(3 not in [1, 2, 4])      # True

a = [1, 2]
b = a
print(a is b)                  # True  (같은 객체)
# ※ == 는 값 비교, is 는 객체 동일성 비교
# ※ None 비교는 항상 is 사용!  →  if x is None:


# ────────────────────────────────────────
# 3. 조건문 (Conditionals)
# ────────────────────────────────────────

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")   # ← 출력됨
elif score >= 70:
    print("C")
else:
    print("D")

# 삼항 연산자 (한 줄 if)
result = "성인" if age >= 18 else "미성년자"
print(result)   # "성인"

# match-case (Python 3.10+)
command = "quit"
match command:
    case "quit":
        print("종료")
    case "start":
        print("시작")
    case _:
        print("모름")   # default


# ────────────────────────────────────────
# 4. 반복문 (Loops)
# ────────────────────────────────────────

# for + range
for i in range(5):
    print(i)            # 0 1 2 3 4

for i in range(0, 10, 2):
    print(i)            # 0 2 4 6 8

# 리스트 순회
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# enumerate: 인덱스도 같이
for i, fruit in enumerate(fruits):
    print(i, fruit)

# zip: 두 리스트 동시에
names = ["클로이", "소은"]
ages  = [22, 21]
for n, a in zip(names, ages):
    print(n, a)

# while
count = 0
while count < 5:
    print(count)
    count += 1

# 무한 루프 + break
while True:
    val = input("입력 (quit으로 종료): ")
    if val == "quit":
        break

# break / continue
for i in range(10):
    if i == 3:
        continue    # 3 건너뜀
    if i == 7:
        break       # 7에서 종료
    print(i)

# 리스트 컴프리헨션  ← 파이썬스러운 문법!
# [표현식 for 변수 in 반복 if 조건]
squares = [x**2 for x in range(5)]         # [0, 1, 4, 9, 16]
evens   = [x for x in range(10) if x%2==0] # [0, 2, 4, 6, 8]
matrix  = [[i*j for j in range(3)] for i in range(3)]  # 2D 리스트


# ────────────────────────────────────────
# 5. 함수 (Functions)
# ────────────────────────────────────────

# 기본 정의
def greet(name):
    return f"안녕, {name}!"

print(greet("클로이"))   # "안녕, 클로이!"

# 기본값 매개변수
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9
print(power(3, 3))  # 27

# 키워드 인자 (순서 달라도 OK)
def info(name, age):
    print(name, age)

info(age=22, name="박소은")

# *args : 여러 위치 인자 → 튜플
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))   # 10

# **kwargs : 여러 키워드 인자 → 딕셔너리
def show(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

show(name="클로이", age=22)

# lambda (익명 함수)
square = lambda x: x ** 2
print(square(5))    # 25

nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda x: -x))  # 내림차순

# 타입 힌트 (강제X, 가독성용)
def add_nums(a: int, b: int) -> int:
    return a + b


# ────────────────────────────────────────
# 6. 자료구조 (Data Structures)
# ────────────────────────────────────────

# ── 리스트 (list) : 순서O, 중복O, 변경O ──
lst = [1, 2, 3]
lst.append(4)           # [1,2,3,4]       끝에 추가
lst.insert(1, 99)       # [1,99,2,3,4]    중간 삽입
lst.remove(99)          # [1,2,3,4]       값으로 삭제
popped = lst.pop()      # 4 반환 & 제거
lst.sort()              # 정렬 (원본 변경)
lst.sort(reverse=True)  # 내림차순
new = sorted(lst)       # 새 리스트 반환
lst.reverse()           # 뒤집기
print(lst.index(2))     # 값의 인덱스
print(2 in lst)         # True
print(lst[1:3])         # 슬라이싱
print(lst[::-1])        # 역순

# ── 딕셔너리 (dict) : key-value, 순서O(3.7+), 변경O ──
d = {"name": "클로이", "age": 22}
print(d["name"])            # "클로이"
print(d.get("x", 0))       # 0  (키 없을 때 기본값)
d["job"] = "developer"     # 추가/수정
del d["age"]               # 삭제
print(d.keys())            # 키 목록
print(d.values())          # 값 목록
print(d.items())           # (k,v) 쌍 목록

# 딕셔너리 컴프리헨션
sq_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, ...}

# ── 튜플 (tuple) : 순서O, 변경X ──
t = (1, 2, 3)
print(t[0])         # 1
print(len(t))       # 3
print(t.count(1))   # 1

# 언패킹
a, b, c = t
a, *rest = t        # a=1, rest=[2,3]

# ── 셋 (set) : 순서X, 중복X ──
s = {1, 2, 3, 2}    # {1, 2, 3}  중복 자동 제거
s.add(4)
s.remove(1)
s.discard(99)       # 없어도 에러 안남

set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)    # 합집합 {1,2,3,4}
print(set_a & set_b)    # 교집합 {2,3}
print(set_a - set_b)    # 차집합 {1}
print(set_a ^ set_b)    # 대칭차집합 {1,4}


# ────────────────────────────────────────
# 7. 클래스 (Class)
# ────────────────────────────────────────

class Person:
    species = "Human"   # 클래스 변수 (모든 인스턴스 공유)

    def __init__(self, name, age):
        self.name = name    # 인스턴스 변수
        self.age  = age

    def greet(self):
        return f"안녕 나는 {self.name}"

    def __str__(self):      # print() 시 출력
        return f"Person({self.name}, {self.age})"

    def __repr__(self):     # 개발자용 문자열
        return f"Person(name={self.name!r}, age={self.age!r})"


p = Person("클로이", 22)
print(p.greet())    # "안녕 나는 클로이"
print(p)            # "Person(클로이, 22)"


# 상속 (Inheritance)
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)     # 부모 __init__ 호출
        self.major = major

    def greet(self):                    # 메서드 오버라이딩
        return f"나는 {self.major}학과 {self.name}"


s = Student("소은", 22, "보건의료정보")
print(s.greet())        # "나는 보건의료정보학과 소은"
print(isinstance(s, Person))    # True  (부모 타입으로도 인식)


# @property / @staticmethod / @classmethod
class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def area(self):             # 메서드를 속성처럼 사용
        return 3.14159 * self._r ** 2

    @area.setter
    def area(self, value):      # 속성 세터
        self._r = (value / 3.14159) ** 0.5

    @staticmethod
    def description():          # self/cls 없음, 유틸 함수용
        return "원을 나타내는 클래스"

    @classmethod
    def unit_circle(cls):       # cls로 클래스 자체를 받음
        return cls(1)


c = Circle(5)
print(c.area)               # 78.53975  (괄호 없이!)
print(Circle.description()) # "원을 나타내는 클래스"


# ────────────────────────────────────────
# 8. 예외 처리 (Exception Handling)
# ────────────────────────────────────────

# try / except / else / finally
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"에러: {e}")
except (TypeError, ValueError):
    print("타입/값 에러")
else:
    print("에러 없을 때만 실행")   # 정상 실행 시
finally:
    print("항상 실행됨")           # 파일 닫기, 연결 해제 등

# raise : 에러 직접 발생
def set_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 해요")
    return age

# 커스텀 예외 클래스
class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError(f"잘못된 나이: {age}")

try:
    check_age(-1)
except AgeError as e:
    print(e)

# 자주 나오는 예외 종류
# ValueError        → int("abc")          변환 실패
# TypeError         → "a" + 1             타입 불일치
# IndexError        → [1,2][5]            인덱스 범위 초과
# KeyError          → d["없는키"]          딕셔너리 키 없음
# AttributeError    → None.upper()        속성/메서드 없음
# ZeroDivisionError → 1 / 0              0으로 나눔
# FileNotFoundError → open("없는파일")    파일 없음
# NameError         → print(없는변수)     변수 미정의


# ────────────────────────────────────────
# 9. 파일 입출력 (File I/O)
# ────────────────────────────────────────

# 쓰기
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")
    f.write("파이썬 파일 입출력\n")

# 읽기
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()      # 전체 읽기
    # lines = f.readlines() # 줄별로 리스트
    # line  = f.readline()  # 한 줄만

# with 사용 이유: 블록 끝나면 자동으로 파일 닫힘 (close 불필요)


# ────────────────────────────────────────
# 10. 모듈 & 패키지 (Modules)
# ────────────────────────────────────────

import math
import random
import os
from datetime import datetime

print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.14159...
print(random.randint(1, 6)) # 주사위 (1~6)
print(os.getcwd())          # 현재 작업 디렉토리
print(datetime.now())       # 현재 날짜/시간


# ────────────────────────────────────────
# 11. 유용한 내장 함수 모음
# ────────────────────────────────────────

nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(nums))            # 8      길이
print(max(nums))            # 9      최댓값
print(min(nums))            # 1      최솟값
print(sum(nums))            # 31     합계
print(sorted(nums))         # 오름차순 새 리스트
print(sorted(nums, reverse=True))  # 내림차순

print(list(range(5)))       # [0,1,2,3,4]
print(list(map(str, nums))) # 각 요소에 함수 적용
print(list(filter(lambda x: x > 3, nums)))  # 조건 필터

# enumerate, zip은 반복문 섹션 참고

print(abs(-5))              # 5      절댓값
print(round(3.567, 2))      # 3.57   반올림
print(divmod(10, 3))        # (3, 1) 몫과 나머지

# any / all
print(any([False, True, False]))    # True  (하나라도 True면)
print(all([True, True, True]))      # True  (모두 True면)
