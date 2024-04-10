#test 폴더에 입력받은 수만큼 시험지, 답지 파일 만들기
import pyperclip, re

txt = pyperclip.paste()      #str?

phn_rgx = re.compile('(\s)(\d{3,})(-|.)(\d{3,})(-|.)(\d{3,})')
phone = phn_rgx.findall(txt)

mail_rgx = re.compile('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
mail = mail_rgx.findall(txt)

matches = []

for i in phone:
    numbers = '-'.join([i[1],i[3],i[5]])
    matches.append(numbers)
for i in mail:
    matches.append(i)

print('copied results:')
for i in matches:
    print(i)