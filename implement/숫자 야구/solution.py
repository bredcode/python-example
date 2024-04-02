from random import randint

def generate_answer():
    answer = []
    number = 0

    i = 0
    while i < 3:
        number = randint(1, 9)
        if number not in answer:
            answer.append(number)
            i += 1

    print("1과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return answer


def get_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 0
    guess = []
    while i < 3:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        if not (1 <= gue_number <= 9):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in guess:
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            guess.append(gue_number)
            i += 1

    return guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count

def main():
    tries = 0
    answer = generate_answer()

    while 1:
        guess = get_guess()
        strike, ball = get_score(guess, answer)
        print("{}S {}B ".format(strike, ball))

        if strike == 3:
            tries += 1
            break
        else:
            tries += 1

    print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

if __name__ == "__main__":
    main()
