from logic import load_movies, display_movies, add_movie_ui, mark_watched_ui, find_movies_ui, DATA_FILE

def show_menu():
    print("\nКаталог фильмов")
    print("1 - Показать все фильмы")
    print("2 - Добавить фильм")
    print("3 - Отметить фильм как просмотренный")
    print("4 - Найти фильмы по году")
    print("0 - Выход")

def main():
    movies = load_movies(DATA_FILE)

    while True:
        show_menu()
        choice = input("Выберите пункт:\n")

        if choice == "1":
            display_movies(movies)
        elif choice == "2":
            add_movie_ui(DATA_FILE, movies)
        elif choice == "3":
            mark_watched_ui(DATA_FILE, movies)
        elif choice == "4":
            find_movies_ui(movies)
        elif choice == "0":
            print("Всего доброго!")
            break
        else:
            print("Ошибка! Такого пункта меню нет.")

if __name__ == "__main__":
    main()
