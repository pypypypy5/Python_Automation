#같은 디렉토리에 있는 t.txt 파일의 대문자로만 이루어진 부분 문자열을 input으로 대체, 저장
import re

f = open('t.txt', 'r')
string = f.read()
f.close()

mo = re.compile('[A-Z]{2,}')
li = mo.findall(string)

for i in li:
    replace_str = input(f'Enter {i}:\n')
    pattern = re.compile(i)
    string = pattern.sub(replace_str, string, count=1)

f = open('t.txt', 'w')
f.write(string)
f.close()

print(string)