# widt as는 close를 자동으로 처리해준다.
# 바이너리 파일 입력 mode="bw"
with open(file="fileio/test.txt", mode="bw") as file_editor:
    file_editor.write(b"aas")
