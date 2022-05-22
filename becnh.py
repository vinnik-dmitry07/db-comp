import duckdb
import psycopg
from tqdm import tqdm

EXEC_NUMBER = 100

con_duck = duckdb.connect(database='duck.db')
con_post = psycopg.connect(user='postgres', password='postgres')
cur_post = con_post.cursor()

for c, name in [(con_duck, 'DuckDB'), (cur_post, 'PostgreSQL')]:
    def f(q):
        return c.execute(q).fetchall()


    print(name + ':')

    for _ in tqdm(range(EXEC_NUMBER), desc='Порахувати кількість проданого товару'):
        f(f"""
            select sum(sale.quantity)
            from sale
        """)

    for _ in tqdm(range(EXEC_NUMBER), desc='Порахувати вартість проданого товару'):
        f(f"""
            select sum(product.price * sale.quantity)
            from sale
            inner join product
            on sale.product_id = product.id
        """)

    for _ in tqdm(range(EXEC_NUMBER), desc='Порахувати вартість проданого товару за період'):
        f(f"""
            select sum(product.price * sale.quantity)
            from sale
            inner join product
            on sale.product_id = product.id
            where '2010-09-26T02:06:34' < sale.time and sale.time < '2010-09-29T02:06:34'
        """)

    for _ in tqdm(range(EXEC_NUMBER), desc='Порахувати скільки було придбано товару А в мазазині В за період С'):
        f(f"""
            select sum(sale.quantity)
            from sale
            where sale.product_id = 0
            and sale.store_id = 0
            and '2010-09-26T02:06:34' < sale.time and sale.time < '2010-09-29T02:06:34'
        """)

    for _ in tqdm(range(EXEC_NUMBER), desc='Порахувати скільки було придбано товару А в усіх магазинах за період С'):
        f(f"""
            select sum(sale.quantity)
            from sale
            where sale.product_id = 0
            and '2010-09-26T02:06:34' < sale.time and sale.time < '2010-09-29T02:06:34'
        """)

    for _ in tqdm(range(EXEC_NUMBER), desc='Порахувати сумарну виручку магазинів за період С'):
        f(f"""
            select sum(product.price * sale.quantity)
            from sale
            inner join product
            on sale.product_id = product.id
            and '2010-09-26T02:06:34' < sale.time and sale.time < '2010-09-29T02:06:34'
        """)

    for _ in tqdm(
            range(EXEC_NUMBER),
            desc='Вивести топ 10 купівель товарів по два за період С (покупка >= 2 товари)'
    ):
        f(f"""
            select s1.product_id, s2.product_id, count(*) as c
            from sale as s1
            inner join sale as s2
            on s1.id = s2.id
            and s1.product_id < s2.product_id
            where '2010-09-26T02:06:34' < s1.time and s1.time < '2010-09-29T02:06:34'
            group by s1.product_id, s2.product_id
            order by c desc
            limit 10
        """)

    for _ in tqdm(
            range(EXEC_NUMBER),
            desc='Вивести топ 10 купівель товарів по два за період С (покупка == 2 товари)'
    ):
        f(f"""
            select l, count(*) as c
            from (
                select array_agg(product_id order by product_id) as l
                from sale
                where '2010-09-26T02:06:34' < sale.time and sale.time < '2010-09-29T02:06:34'
                group by id
                having count(product_id) = 2
            ) as tmp
            group by l
            order by c desc
            limit 10
        """)

    for _ in tqdm(
            range(EXEC_NUMBER),
            desc='Вивести топ 10 купівель товарів по два за період С (покупка == 2 товари v2)'
    ):
        f(f"""
            select s1.product_id, s2.product_id, count(*) as c
            from (select *, count(s0.product_id) over (partition by s0.id) as c0 from sale as s0) as s1
            inner join sale as s2
            on c0 = 2
            and s1.id = s2.id 
            and s1.product_id < s2.product_id
            where '2010-09-26T02:06:34' < s1.time and s1.time < '2010-09-29T02:06:34'
            group by s1.product_id, s2.product_id
            order by c desc
            limit 10  
        """)
