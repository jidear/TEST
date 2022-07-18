'''
x = int(input("첫번째 정수를 입력하시요: "))
y = int(input("첫번째 정수를 입력하시요: "))
sum = (x+y)
print("첫번째 숫자와", x, " 두번째 숫자", y," 합은", sum," 입니다.")
'''

# tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

"""
eng = 90
math = 70
kor = 80
sum = eng+math+kor
print("총 점수 = ", sum)
print("평균 점수 = ", sum/3)
"""

"""
person = {"name" : "hong kil dong", "height" : 185, "weight" : 80, "phone" : "010-1234-5678"}
for key, value in person.items():
    print(f"{key}: {value}")
"""

'''
a = 100
result = 0
for i in range(1,3):
   result = a >> i
   #print(result)
   result = result + 1
   #print(result)
print(result)
'''
# PYTHON_WIN10
'''
a = 123	# 변수 치환(‘=’를 기준으로 좌항은 ‘변수’, 우항은 ‘값’)
b = -123
print(a,b)          # 내용 출력
print(a+b)          # 연산
c, d = 456, -456    # 변수는 '='를 기준으로 좌우항의 개수가 동일하면 된다.
print(c + d)        # 띄어쓰기 무관

e, f = 1.2, 3.4     # 실수형은 소수점만 있으면 된다.
g, h, i = 0b1011, 0o177, 0xABC      # 2진수, 8진수, 16진수

j, k = 123, 27
print(j + k)        # 더하기
print(j - k)        # 빼기
print(j * k)        # 곱하기
print(j / k)        # 나누기
print(j // k)       # 몫
print(j % k)        # 나머지
'''

'''
a = "Hello Samadal"         # 문자열 유형은 4개 모두 사용 가능
a = 'Hello Samadal'
a = """Hello Samadal"""
a = ' ''Hello Samadal' ''

b = "Kg It Bank"            # 변수 치환
print("Kg It Bank")
print(b)
# 이스케이프 코드(Escape Code) - 반드시 문자열 안에서만 동작한다.

print('1다음 라인으로\이동')        # 그냥 문자열
print('2다음 라인으로\n이동')       # 줄바꿈(엔터)
print('3다음 라인으로\r이동')       # 교체
print(123456781234567812345678)
print('4다음 라인으로\t이동')       # 탭(8문자, 8칸)
print('5다음 라인으로\'이동')       # 기호(') 삽입
print('6다음 라인으로\"이동')       # 기호(") 삽입
print('7다음 라인으로\\이동')       # 기호(\) 삽입
'''

'''
a = "KgItBank, Samadal"
print(a)
print(a[0])     # 앞에서 인덱싱할 때는 '0'부터
print(a[1])
print(a[-1])    # 뒤에서 인덱싱할 때는 '-1'부터
print(a[-2])
b = a[7]
print(b)

print('SAM', 'samadal', sep=' = ')  # 문자열 출력 구분
print('S', 'A', 'M', sep=' = ')
print(10, 20, 30, sep='% ', end='%')    # 마지막 문자 삽입

print('C:\\Program Files\\Python310\\')
print('C:', 'Program Files', 'Python310', sep='\\', end='\\\n')
print('C:', 'Program Files', 'Python310', sep='\\''\\', end='\\''\\')
print('\nC:\\', 'Program Files\\', 'Python\\', sep='\\', end='\\')

a = "KgItBank"
b, c, d = a[1], a[2], a[3]
print(b, c, d)
print(a[1:4])       # 1 <= a < 4
print(a[3:-1])      # 3 <= a < -1
print(a[:])         # 전체 범위
print(a[3:])        # 3 <= a <= 끝
print(a[:3])        # 0 <= a < 3
e = "KgItBank20220718"
company, day = e[0:8], e[8:]
print(company, day)
'''

