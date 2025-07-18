class Operation:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def dif(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        if num2 == 0:
            res = "0으로 나눌 수 없습니다."
        else : 
            res = num1 / num2
        return res
    
def getnum():
    while(True):
        try:
            res = float(input("숫자를 입력해 주세요. : "))
            break
        except:
            print("잘못 입력하셨습니다.")
    return res
    
op = Operation()

# 숫자 입력 부분을 함수로 만들어 볼 것
# while(True):
#     try:
#         n1 = float(input("숫자를 입력해 주세요. : "))
#         break
#     except:
#         print("잘못 입력하셨습니다.")
n1 = getnum()


while(True):
    try:
        cal = input("연산 기호를 입력해 주세요.(+, -, *, /, =, end) : ")
        if cal == "end":
            print("계산을 종료합니다.")
            break
        elif cal != "+" and cal != "-" and cal != "*" and cal != "/" and cal != "=" and cal != "end":
            print("잘못 입력하셨습니다.")
            continue
        elif cal == "=":
            print(res)
            # while(True):
            #     try:
            #         n1 = float(input("숫자를 입력해 주세요. : "))
            #         break
            #     except:
            #         print("잘못 입력하셨습니다.")
            n1 = getnum()
            continue


        # n2 = float(input("숫자를 입력해 주세요. : "))
        n2 = getnum()

        if cal == "+":
            res = op.add(n1, n2)
        elif cal == "-":
            res = op.dif(n1, n2)
        elif cal == '*':
            res = op.mul(n1, n2)
        elif cal == "/":
            res = op.div(n1, n2)

        print(res)
        if res != "0으로 나눌 수 없습니다." and res != "잘못 입력하셨습니다.":
            n1 = res
    except:
        print("잘못 입력하셨습니다.")