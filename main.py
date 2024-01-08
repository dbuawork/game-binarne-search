import random

def binary_search_guessing_game():
    print("Вгадайте число від 1 до 100.")
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        guess = (lower_bound + upper_bound) // 2
        attempts += 1

        print(f"ПК вгадує: {guess}")

        if guess == number_to_guess:
            print(f"ПК вгадав число {number_to_guess} за {attempts} спроб.")
            break
        elif guess < number_to_guess:
            print("Загадане число більше. ПК вгадує більше число.")
            lower_bound = guess + 1
        else:
            print("Загадане число менше. ПК вгадує менше число.")
            upper_bound = guess - 1

if __name__ == "__main__":
    binary_search_guessing_game()