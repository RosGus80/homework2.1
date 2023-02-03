import random



def write_game_record(name, score):
    """Записывает  в файл истории имя и количество очков игрока в этом прохождении, в формате, удобном для чтения                                                                                                                                                                                           """

    with open("history.txt", "wt") as file:

        file.write(f"{name} {score}")


def read_rankings():
    with open("history.txt") as file:
        print(file.read())


def read_stats():
    """Поскольку результаты игр в файле истории записаны как "имя" - "очки" через пробел, после сплита я беру второй элемент списка, который всегда окажется количеством очков и прибавляю его к сумме очков"""
    with open("history.txt") as file:
        games_counter = 0
        record = 0
        for line in file:
            stat = line.split(" ")
            if int(stat[1]) > record:
                record = int(stat[1])
            games_counter += 1
        print(f"Всего игр сыграно: {games_counter}")
        print(f"Максимальный рекорд: {record}")





username = input('Введите ваше имя: ')
userscore = 0


with open("words.txt") as file:

    for line in file:
        word = [] # Сделать список нужно, чтобы перемешать его составляющие (символы)
        answer = line.rstrip("\n")

        for char in answer:
            word.append(char)

        word = random.sample(word, len(answer))
        word = "".join(word)
        user_input = input(f"Угадайте слово: {word}: ").lower()

        if user_input == answer:
            print("Верно! Вы получаете 10 очков")
            userscore += 10
        else:
            print(f"Неверно! Верный ответ – {line}")

print("\n")


write_game_record(username, userscore)
read_rankings()
print("\n")
read_stats()


