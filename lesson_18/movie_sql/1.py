import psycopg2
import argparse

from config import get_config


def display_rating(rating_num:float):
    params = get_config()

    conn = psycopg2.connect(**params)

    data = None

    with conn:
        with conn.cursor() as cur:
            cur.execute(f"select movie_name from imdb_top it where it.rating > '{rating_num}'")
            data = cur.fetchall()
    conn.close()
    print(data)
    return data


def find_movie(movie_name:list):
    params = get_config()

    conn: psycopg2._psycopg.connection = None

    movie_list = []
    for movie in movie_name:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"select release_date, rating from imdb_top it where it.movie_name ilike '{movie}'")
                movie_list.append(cur.fetchall())
    print(movie_list)
    return movie_list

    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-m','--movie_name')
    parser.add_argument('-r', '--rating_num')

    args = parser.parse_args()


    if args.rating_num:
        display_rating(args.rating_num)
    if args.movie_name:
        find_movie(args.movie_name.split(","))
        #run movie name function


