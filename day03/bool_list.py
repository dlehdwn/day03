

a = 1
b = 3.14
c = '메가스터디'
d = True # bool
e = False # bool
# bool()

#대부분 값을 True
#비어있는 값, 0 이면 False
boolA = bool(a)
print(boolA)

boolB = bool(0)
print(boolB)

# list type
coffee = ['아아','카페라떼','바닐라라떼']
print(coffee[1]) # [index]

bus_n = [10,171,271.273]

# 리스트 안에는 아무 타입이나 가능
mega = [[1,3,5],[5,6,7],[1,5,9]]
print(f"c언어 마지막 강의 날짜:{mega[2][2]}")

# list() # 리스트화
# nlist = list(1,2,3,4,5,6,) # 정수를 리스트화
mega = list("megastudy")
print(mega)
