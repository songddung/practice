### 시험대비

# 과목평가

### map 사용법
# ex. map(lambda x : x**2, [1,2,3,4])
# ex. map(______ x : x**2, [1,2,3,4])

### for , while, if 등이 주어지고
# - continue, break, pass 중 빈칸으로 알맞은 것은?

### 문자열 뒤집는 방법
# 슬라이싱 [::-1]
# reverse()

### 재귀함수 정의 : 함수 본문내부에서 자신을 호출하는 함수

### 다음과 같이 언패킹을 했을 때 에러가 발생하지 않는 코드는?

### 삼항연산자 활용법

### 주석 사용법
# 여러줄 '''''' 또는 """"""

### 다음중 False로 평가되는 것은?
# 0


### class변수, 인스턴스 변수, 다음 중 실행결과는?

### 이스케이프 시퀀스



### 정수형과 실수형의 형변환 

### 튜플 생성법 (V)
#   - 길이가 1,0인 튜플 생성법


### 리스트 컴프리헨션 (V)
# [([0] * 10) for i in range(10) ]

### 슬라이싱 결과가 다른 것?

### 다음 중 변수의 값이 다른 하나는?

### 피보나치 수열에서 함수의 횟수는?

### LEGB룰 (스코프)
# L > E > G > B 순서로 탐색
# L : local
# E : enclosed
# G : global
# B : bulit-in





### 인터프리터란?
#   - 고급언어로 작성된 프로그램을 한줄씩 받아들여 번역과 동시에 프로그램을 한줄 단위로 실행


### 다음 중 예외가 발생하는 것은?

### 다음중 형변환이 불가능한 것은?

### 다음중 가변 자료형은? 불변 자료형은?
# 가변
# list, dict, set
# 불변
# str, int, range, tuple...



### 모듈을 불러오는 방법으로 알맞은 것은?
#   - 불러온 모듈을 사용하는 방법으로 알맞은 것은?
#   - alias 지정해서 불러오기(as)


### enumerate 함수 사용법
# list함수로 인덱스와 값을 반환
# for문에서 주로 사용
# for index, value enumerate(list): 형태로 사용


### 0이 5개 있는 리스트를 만드는 방법
# arr = [0]*5

### 다음중 시퀀스 타입은?
# list, set, tuple, str

### 리스트의 메서드는?
# len, append, pop, remove, index 등등

### str의 메서드는?
# upper, lower, count, split, strip 등등

### dict, set, ... 메서드는?
# dict : keys, values, items, clear, pop 등등
# set : add, clear, pop, remove, copy

### try, except, else, finally 동작 순서
# try > except > else > finally


### 예외 처리 시 반드시 구체적인 것(자식 클래스)부터 조사
# 세부적인것 부터 예외처리를 해야 정확하게 어떤 예외가 발생했는지 알기 용이함
# 부모클래스에 가까울수록 정확한 예외를 알기가 어려움


### MRO 다중 상속 시 출력 결과 예측
#   - 자식클래스가 상속받을때의 순서
#   - child(parent1, parent2)의 경우 1번으로 p1, 그다음 p2 순서


### ####### ### 서술형 [20자 이상, 키워드]

### 주어진 단축평가 코드가 실행된 결과를 예측하고, 그 이유를 설명하시오.
### 얉은 복사와 깊은 복사의 차이를 설명
#   - 얉은 복사 : 슬라이싱, copy()
#   - 문제점 : 중첩된 경우 복사를 해도 메모리 주소를 복사하여 원본 데이터를 손상
#   - 깊은 복사 : deepcopy()

### 슬라이싱 할 때 [처음 : 끝 : 스탭]
#   - 방향, inclusive, exclusive, 생략하는 경우 어떻게 되는지(default)
# 시작의 default는 처음, 끝의 default는 끝, 스탭의 default는 정방향인 1
#   [i] 형태로 :를 넣지 않고 사용 시 해당 인덱스의 값 반환
#   - [:]의 형태로 사용시 시작부터 끝까지를 뜻함
# 인자가 1개일 때, [i:] 인자가 시작부분에 있을 경우 원하는 지점부터 끝까지, [:i] 반대로 인자가 끝부분일 경우 처음부터 i번째까지 
# 방향인자에 -1를 넣어주면 역순으로 진행
# -값 사용가능, [2:-2] 2번째 인덱스부터 끝부분의 2개를 제외한 값 반환


### range도 슬라이싱과 같이
# 슬라이싱과 같은 방식

# 월말 평가

### average
### min, max
### dict 내부의 특정한 값을 조건문으로 확인하기
### 문자열의 길이를 반환하는 My_length
### 딕셔너리 내부의 모든 값의 합을 반환하는 함수
### 인원에 대한 정보가 들어있는 리스트 순회하면서 19살 이상인 인원의 수를 세는 
### 가변인자로 파라미터를 받아서 합을 계산하는 calc

### 카이사르 암호화를 하는 함수
#   - 문자열 > 아스키코드 > +n > 암호화문자열 
#   - ''.join([chr(ord(ch)+ 10) for ch in 'Hello'])

### 10진수를 2진수로
### 소수를 판별하는 함수

### 문자열 내에서 숫자만 골라서 모두 더하는 함수
### 리스트 내의 요소와 그 카운트 수를 키-값 형태로 딕셔너리로 만들기
### 2차원 리스트의 가로, 세로 길이 반환
#   - 가로 세로중 긴거 반환

### 딕셔너리를 활용한 장바구니 물건의 총합 계산