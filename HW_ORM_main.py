import json
import os
import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from HW_ORM_models import create_tables, Publisher, Shop, Book, Stock, Sale

Password_bd = os.getenv('Password_bd')

DSN = f'postgresql://postgres:{Password_bd}@localhost:5432/netology'
engine = sqlalchemy.create_engine(DSN)


# создание таблиц
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


# заполнение данными

# with open('fixtures/tests_data.json', 'r') as fd:
#     data = json.load(fd)
#
# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()


# выборкаданных
# autor_name = input('Введите имя автора')
autor_name = 'Pearson'


def sale_book(autor):
#     q = session.query(Publisher).all()
#     q = session.query(Publisher).filter(Publisher.name == autor)
#     q = session.query(Publisher.name, Book.title).join(Book.publisher).filter(Publisher.name == autor_name).all()
    q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Book.publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == autor_name).all()
    for r in q:
        print(r)
        res = f'{r[0]} | {r[1]} | {r[2]} | {r[3]}'
        print (res)
        # print([r[0]] + [r[1]] + [str(r[2])] + [str(r[3])])


sale_book(autor_name)



session.close()


# С помощью list comprehension . Больше будет для вывода нескольких списков (книг).
# print([[r[0]] + [r[1]] + [str(r[2])] + [str(r[3])] for s in selected.all()])
