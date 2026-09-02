from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

async def get_connection():
    try:
        user=await asyncpg.connect(
            host="localhost",
            user="postgres",
            database="game_db",
            password=os.getenv("SQL_PASSWORD"),
            port=5432
        )
        return user
    except Exception as er:
        print("connection error:",er)

async def init_tables():
    conn=await get_connection()
    try:
        await conn.execute("""
        create table if not exists users(
        id serial primary key,
        username varchar(50),
        tg_id varchar,
        is_admin boolean default false
        );

        create table if not exists quetions(
        id serial primary key,
        question varchar,
        answer varchar,
        user_id int references users(id)
        );
        """)
        print("tables created")

    except Exception as er:
        print("initailazation error:",er)

    finally:
        await conn.close()