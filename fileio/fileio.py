# 파일 읽기
file_editor = open(file="fileio/test.txt", mode="a", encoding="UTF-8")

# 파일 쓰기
file_editor.write("안녕하세요.")
file_editor.write("\n반갑습니다.")

# 파일 저장 닫기
file_editor.close()
