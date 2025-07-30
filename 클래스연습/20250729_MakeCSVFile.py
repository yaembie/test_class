import os
import csv
import random
from faker import Faker

fake = Faker()

def random_grade():
    if random.random() < 0.8:  # 80% 확률로 숫자
        return random.randint(60, 100)
    else:                      # 20% 확률로 문자
        return random.choice(['a', 'b', 'c'])

filepath = "data/student2.csv"
# test_data = [(fake.name(), fake.pyint(min_value=40, max_value=100), fake.pyint(min_value=40, max_value=100), fake.pyint(min_value=40, max_value=100)) for i in range(30)]
test_data = [(fake.name(), random_grade(), random_grade(), random_grade()) for i in range(30)]

# csv파일을 쓰기모드 'w'로 열기(인코딩 'cp949', 라인 종료 문자 설정 'newline = '')
with open(filepath, 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file) # 파일 객체를 csv.writer의 인자로 전달해 새로운 writer 객체를 생성

    csv_writer.writerow(['이름', '수학', '영어', '과학']) # 헤더 작성
    for arr in test_data:
        csv_writer.writerow(arr) # 데이터 행 추가

# 왜인지 faker가 안돼서 terminal에서 python 하여 실행함
# pip install faker=8 하니 해결됨