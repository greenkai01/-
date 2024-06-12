import requests
from bs4 import BeautifulSoup
from datetime import datetime

datetime_today = int(datetime.today().day)
datetime_real_today = str(datetime.today().day)

datetime_year = str(datetime.today().year)

URL = 'https://school.koreacharts.com/school/meals/B000012911/contents.html'
headers = {"User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res = requests.get(URL, headers=headers)
res.raise_for_status()

def mycalculator(answer11):
  global a1
  global b1
  if answer11 == 1:
    a1 = input('\n' + 'a+b를 하고 싶으면 a를 먼저 입력해주세요.') 
    b1 = input('\n' + 'b를 입력해주세요.')
    result = str(int(a1)+int(b1))
  elif answer11 == 2:
    a1 = input('\n' + 'a-b를 하고 싶으면 a를 먼저 입력해주세요.')
    b1 = input('\n' + 'b를 입력해주세요.')
    result = str(int(a1)-int(b1))
  elif answer11 == 3:
    a1 = input('\n' + 'a*b를 하고 싶으면 a를 먼저 입력해주세요.')
    b1 = input('\n' + 'b를 입력해주세요.')
    result = str(int(a1)*int(b1))
  elif answer11 == 4:
    a1 = input('\n' + 'a/b의 정수 몫을 알고 싶으면 a를 먼저 입력해주세요.')
    b1 = input('\n' + 'b를 입력해주세요.')
    result = str(int(a1)//int(b1))
  elif answer11 == 5:
    a1 = input('\n' + 'a/b의 나머지를 알고 싶으면 a를 먼저 입력해주세요.')
    b1 = input('\n' + 'b를 입력해주세요.')
    result = str(int(a1)%int(b1))
  elif answer11 == 6:
    a1 = input('\n' + 'a**b를 하고 싶으면 a를 먼저 입력해주세요.')
    b1 = input('\n' + 'b를 입력해주세요.')
    result = str(int(a1)**int(b1))
  return result
    

soup = BeautifulSoup(res.content, 'html.parser')

table = soup.select_one('body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table')

hb = list()
hl = list()
hd = list()
hdate = list()

#for문을 이용하여 table 안에 있는 tbody 안에 있는 tr을 하나씩 가져옴

for tr in table.find_all('tr'): #tr값을 하나 가져옴 (이거를 급식표가 16일꺼까지 나와있으면 16번 반복)
  tds = list(tr.find_all('td')) #tds에다가 가져온 tr에 있는 모든 td를 list로 만들기
  for td in tds: #아까 tds에 넣은 모든 td 중 하나를 가져옴
    if td.find('p'): #td값에 p값을 찾으면 통과
      p = list(td.find_all('p')) #가져온 td값 중 모든 p값을 list로 만듬
      hb.append(p[0].text + '\n') #list로 만든 p값 중 첫번째 값을 text값만 불러옴
      hl.append(p[1].text) #list로 만든 p값 중 두번째 값을 text값만 불러옴
      hd.append(p[2].text) #list로 만든 p값 중 세번째 값을 text값만 불러옴
      hdate.append(tds[0].text) #list로 만든 tds값 중 첫번째 값을 text값만 불러옴

hanilgo_real_month = str(datetime.today().month)

while True:
  try:
    answer = int(input('*원하는 항목의 번호를 입력 후 enter키를 눌러주세요.' + '\n' + '1. 오늘 시간표 보기'+ '\n' +'2. 오늘 급식표 보기'+ '\n' +'3. 일기쓰기'+ '\n' + '4. 일기읽기'+ '\n' + '5. 일기 모두 지우기'+ '\n' + '6. 계산기 이용하기'+ '\n' + '7. 그만하기'+ '\n'))
    if answer == 1:
      f1 = open("schedule.txt", "r")
      answer1 = int(input('\n' + '*원하는 항목의 번호를 입력 후 enter키를 눌러주세요.' + '\n' + '1. 월요일'+ '\n' +'2. 화요일'+ '\n' +'3. 수요일'+ '\n' +'4. 목요일'+ '\n' +'5. 금요일'+ '\n' +'6. 토요일'+ '\n' +'7. 일요일'+ '\n'))
      answer2 = f1.readline()
      answer3 = f1.readline()
      answer4 = f1.readline()
      answer5 = f1.readline()
      answer6 = f1.readline()
      answer7 = f1.readline()
      answer8 = f1.readline()
      f1.close()
      if answer1 == 1:
        print('\n'+'월요일 시간표: '+answer2)
      elif answer1 == 2:
        print('\n'+'화요일 시간표: '+answer3)
      elif answer1 == 3:
        print('\n'+'수요일 시간표: '+answer4)
      elif answer1 == 4:
        print('\n'+'목요일 시간표: '+answer5)
      elif answer1 == 5:
        print('\n'+'금요일 시간표: '+answer6)
      elif answer1 == 6:
        print('\n'+'토요일 시간표: '+answer7)
      elif answer1 == 7:
        print('\n'+'일요일 시간표: '+answer8)
    elif answer == 2:
      answer9 = int(input('\n' + '*원하는 항목의 번호를 입력 후 enter키를 눌러주세요.' + '\n' + '1. 아침'+ '\n' +'2. 점심'+ '\n' +'3. 저녁'+ '\n'))
      hanilgo_month = soup.select_one('body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-header.with-border > h2').text
      print('\n' + hanilgo_month)
      if answer9 == 1:
        hanilgo_breakfast_1 = hb[datetime_today - 1]
        hanilgo_date_1 = hdate[datetime_today - 1]
        print('\n' + hanilgo_real_month + '월 ' + hanilgo_date_1 + '일')
        print(hanilgo_breakfast_1)
      if answer9 == 2:
        hanilgo_lunch_1 = hl[datetime_today - 1]
        hanilgo_date_2 = hdate[datetime_today - 1]
        print('\n' + hanilgo_real_month + '월 ' + hanilgo_date_2 + '일')
        print(hanilgo_lunch_1)
      if answer9 == 3:
        hanilgo_dinner_1 = hd[datetime_today - 1]
        hanilgo_date_3 = hdate[datetime_today - 1]
        print('\n' + hanilgo_real_month + '월 ' + hanilgo_date_3 + '일')
        print(hanilgo_dinner_1)
    elif answer == 3:
      answer10 = input('오늘의 일기를 써주세요.'+'\n')
      f2 = open("diary.txt","a")
      f2.write(datetime_year + '년 ' + hanilgo_real_month + '월 ' + datetime_real_today + '일 일기: ' + answer10 + '\n')
      f2.close()
    elif answer == 4:
      f3 = open("diary.txt","r")
      while True:
          line = f3.readline() # 파일의 첫번째 줄부터 line에 저장하여 한줄씩 읽기
          if not line: break # line이 없을때 break
          print(line + '\n')
      f3.close()
    elif answer == 5:
      f4 = open("diary.txt","w")
      f4.write("")
      f4.close()
    elif answer == 6:
      answer11 = int(input('\n' + '*원하는 항목의 번호를 입력 후 enter키를 눌러주세요.' + '\n' + '1. 더하기'+ '\n' +'2. 빼기'+ '\n' + '3. 곱하기'+ '\n' + '4. 나누기(몫(정수자리만))'+ '\n' + '5. 나누기(나머지)'+ '\n' + '6. 제곱'+ '\n'))
      result11 = mycalculator(answer11)
      if answer11 == 1:
        print('\n' + '결과값은 ' + a1 + ' + ' + b1 + ' = ' + result11 + '입니다.' + '\n')
      if answer11 == 2:
        print('\n' + '결과값은 ' + a1 + ' - ' + b1 + ' = ' + result11 + '입니다.' + '\n')
      if answer11 == 3:
        print('\n' + '결과값은 ' + a1 + ' * ' + b1 + ' = ' + result11 + '입니다.' + '\n')
      if answer11 == 4:
        print('\n' + '결과값은 ' + a1 + ' / ' + b1 + ' 의 정수 몫 = ' + result11 + '입니다.' + '\n')
      if answer11 == 5:
        print('\n' + '결과값은 ' + a1 + ' / ' + b1 + ' 의 나머지 = ' + result11 + '입니다.' + '\n')
      if answer11 == 6:
        print('\n' + '결과값은 ' + a1 + ' ** ' + b1 + ' = ' + result11 + '입니다.' + '\n')
    elif answer == 7:
      print('\n' + "제 프로그램을 이용해 주셔서 감사합니다." + '\n')
      break

  except:
    print('다시 입력하시오. (항목에 있는 숫자만 입력해야함)')






------------------------------------------------------------------------------------------------------------------------
#여기서부터는 추가로 해줘야 할 것들 모음임

pip install datetime #깔아야 할 모듈

pip install beautifulsoup4 #깔아야 할 모듈

pip install requests #깔아야 할 모듈





f1 = open("schedule.txt","w") #파일 만들기
mon = input("월요일 시간표를 입력해주세요:")
tue = input("화요일 시간표를 입력해주세요:")
wed = input("수요일 시간표를 입력해주세요:")
thu = input("목요일 시간표를 입력해주세요:")
fri = input("금요일 시간표를 입력해주세요:")
sat = input("토요일 시간표를 입력해주세요:")
sun = input("일요일 시간표를 입력해주세요:")
f1.write(mon+"\n")
f1.write(tue+"\n")
f1.write(wed+"\n")
f1.write(thu+"\n")
f1.write(fri+"\n")
f1.write(sat+"\n")
f1.write(sun)
f1.close()

#월: 수학(이동규) , 사회(배장렬) , 국사(윤형덕) , 진로(김명연) , 과학(박영철) , 창체 , 정보(구재랑) , 수학(이동규)
#화: 수학(황억상) , 국사(전대희) , 영어(신지원) , 체육(박민춘) , 국어(류연득) , 수학(이동규) , 정보(구재랑) , 영어(David)
#수: 영어(신지원) , 사회(배장렬) , 국어(서인우) , 수학(황억상) , 창체 , 창체 , 체육(김동화) , 정보(구재랑)
#목: 영어(David) , 국사(윤형덕) , 국어(서인우) , 수학(이동규) , 국어(류연득) , 과학(김채운) , 과학(김현동) , 영어(신지원)
#금: 음악(조은산) , 음악(조은산) , 사회(송미라) , 수학(이상훈) , 영어(신지원) , 실험(김민석) , 정보(구재랑) , 국어(서인우)
#토: 모의고사 -> 진진인 -> 자습
#일: 자습





f2 = open("diary.txt","w") #파일 만들기
f2.close()
