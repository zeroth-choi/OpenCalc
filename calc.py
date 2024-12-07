import sub.ops as ops
print("연산 종류")
print(" 1: 더하기")
print(" 2: 빼기")
print(" 3: 곱하기")
print(" 4: 나누기")
def main():
    while True:
        choice = input("(1/2/3/4) 중에서 선택하세요: ")
        if choice in ('1', '2', '3', '4'):
            num1 = int(input("첫번째 수: "))
            num2 = int(input("두번째 수: "))
            if choice == '1':
                print(num1, "+", num2, "=", ops.add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", ops.subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", ops.multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", ops.divide(num1, num2))
        else:
            break
if __name__ == "__main__":
    main()