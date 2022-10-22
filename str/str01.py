from ast import Delete
from multiprocessing.sharedctypes import Value
import tempfile

temp = "가나다"
# 문자열은 요소를 번호로 가져올 수 있다.
# temp[0] = '가'
print(f'{temp[0]=}')

# 문자열은 불변 요소 변경시 에러
# temp[0] = "라"
temp = "라"
# 변수에 다른 문자열을 넣을 수는 있다.
# temp = "라"

# 변수삭제
del temp

temp = "가나다"
print(f'{id(temp)=}')
# id(temp)=1917727286224
temp = "라"
print(f'{id(temp)=}')
# id(temp)=1917727450784
temp = "가나다"
print(f'{id(temp)=}')
# id(temp)=1917727286224
# 문자열, 숫자는 메모리 어딘가에 저장되어 다시 불러와진다.

temp = "가나다\n라마바"
# 문자열을 여러줄로 출력하고 싶으면 \n 사용한다.

temp = '''\
가나다
마바사
'''

temp = '그가 말했다. "안녕?"'
# 쌍따옴표 문자열 안에 넣고 싶을 때 홑따옴표로 감싼다.

temp = "나는 생각했다. '잠온다'"
# 반대의 경우

temp = ''' 그가 말했다. "안녕?" 나는 생각했다. '잠온다' '''
# 모두 넣고 싶을경우 '''나 """ 사용


temp = '가나다라'
temp = temp[-1]

# 범위를 넘어서는 값을 주면 에러가 발생한다. 0,1,2,3
# temp = temp[4]

temp = "가나다라"
temp = temp[-4]

# 위와 마찬가지로 넘어서는 값이 나오면 에러 발생
#temp = temp[-5]

# 처음부터 2번까지 컷팅
temp = "가나다라"
temp = temp[:2]
print(f'{temp=}')

# 처음부터 끝까지 컷팅
temp = "가나다라"
temp = temp[:]
print(f'{temp=}')

# 없는 데이터일경우 빈값이 출력됨
temp = "가나다라"
temp = temp[5:100]
print(f'{temp=}')

temp = "가나다라"
for item in temp:
    print(item)

temp = "가나" "다라"
print(f'{temp=}')

# 문자열의 길이 len
temp = len(temp)
print(f'{temp=}')

temp = "가나다라"
temp = f"한글은 {temp}"
print(f'{temp=}')

temp = "가나다라"
temp = "한글은 " + temp
print(f'{temp=}')

temp = "가나다라"
temp = "한글은 %s" % temp
print(f'{temp=}')

temp = "가나다라"
temp = "한글은 {0}".format(temp)
print(f'{temp=}')

temp = "가나다라"
temp = temp.startswith("가나")
# 문자열의 시작을 확인하여 True False로 리턴한다.
print(f'{temp=}')

temp = "가나다라"
temp = temp.endswith("다라")
# 문자열의 끝을 확인하여 True False로 리턴한다.
print(f'{temp=}')

temp = "가나다라"
temp = temp.index("가")
# index는 해당문자의 요소 번호를 리턴한다
print(f'{temp=}')


temp = "1"
temp = temp.rjust(5, "!")
# 내가 원하는 문자열 채우기
print(f'{temp=}')