'''
bin = 0b1101010001110001
bin2 = 1101010001110001
print("%d" % (bin))     # 2진수
print("%d" % (bin2))    # 그냥 숫자(값이 1개일 경우 ()생략가능)
print("{0}" .format(bin))
print("{}" .format(bin))    # 인덱스 넘버 생략 가능
print(f"{bin}")

hexa, dec = 0x3D5F, 1024
print("%d | %x" % (hexa, dec))
print("{}, {:x}" .format(hexa, dec))
print(f"{hexa}, {dec:x}")

a = "KgItBank20220718"
b, c, d, e = a[:8], a[8:12], a[12:14], a[14:]
# print("%d | %d | %d | %d" % (b,c,d,e))    # 주어진 a가 문자열이기 때문에
print("%s | %s | %s | %s" % (b,c,d,e))      # 출력도 문자열로 해야 됨
print(type(b), type(c), type(d), type(e))   # 문자열 유형 확인
print("{0} | {1} | {2} | {3}" .format(b,c,d,e))
print(f"{b} | {c} | {d} | {e}")

a, b, c = 85.5, 79.3, 95.4      # 국어, 영어, 수학 점수
sum = a + b + c
avg = sum / 3
print("합계(%d) | 평균(%d)" % (sum, avg))   # 서식지정자에 문제가 있다.
print("합계(%.1f) | 평균(%.1f)" % (sum, avg))
print("합계({0:.1f}) | 평균({1:.1f})" .format(sum, avg))
print(f"합계({sum:.1f}) | 평균({avg:.1f})")


var1 = input("국어 : ")
var2 = input("영어 : ")
var3 = input("수학 : ")
print(var1, var2, var3)
print(var1 + var2 + var3)
print(type(var1))
print(int(var1) + int(var2) + int(var3))    # 강제 형 변환(Cast 연산)을 이용해서 유형 변경
a, b, c = int(var1), int(var2), int(var3)
d = a + b + c
print("%d + %d + %d = %d" % (a, b, c, d))
var4 = int(input("국어 : "))
var5 = int(input("영어 : "))
var6 = int(input("수학 : "))
print(var4+var5+var6)
'''

'''
print(7 % 3)
print(7 ** 3)
samadal = 1
if samadal == 1: print("True")
else: print("False")
if samadal != 1: print("False")
else: print("True")

a = 0
a = a + 3
print(a)
a += 4      # a = a + 4
print(a)

x, y = True, False
if x and y: print("OK")     # 둘 다 동일하다면...
else: print("Fail")
'''

'''
x, y = 15, 10
if x > y:
   print("%d는 %d보다 크다" % (x, y))

z = 25  # 매개 변수
if z in (10, 15, 25):  # 인수
   print("주어진 값과 비교값 {}는 동일하다".format(z))

x = 15
if x > 10 and x != 15:
   print("Samadal")
else:
   print("Madal")
y = 15
if y > 10 or x != 15:
   print("samadal")
else:
   print("Madal")

x, y, asmd = int(input("값1 : ")), int(input("값2 : ")), (input("값3 : "))
asmd_list = ['+', '-', '*', '/']
if asmd == '+' in asmd_list: tmp = x + y
if asmd == '-' in asmd_list: tmp = x - y
if asmd == '*' in asmd_list: tmp = x * y
if asmd == '/' in asmd_list: tmp = x / y

print("%d %s %d = %d" % (x, asmd, y, tmp))

# if asmd == '+' in asmd_list: print("%d + %d = %d" % (x, y, x+y))
# if asmd == '-' in asmd_list: print("%d + %d = %d" % (x, y, x-y))
# if asmd == '*' in asmd_list: print("%d + %d = %d" % (x, y, x*y))
# if asmd == '/' in asmd_list: print("%d + %d = %d" % (x, y, x/y))


x, y, z = int(input("값1 : ")), int(input("값2 : ")), int(input("값3 : "))
if x > y and x > z: max = x
elif y > x and y > z: max = y
elif z > x and z > y: max = z
# 마지막 줄에 있는 'elif'를 'else'로 변경하면 오류가 발생한다.
# 'elif'는 'if'가 있기 때문에 조건문이 반드시 와야하고 'else'는 없기 때문에 오면 안된다. 
if x < y and x < z: min = x
elif y < x and y < z: min = y
elif z < x and z < y: min = z
print("최대값 : %d | 최소값 : %d" % (max, min))


year = int(input("년도 : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: print("%d는 윤년입니다." % year)
        else: print("%d는 평년입니다." % year)
    else: print("%d는 윤년입니다." % year)
else: print("%d는 평년입니다." % year)


year = int(input("년도 : "))
if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         yr = "윤년"
      else:
         yr = "평년"
   else:
      yr = "윤년"
else:
   yr = "평년"
print("%d는 %s입니다." % (year, yr))
'''

