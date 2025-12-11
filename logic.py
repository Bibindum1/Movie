import json
import os

DATA_FILE = "movies.json"

def load_movies(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            movies = json.load(f)
            return movies
    except json.JSONDecodeError:
        return []

def save_movies(path: str, movies: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)

def display_movies(movies: list[dict]) -> None:
    if not movies:
        print("Список фильмов пуст.")
    else:
        print("\nСписок фильмов:")
        for movie in movies:
            status = "Просмотрен" if movie["watched"] else "Не просмотрен"
            print(f"[{movie['id']}] {movie['title']} ({movie['year']}) — {status}")

def add_movie_ui(path: str, movies: list[dict]) -> None:
    title = input("Введите название фильма: ").strip()
    year_raw = input("Введите год: ").strip()

    if not year_raw.isdigit():
        print("Ошибка: год должен быть числом.")
        return

    year = int(year_raw)
    add_movie(path, movies, title, year)
    print("Фильм успешно добавлен!")

def mark_watched_ui(path: str, movies: list[dict]) -> None:
    title = input("Введите название фильма: ").strip()

    if not title:
        print("Ошибка: название не может быть пустым.")
        return

    found = False
    for movie in movies:
        if movie.get("title", "").lower() == title.lower():
            movie["watched"] = True
            found = True
            break

    if found:
        save_movies(path, movies)
        print("Фильм отмечен как просмотренный!")
    else:
        print("Фильм с таким названием не найден.")

def find_movies_ui(movies: list[dict]) -> None:
    year_raw = input("Введите год для поиска: ").strip()

    if not year_raw.isdigit():
        print("Ошибка: год должен быть числом.")
        return

    year = int(year_raw)
    results = find_by_year(movies, year)

    if not results:
        print(f"Фильмов за {year} год не найдено.")
    else:
        print(f"Фильмы за {year} год:")
        for movie in results:
            status = "Просмотрен" if movie["watched"] else "Не просмотрен"
            print(f"[{movie['id']}] {movie['title']} ({movie['year']}) — {status}")

def add_movie(path: str, movies: list[dict], title: str, year: int) -> list[dict]:
    if movies:
        new_id = max(movie["id"] for movie in movies) + 1
    else:
        new_id = 1

    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False,
    }
    movies.append(new_movie)
    save_movies(path, movies)
    print("Фильм добавлен\n")
    return movies

def mark_watched(path: str, movies: list[dict], title: str) -> list[dict]:
    for movie in movies:
        if movie.get("title") == title:
            movie["watched"] = True
    save_movies(path, movies)
    return movies

def find_by_year(movies: list[dict], year: int) -> list[dict]:
    return [movie for movie in movies if movie.get("year") == year]
