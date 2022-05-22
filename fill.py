from datetime import datetime
from random import randrange, sample

import duckdb
import psycopg
from tqdm import tqdm


def random_time_str(ts, d):
    return datetime.fromtimestamp(randrange(ts, ts + d)).isoformat()


def e(query):
    con_duck.execute(query)
    cur_post.execute(query)


TIMESTEP = 1285286794  # '2010-09-24T02:06:34'
TIMESTEP_DELTA = 7 * 24 * 60 * 60  # 7 days
PRODUCTS_NUMBER = 33
PRICE_RANGE = 100
STORES_NUMBER = 20
SALES_NUMBER = 50000
MAX_QUANTITY = 4
MAX_PRODUCTS = 5

assert MAX_PRODUCTS <= PRODUCTS_NUMBER

if __name__ == '__main__':
    con_duck = duckdb.connect(database='duck.db')
    con_post = psycopg.connect(user='postgres', password='postgres')
    cur_post = con_post.cursor()

    e("drop table if exists product")
    e("drop table if exists sale")

    e("create table product(id integer, price integer)")
    e("create table sale(id integer, product_id integer, store_id integer, quantity integer, time timestamp)")

    for i in range(PRODUCTS_NUMBER):
        e(f"insert into product values ({i}, {randrange(PRICE_RANGE)})")

    e("begin transaction")
    for i in tqdm(range(SALES_NUMBER)):
        store = randrange(STORES_NUMBER)
        time_str = random_time_str(TIMESTEP, TIMESTEP_DELTA)
        products_num = randrange(1, MAX_PRODUCTS + 1)
        products = sample(range(PRODUCTS_NUMBER), products_num)  # ensure unique
        for p in products:
            e(f"""
                insert into sale values (
                  {i},
                  {p},
                  {store},
                  {randrange(1, MAX_QUANTITY + 1)},
                  '{time_str}'
                )
            """)
    e("commit")
