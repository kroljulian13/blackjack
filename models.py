# coding=utf-8
import datetime
from peewee import *

DATABASE = SqliteDatabase('blackjack.db')


class Results(Model):
    timestamp = DateTimeField( default = datetime.datetime.now)
    balance = CharField()
    strategy = CharField()
    total_win = CharField()
    numberOfPlays = CharField()
    userNick = CharField( default="annonymous")

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Results], safe=True)
    DATABASE.close()