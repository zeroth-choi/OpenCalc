print("연산 종류")
print(" 1: 더하기")
print(" 2: 빼기")
print(" 3: 곱하기")
print(" 4: 나누기")
def main():
    while True:
        choice = input("(1/2/3/4) 중에서 선택하세요: ")
        if choice in ('1', '2', '3', '4'):
            pass
        else:
            break
if __name__ == "__main__":
    main()