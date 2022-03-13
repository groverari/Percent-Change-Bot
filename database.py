import psycopg2
from psycopg2 import *
import os
from dotenv import load_dotenv

load_dotenv()
class Database:

    @staticmethod
    def connect():
        conn = psycopg2.connect(
            host = os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD")
        )