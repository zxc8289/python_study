# 연산자 우선순위 *,/가 +,-보다 우선
from decimal import Decimal
import math

temp = 1+2*3

# 연산 자 우선순위를 바꾸기 위해서는 () 사용
print((1+2)*3)
print(32321)

# 숫자는 0으로 나눌수 없다.
# temp = 1/0

# 실수 중에서 2진수로 계산할 수 없는 숫자는 근사값이 나온다.
temp = 1.1 + 0.1
print(f'{temp}')

# Decimal을 사용하면 정확한 값 확인가능, 자리수 한정
temp = Decimal('1.1') + Decimal('0.1')
temp = float(temp)
print(f'{temp}')

# 진수변환

# 2진수
temp = 2
temp = bin(temp)
print(f'{temp}')

# 8진수
temp = 2
temp = oct(temp)
print(f'{temp}')

# 16진수
temp = 2
temp = hex(temp)
print(f'{temp}')

