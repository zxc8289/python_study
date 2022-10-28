# 파일 읽기
file_editor = open(file="fileio/test.txt", mode="r", encoding="UTF-8")

# 파일 데이터를 한줄씩 배열로 가져옴
my_text = file_editor.readlines()

file_editor.close()

print(my_text)
