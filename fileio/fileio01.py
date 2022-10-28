# 파일 읽기
file_editor = open(file="fileio/test.txt", mode="r", encoding="UTF-8")
my_text = file_editor.read()
file_editor.close()

print(my_text)