'''
a = 1104                        # 쓸모없는 변수
for a in range(1, 11, 1):       # 1부터 10(11-1)까지 숫자 출력
    # print("a = %d" % a)
    if a % 2 == 0: print("a = %d" % a)



sum = 0     # 합산, 누적 등과 같은 경우 반드시 초기값에 반드시 '0'으로 초기화해야 한다.
for a in range(1, 101):
    print("%d + %d = %d" % (sum, a, sum+a))
    sum += a   
print("100까지의 합 : %d" % sum)



a = [95, 25, 67, 45, 80]        # 문자열 리스트
count = 0
for i in range(5):              # x, 끝값, x
    count += 1                  # 초기값이 생략한 경우에는 '0'부터 부여
    b = a[i]
    if b >= 60: print("%d번째 학생은 %d점이므로 합격입니다." % (count, b))
    else: print("%d번째 학생은 %d점이므로 불합격입니다." % (count, b))


a = int(input("원하는 단 : "))
for i in range(a, a+1):
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i*j))
    print()
'''

'''
a = 0
sum = 0
while a < 10:       # a가 10보다 작으면 무한반복해라.
    a += 1
    sum += a
    print("%d => %d" % (a, sum))        # 1부터 10까지의 숫자들의 합
print("합 : %d" % sum)


coffee = 10
while True:         # 하단의 내용이 모두 참일 때까지 무한 반복
    money = int(input("돈을 넣어 주세요 : "))
    if money == 300:        # 커피 한잔 가격(300원)
        print("한 잔의 커피를 줍니다.")
        coffee -= 1
        print("남은 커피 수량은 %d잔입니다." % coffee)
    elif money > 300:       # 거스름돈이 필요
        print("한 잔의 커피를 주고 거스름돈 %d원을 줍니다." % (money-300))
        coffee -= 1
        print("남은 커피 수량은 {}잔입니다." .format(coffee))
    else:
        print("입력받은 돈은 %d원이므로 커피를 안 주고 돈을 돌려줍니다." % money)
        print(f"남은 커피 수량은 {coffee}잔입니다.")
    if not coffee:
        print("오늘 준비된 10잔이 커피가 모두 소진되었습니다.")
        break
'''

'''
x, y = 4, 2
def add(a, b):
    ab = a + b
    print(ab)
def sub(a, b):
    ab = a - b
    return ab
def mul(a, b):
    ab = a * b
    return ab
def div(a, b):
    ab = a / b
    return ab
add(x, y)       # 호출부
print(sub(x, y))
print(mul(x, y))
print(div(x, y))



# 윤년을 함수식으로 표현(이중함수)



year = int(input("년도 : "))
def y(i):
    if (i % 4 == 0):
        if (i % 100 == 0):
            yy(i)
        else: print("윤년")
    else: print("평년")
def yy(j):
    if j % 400 == 0: print("윤년")
    else: print("평년")
y(year)



# 1부터 임의의 값까지 입력받았을 때의 출력과 합계를 구하는 소스



num = int(input("값 : "))
def sum1(x):
    sum2(x)
def sum2(y):
    sum = 0
    for i in range(1, y+1):
        sum += i
        print("i = %d" % sum)
    return sum
sum1(num)
print("합계 : %d" % sum2(num))



def cm1():
    coffee = 3
    while True:
        money = int(input("돈을 넣어주세요 : "))
        cm2(money, coffee)
        coffee -= 1
        if not coffee:
            print("커피를 모두 소진해 판매를 종료합니다.")
            break
def cm2(money, coffee):
    if money == 300:
        print("커피 한 잔 제공")
        coffee = coffee - 1
        print("남은 수량 : %d" % coffee)
    elif money > 300:
        print("커피 한 잔 제공하고 거스름돈 %d원 반환" % (money-300))
        coffee -= 1
        print("남은 수량 : %d" % coffee)
    elif money < 300:
        print("커피 가격(300원)보다 낮은 %d원을 투입해서 돈을 반환함" % money)
        print("남은 수량 : %d" % coffee)
cm1()
'''


