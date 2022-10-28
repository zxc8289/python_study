# 파일 읽기
file_editor = open(file="fileio/test.txt", mode="r", encoding="UTF-8")
my_text = file_editor.readline()
my_text1 = file_editor.readline()
my_text2 = file_editor.readline()

file_editor.close()

print(my_text)
print(my_text1)
print(my_text2)