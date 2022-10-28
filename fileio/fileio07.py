import pickle

# 바이너리 파일 입력 mode="bw"
with open(file="fileio/test.pickle", mode="bw") as file_editor:
    pickle.dump([1, 2, 3], file_editor)
