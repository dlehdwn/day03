# 산술 연산자 (결과 : 숫자)

# 100 미만의 정수를 입력받고, 10의 자리, 1의 자리 출력
# n = int(input("100미만의 정수를 입력하시오:"))
# print(f"십의 자리는 {n//10}이고, 일의 자리는 {n%10}입니다")

# 1000이하 정수를 입력받고, 분과 시로 환산
# n = float(input("1000이하의 정수를 입력하세요:"))
# m = int(n//60)
# s = int(n%60)
# print(f"{m}분 {s}초")

# 정수 10000 ~ 99999 사이 입력, 100의 자릿 값 출력
n = int(input("정수를 입력하세요:"))
n1 = (n//100)%10
print(f"{n1}")


#비교연산자 (결과 : bool)  # print(3<5)
# >,<,>=,<=,==(같다),!=(다르다)
a = 3 >= 2 # bool type
b = 3 == 1 # bool type (False)
c = 3 != 1 # bool type (True)

# 논리 연산자 (결과 : bool)
# and : 피연산자가 모두 True이면 True
print(3>1 and 5>1) # True
# or : 피연산자가 하나라도 True이면 True
print(3>1 or 5>1 or 4>7) # True
# not : False --> True,  True --> False
print(not(3>1)) # False

#할당 연산자
a = 1
a = 3 # a얼마?? 3 # 3으로 갈아치우기

b = 1
b = b+3 # 3을 더해주기
b += 3 # 3을 더해주기
b -= 3 # 3을 빼주기
b *= 3 # 3을 곱해주기
b /= 3 # 3을 나눠주기
