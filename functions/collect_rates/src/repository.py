import datetime
import os

import psycopg2
from src.constants import RATES_TABLENAME
from src.environment import (
    DATABASE_SCHEMA,
    DB_DATABASE,
    DB_HOST,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
)
from src.schema import RatesSchema, RepositoryRatesSchema

# QUERIES
INSERT_QUERY = f"""
    INSERT INTO "{DATABASE_SCHEMA}"."{RATES_TABLENAME}" 
    (rate_code, value, date, is_actual, created_at, nominal)
     VALUES (%(code)s, %(value)s, %(date)s, TRUE, %(created_at)s, %(nominal)s)
"""

UPDATE_QUERY = f"""
    UPDATE "{DATABASE_SCHEMA}"."{RATES_TABLENAME}" 
    SET is_actual = FALSE
    WHERE id in %(ids)s
 """

SELECT_QUERY = f"""
    SELECT id, rate_code, value, date, nominal
    FROM "{DATABASE_SCHEMA}"."{RATES_TABLENAME}"
    WHERE date = %(date)s AND is_actual IS TRUE
 """


# conn =
def get_connection():
    return psycopg2.connect(
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )


class Repository:
    def __init__(self, connection):
        self.connection = connection

    def get_rates(self, date: datetime.date) -> list[RepositoryRatesSchema]:
        cur = self.connection.cursor()
        cur.execute(SELECT_QUERY, {"date": date})
        return [
            RepositoryRatesSchema(
                id=row[0],
                rate_code=row[1],
                value=row[2],
                date=row[3],
                nominal=row[4],
            )
            for row in cur.fetchall()
        ]

    def update_old_volutes(self, volutes_ids: list[int]) -> None:
        cur = self.connection.cursor()
        cur.execute(UPDATE_QUERY, {"ids": tuple(volutes_ids)})

    def save_rates(self, rates: list[RatesSchema], date: datetime.date) -> None:
        cur = self.connection.cursor()
        for rate in rates:
            cur.execute(
                INSERT_QUERY,
                {
                    "code": rate.rate_code,
                    "value": rate.value,
                    "date": date,
                    "created_at": datetime.datetime.utcnow(),
                    "nominal": rate.nominal,
                },
            )
