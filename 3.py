import os

# 현재 실행 중인 스크립트의 절대 경로
script_path = os.path.abspath(__file__)
# 디렉토리 경로
directory = os.path.dirname(script_path)

with open(script_path, 'r', encoding='utf-8') as py_file:
    py_content = py_file.read()

txt_file_path = directory + "/your_code.txt"
            # 파일 확장자 변경
with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(py_content)
