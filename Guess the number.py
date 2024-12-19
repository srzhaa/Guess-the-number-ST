import random  # Импортируем модуль random для генерации случайных чисел

def guess_the_number():
    print("Welcome to the Number Guessing Game!")  # Приветственное сообщение
    print("I'm thinking of a number between 1 and 100.")  # Информация о диапазоне чисел
    
    # Генерируем случайное число между 1 и 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Инициализируем счетчик попыток
    max_attempts = 10  # Максимальное количество попыток
    
    while attempts < max_attempts:  # Цикл, который продолжается, пока количество попыток меньше максимального
        try:
            guess = int(input("Enter your guess: "))  # Запрашиваем у игрока ввод числа и преобразуем его в целое число
            attempts += 1  # Увеличиваем счетчик попыток на 1
            
            if guess < secret_number:  # Если предположение меньше загаданного числа
                print("Too low! Try again.")  # Сообщаем, что число слишком маленькое
            elif guess > secret_number:  # Если предположение больше загаданного числа
                print("Too high! Try again.")  # Сообщаем, что число слишком большое
            else:  # Если предположение равно загаданному числу
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")  # Сообщаем о победе
                return  # Выходим из функции
        except ValueError:  # Обрабатываем ошибку, если введено не число
            print("Please enter a valid number.")  # Просим ввести корректное число
    
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")  # Сообщаем, что попытки исчерпаны

def main():
    while True:  # Бесконечный цикл для возможности повторной игры
        guess_the_number()  # Запускаем функцию игры
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()  # Запрашиваем у игрока желание сыграть снова
        if play_again != "yes":  # Если игрок не хочет играть снова
            print("Thanks for playing! Goodbye!")  # Благодарим за игру и завершаем программу
            break  # Выходим из цикла

if __name__ == "__main__":
    main()  # Запускаем основную функцию программы
