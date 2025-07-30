import os
import csv
import random
from faker import Faker

class Grademanagement():
    def __init__(self):
        pass

    def random_grade(self):
        if random.random() < 0.9:  # 80% 확률로 숫자
            return random.randint(60, 100)
        else:                      # 20% 확률로 문자
            return random.choice(['a', 'b', 'c'])
        
    def CreateDataFile(self, filepath):
        # 1. 데이터 로딩-a
        # student.csv 파일에서 학생 데이터를 읽어와 리스트에 저장합니다.
        # CSV의 각 행은 이름, 수학, 영어, 과학 형태입니다.
        # 점수가 숫자가 아닌 경우(예: abc)에는 0점으로 처리해야 합니다.
        gm = Grademanagement()
        inputfile = input(f"파일경로를 입력해주세요(기본값:{filepath}). : ")
        if inputfile != '' and inputfile != None:
            filepath = inputfile
        test_data = [(fake.name(), gm.random_grade(), gm.random_grade(), gm.random_grade()) for i in range(30)]
        with open(filepath, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file) # 파일 객체를 csv.writer의 인자로 전달해 새로운 writer 객체를 생성

            csv_writer.writerow(['이름', '수학', '영어', '과학']) # 헤더 작성
            for arr in test_data:
                csv_writer.writerow(arr) # 데이터 행 추가
            print("데이터 파일을 생성하였습니다.")

    def DataLoading(self, filepath):
        # 1. 데이터 로딩-b
        # student.csv 파일에서 학생 데이터를 읽어와 리스트에 저장합니다.
        # CSV의 각 행은 이름, 수학, 영어, 과학 형태입니다.
        # 점수가 숫자가 아닌 경우(예: abc)에는 0점으로 처리해야 합니다.
        # 파일이 없으면 파일을 찾을 수 없습니다라고 출력 후 프로그램을 종료합니다.
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader) # 제목줄 건너뛰기
                data_list = list(csv_reader)
            for i in range(0, len(data_list)):
                for j in range(1, 4):
                    if not data_list[i][j].isdigit():
                        data_list[i][j] = 0
        else:
            data_list = "failed"
            print("파일을 찾을 수 없습니다")

        return data_list
    
    
    def GetAverages(self, filepath):
        data_list = Grademanagement().DataLoading(filepath)
        # 2. 통계분석-a
        # 각 학생의 평균 점수를 계산하는 함수를 만드세요.
        for i in range(0, len(data_list)):
            grages = [int(data_list[i][1]), int(data_list[i][2]), int(data_list[i][3])]
            average = sum(grages) / len(grages)
            data_list[i].append(round(average,2))
        return data_list
    
    def GetMinMax(self, filepath):
        # 2. 통계분석-b
        # 전체 학생 중 평균이 가장 높은 학생과 가장 낮은 학생을 찾아 이름(평균점수) 형식으로 출력하세요.
        data_list_average = Grademanagement().GetAverages(filepath)
        data_list_average.sort(key=lambda x:-x[-1])
        print(f"가장 높은 학생 : {data_list_average[0][0]}({data_list_average[0][4]})")
        print(f"가장 낮은 학생 : {data_list_average[len(data_list_average)-1][0]}({data_list_average[len(data_list_average)-1][4]})")
        

    def GetGradesOfStudent(self, filepath):
        # 3. 검색 기능
        # 사용자로부터 이름을 입력받아 해당 학생의 각 과목 점수와 평균 점수를 출력하세요.
        # 학생이 없으면 학생을 찾을수 없습니다. 라고 출력하세요.
        data_list_average =  Grademanagement().GetAverages(filepath)
        name = data_list_average[0][0]
        inputname = input(f"찾으시는 학생의 이름을 입력해주세요(기본값 : {name})")
        if inputname != '' and inputname != None:
            name = inputname
        target_row = [(i) for i in range(len(data_list_average)) if data_list_average[i][0] == name]
        if target_row == []:
            print("학생을 찾을수 없습니다.")
        else:
            target_data = data_list_average[target_row[0]]
            print(f"순번 : {target_row[0] + 1}")
            print(f"이름 : {target_data[0]}")
            print(f"수학 : {target_data[1]}")
            print(f"영어 : {target_data[2]}")
            print(f"과학 : {target_data[3]}")
            print(f"평균 : {target_data[4]}")
    
    def SortDown(self, filepath):
        # 4. 성적 정렬
        # 학생들을 평균 점수 기준으로 내림차순 정렬하여 이름과 평균 점수를 출력하세요.
        data_list_average = gm.GetAverages(filepath)
        data_list_average.sort(key=lambda x:-x[-1])
        for i in range(0, len(data_list_average)):
            print(f"{data_list_average[i][0]}({data_list_average[i][4]})")
    
    def CreatePassFile(self, filepath, new_filepath):
        # 5. 파일 저장
        # 평균 점수가 70점 이상인 학생만 새로운 파일 pass_student.csv 에 저장하세요.
        data_list_average =  Grademanagement().GetAverages(filepath)
        target_row = [(i) for i in range(len(data_list_average)) if data_list_average[i][4] >= 70]
        if target_row == []:
            print("70점 이상인 학생이 없습니다.")
        else:
            inputfile = input(f"새로 만들 파일 경로를 입력하세요(기본값 : {new_filepath})")
            if inputfile != '' and inputfile != None:
                new_filepath = inputfile
            with open(new_filepath, 'w', encoding='utf-8', newline='') as file:
                csv_writer = csv.writer(file) # 파일 객체를 csv.writer의 인자로 전달해 새로운 writer 객체를 생성
                csv_writer.writerow(['이름', '수학', '영어', '과학']) # 헤더 작성
                for i in target_row:
                    csv_writer.writerow(data_list_average[i]) # 데이터 행 추가
                print("파일을 생성하였습니다.")


fake = Faker()
gm = Grademanagement()

filepath = "data/student.csv"
new_filepath = "data/pass_student.csv"

while True:

    func = int(input('''
                 원하시는 번호를 입력하세요.
                 0. 데이터 파일 생성
                 1. 데이터 로딩
                 2. 통계 분석
                 3. 검색 기능
                 4. 성적 정렬
                 5. 파일 저장
                 6. 종료
                 '''))
    if func == 0:
        gm.CreateDataFile(filepath)
    elif func == 1:
        inputfile = input(f"파일경로를 입력해주세요(기본값:{filepath}). : ")
        if inputfile != '' and inputfile != None:
            filepath = inputfile
        data_list = gm.DataLoading(filepath)
        if data_list == "failed":
            print("프로그램을 종료합니다.")
            break
        else :
            print("데이터 로딩을 완료하였습니다.")
            # print(data_list)
    elif func == 2:
        gm.GetMinMax(filepath)
    elif func == 3:
        gm.GetGradesOfStudent(filepath)
    elif func == 4:
        gm.SortDown(filepath)
    elif func == 5:
        gm.CreatePassFile(filepath, new_filepath)
    elif func == 6:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하였습니다.")