'''
class _AB:
    def __init__(self):
        self.result = 0
    def add(self, a, b):
        self.a = a
        self.b = b
        self.rt = self.a + self.b
        return self.rt
cla = _AB()          # '객체(변수) = 값' 형태로 생각하면 된다.
                    # 클래스의 모든 내용에 대한 접근 권한을 cla라는 객체에 위임하겠다.
                    # 인스턴스(객체(cla)가 어떤 클래스(AB)의 객체인지를 표현)
print(cla.add(4, 3))



class _H:
    def a(self, hx):
        self.hx = hex
    def b(self):
        return self.hx
h = _H()
hexa = 0x3D5F
h.a(hexa)
print("%d" % h.b())



d = a + b + c
e = d / 3
print("국어(%d) | 영어(%d) | 수학(%d)" % (a, b, c))



class _SUM:
    def sum1(self, x, y, z):        # self인자를 이용한 변수 재지정
        self.x = x                  # 클래스 안에 있는 메서드들은 그냥 사용한다.
        self.y = y
        self.z = z
    def sum2(self):
        return self.x + self.y + self.z
class _AVG:
    def avg1(self, xyz):
        self.xyz = xyz
    def avg2(self):
        return self.xyz / 3

sS = _SUM()
aA = _AVG()
a, b, c = 85.5, 79.3, 95.4

sS.sum1(a, b, c)        # 메서드에 초기값을 대입
it1 = sS.sum2()         # 반환된 결과값을 변수에 저장
aA.avg1(it1)
it2 = aA.avg2()
# 주어진 값이 실수이므로 서식지정자 'f'를 사용한다.
print("국어(%.1f) | 영어(%.1f) | 수학(%.1f) | 합(%.1f) | 평균(%.1f)" % (a, b, c, it1, it2))



class _FourCal:     # 한 개의 클래스 안에 모든 내용 삽입
    def madal(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
fc = _FourCal()
fc.madal(4, 2)
a = fc.add()
print(a)
print(fc.sub())
print(fc.mul())
print(fc.div())


class _FourCal2:     # 한 개의 클래스 안에 모든 내용 삽입
    def __init__(self):
        self.result = 0
    def add(self, first, second):
        self.first = first
        self.second = second
        return self.first + self.second
    def sub(self, first, second):       # 2. 초기값을 지정할 필요가 없다.
        return first - second           # 3.연산식에서도 'self'를 빼도 된다.
    def mul(self, first, second):
        return first * second
    def div(self, first, second):
        return first / second
a, b = 7, 3
fc = _FourCal2()
print(fc.add(a, b))     # 1. 값을 메서드 안에 직접 삽입할 경우에는
print(fc.sub(a, b))
print(fc.mul(a, b))
print(fc.div(a, b))
'''

# * 숙제
#   - 위에서 작업한 클래스를 모두 분리, 즉 4개의 클래스로 코딩
#   - 사용자 입력 함수를 이용해서 3개의 정수값을 입력 받고 비교한 후 가장 큰 값과 가장 작은 값만을 출력
#   - 받아들인 3개의 값(기호 1개, 숫자 2개)에 따라 사칙연산하는 계산기
#   - 구구단 전체(2단 ~ 9단)를 출력

# print("!!")
# x = int(input())