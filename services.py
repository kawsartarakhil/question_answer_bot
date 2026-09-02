from connections import get_connection


async def register(username,tg_id):
    conn=await get_connection()
    try:
        user=await conn.fetchrow("""
        select * from users
        where username=$1 and tg_id=$2
        """,username,str(tg_id))
        if user:
            print("user already exists")
        else:
            user=await conn.execute("""
        insert into users(username,tg_id,is_admin)
        values
        ($1,$2,False)
        """,username,str(tg_id))
            return user
    except Exception as er:
        print("registeration error:",er)

    finally:
        await conn.close()

    

async def get_user(username):
    conn=await get_connection()
    try:
        user=await conn.fetchrow("""
        select * from users 
        where username=$1
        """,username)
        return user
    except Exception as er:
        print("get user error:",er)
    finally:
        await conn.close()

async def add_question(question,answer):
    conn=await get_connection()
    try:
        await conn.execute("""
        insert into questions(question,answer)
        values
        ($1,$2)
        """,question,answer)
    except Exception as er:
        print("Add quetion error:",er)

    finally:
        await conn.close()

async def get_quetions(tg_id):
    conn=await get_connection()
    try:
        quetions=await conn.fetch("""
        select question from quetions
        where tg_id=$1
        """,str(tg_id))
        return quetions
    except Exception as er:
        print("Get questions error:",er)
    finally:
        await conn.close()

async def edit_question(q_id):
    conn=await get_connection()
    try:
        question=await conn.fetchrow("""
        select * from questions
        where id=$1
        """,q_id)
        if not question:
            print("Question dosen't exists")
        else:
            question=await conn.execute("""

    
            """)



 