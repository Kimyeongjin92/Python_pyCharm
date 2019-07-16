# ====================================================================
# 8
korean,english,mathematics,science=map(int,input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >=80)

print( int(input('')) >= 90 and int(input('')) >  80 and int(input('')) >  85 and int(input('')) >= 80 )


# ====================================================================
# 9
S = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

print(S)


# ====================================================================
# 10. -10에서 10까지 범위 지정하기.
tuple(range(-10,10,int(input(''))))


# ====================================================================
# 11(1) 리스트 끝부분 삭제하기.
x = input().split()
del x[-5:]
x=tuple(x)
print(x)


# ====================================================================
# 11(2) : 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결.
print(input()[1::2]+input()[::2])


# ====================================================================
# 12
print(dict(zip(input().split(),map(float,input().split()))))