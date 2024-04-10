import random

howmany = int(input())

capital = {'Korea':'Seoul','America':'Washington','Japan':'Tokyo','China':'Beijing','Russia':'Moscow'}
country = list(capital.keys())

for i in range(howmany):
    testfi = open(f'C:\\Users\\신효재\\OneDrive - 연세대학교 (Yonsei University)\\바탕 화면\\Python Automation\\test\\no{i+1}.txt', 'w')
    answerfi = open(f'C:\\Users\\신효재\\OneDrive - 연세대학교 (Yonsei University)\\바탕 화면\\Python Automation\\test\\no{i+1}ans.txt', 'w')
    testfi.write(f'Test no{i+1}\n')
    answerfi.write(f'Answer no{i+1}\n')
    random.shuffle(country)

    for j in range(len(country)):
        
        ans = []
        ans.append(capital[country[j]])
        wrongans = list(capital.values())
        wrongans.remove(ans[0])
        wrongans = random.sample(wrongans, 3)
        ans.extend(wrongans)
        random.shuffle(ans)
        answerfi.write(f'\n{j+1}. {ans.index(capital[country[j]])+1}\n')

        testfi.write(f'\n{j+1}. Choose the capital of {country[j]}\n\n')
        
        for k in range(4):
            testfi.write(f'\t{k+1}. {ans[k]}\n')