# Unit 10 리스트와 튜플 사용하기 ===============
** 가나다라마바사

list('Hello')
tuple('Hello')

x, y, z = 1,2,3

# 리스트 언팩킹
x = [1,2,3]
a,b,c=x

# 튜플 언팩킹
y=4,5,6
d,e,f=y

# list로 반납한다.
input().split()

# tuple로 만들어진다.
tuple([10,20,30])


# Unit 11 시퀀스 자료형 활용하기. =================

# list --------------------------------
a = list(range(0,100,10))
30 in a, 100 in a, 100 not in a
list(range(0,10)) + list(range(0,10))
a + [100,200,300]
a*2
len(a)


# tuple --------------------------------
b = tuple(range(0,100,10))
30 in b, 100 in b, 100 not in b
tuple(range(0,10)) + tuple(range(0,10))
b + (100,200,300)
b*2
len(b)


# 문자열 -------------------------------
'he' in 'hello'
'Hello'+' '+'World'
'hello' + str(1000)
'hello'*3


# len함수 -------------------------------------------------
len(range(0,10,2))
len(['james',17,176.5,True])
len('안녕하세요')
hello = '안녕하세요'
len(hello)
len(hello.encode('utf-8'))  # 글자당 3bite
len(hello.encode('euc-kr')) # 글자당 2bite

# 인덱스(index,slice) 사용하기. (list, tuple, range 전부 사용가능)
a.__getitem__(0)
a.__getitem__(-1)

a[0]        # R과 다르게 0부터 시작한다.
a[-1]       # 맨끝은 -1
a[len(a)-1] # len은 맨끝이 아니다. -1을 해줘야한다.
a[10-1]

a[0:4]      # 슬라이스. 4직전까지 잘라낸다.
a[0:len(a)]
a[4:10]     # 앞의것은 포함하지만 뒤의것은 포함하지 않는다.
a[4:-1]     # 끝의 것 직전까지 가져온다.

a[2:8:3]    # 2부터 8직전까지  3씩 증가시켜서. a[2], a[5]
a[2:9:3]

a[:8]       # 0부터 8직전까지
a[4:]       # 4부터 끝까지.

a[2::3]     # 2부터 끝까지 3씩 증가.
a[7::2]     # 7부터 끝까지 2씩 증가.
a[::2]      # 0부터 끝까지 2씩 증가.

a[5:1:-1]   # 5부터 1직전까지 거꾸로.
a[::-1]     # 끝부터 처음까지 거꾸로.

a[9] = 99 # 기존의 데이터를 바꿔줄 수 있다. (list만 가능)

range(10)[slice(4,7,2)]
range(10)[slice(3,12,2)]  # 자기가 알아서 끝을 찾아준다.

c = slice(4,7,2)
a[c]

a[2:5] = ['a','b','c']
a

a[2:5] = [1000]
a

a[2]   = [20,30,40] #list안에 list를 만들어준다.
a

del a[2]
a

a[1:3] = [10,20,30,40,50]
a

a[2:8:2] = ['a','b','c']
a

# 문자도 똑같이 적용된다.

# del함수 (del : 데이터 개별적으로는 list만 가능하다. ) ---------------
del a,b,c,d



# Unit_12 딕셔너리 사용하기 -----------------------------------------
x = dic()
x = {}

lux = [490,334,550,18.72]
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux1 = dict(health=490,mana=334,melee=550,armor=18.72)
lux2 = dict(zip(['health','mana'],[490,334]))  # list
lux3 = dict([('health',490),('mana',334)])     # tuple
lux4 = dict({'health':490,'mana':334})

lux['health'] = 500
lux['health2'] = 700
'health' in lux
'health' not in lux
len(lux)   # 키의 개수

# 퀴즈
x = {10: 'Hello', 'world': 30}
x[10]

# 연습문제
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

# 심사문제




# --------------------------------------------------------------------


# 8
korean,english,mathematics,science=map(int,input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >=80)

print( int(input('')) >= 90 and int(input('')) >  80 and int(input('')) >  85 and int(input('')) >= 80 )

# 9
S = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

print(S)

# 10. -10에서 10까지 범위 지정하기.
tuple(range(-10,10,int(input(''))))

# 11(1) 리스트 끝부분 삭제하기.
x = input().split()
del x[-5:]
x=tuple(x)
print(x)

# 11(2) : 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결.
print(input()[1::2]+input()[::2])

# 12
print(dict(zip(input().split(),map(float,input().split()))))


