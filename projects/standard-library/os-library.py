import os

cwd = os.getcwd()

print("Current working directory: ", cwd)


# Listr los archivos .txt
txt_files = [f for f in os.listdir(cwd) if f.endswith('.txt')]
print("Text files: ", txt_files)


os.rename('file1.txt', 'file2.txt')
