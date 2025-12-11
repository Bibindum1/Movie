import os
import json
import pytest
from logic import *


def test_load_movies_empty(tmp_path):
    path = tmp_path / "movies.json"
    movies = load_movies(str(path))
    assert movies == []


def test_load_movies_valid(tmp_path):
    path = tmp_path / "movies.json"
    test_data = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    movies = load_movies(str(path))
    assert movies == test_data


def test_load_movies_invalid_json(tmp_path):
    path = tmp_path / "movies.json"
    with open(path, "w") as f:
        f.write("invalid json")
    movies = load_movies(str(path))
    assert movies == []


def test_save_movies(tmp_path):
    path = tmp_path / "movies.json"
    movies = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    save_movies(str(path), movies)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == movies


def test_add_movie(tmp_path):
    path = tmp_path / "movies.json"
    movies = []
    movies = add_movie(str(path), movies, "Фильм", 2020)

    assert len(movies) == 1
    assert movies[0]["title"] == "Фильм"
    assert movies[0]["year"] == 2020
    assert movies[0]["id"] == 1
    assert movies[0]["watched"] is False

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1


def test_add_movie_next_id(tmp_path):
    path = tmp_path / "movies.json"
    movies = [{"id": 5, "title": "Old", "year": 2010, "watched": False}]
    movies = add_movie(str(path), movies, "New", 2020)

    assert len(movies) == 2
    assert movies[1]["id"] == 6


def test_mark_watched(tmp_path):
    path = tmp_path / "movies.json"
    movies = [{"id": 1, "title": "Фильм", "year": 2020, "watched": False}]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(movies, f)

    movies = mark_watched(str(path), movies, "Фильм")
    assert movies[0]["watched"] is True


def test_find_by_year():
    movies = [
        {"id": 1, "title": "A", "year": 2020, "watched": False},
        {"id": 2, "title": "B", "year": 2021, "watched": False},
        {"id": 3, "title": "C", "year": 2020, "watched": True},
    ]
    results = find_by_year(movies, 2020)
    assert len(results) == 2
    assert {m["title"] for m in results} == {"A", "C"}
