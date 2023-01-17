#! /usr/local/bin/python3.11
from datetime import datetime


# import psycopg2
import argparse

# import mysql.connector
import psycopg2
# from mysql.connector import Error
# from mysql.connector import errorcode
from config import get_config


def transfer(amnt:int, from_account:int, to_account:int):
    params = get_config()
    conn = psycopg2.connect(**params)
    data = None


    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            #checking if there's enough credit:
            cur.execute(f"select balance + max_limit from accounts a where id = {from_account}")
            myresult = cur.fetchone()
            print(myresult)
            balance_and_credit_limit = int(myresult[0])
            if balance_and_credit_limit < int(amnt):
                raise Exception('not enough credit')

            else:
                cur.execute(f"insert into transactions (t_type, amount, t_timestamp, sender, resiver) VALUES ('transfer', {amnt}, '{datetime.now()}',{from_account},{to_account})")
                cur.execute(f"update accounts set balance = balance - {amnt} where id={from_account}")
                cur.execute(f" update accounts set balance = balance + {amnt} where id={to_account}")
                print("Database Updated !")

    if conn is not None:
        conn.close()
        print('db connection closed')


# a = transfer(30,4,5)
# print(a)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # parser.add_argument('-t', '--transfer')
    parser.add_argument('-a', '--amnt')
    parser.add_argument('-f', '--from_account')
    parser.add_argument('-t', '--to_account')

    args = parser.parse_args()

    amnt = args.amnt
    from_account = args.from_account
    to_account = args.to_account

    print(args.amnt, args.from_account, args.to_account)
try:
    a = transfer(amnt, from_account,to_account)
except Exception as e:
    print(str(e))