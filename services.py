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
            await conn.execute("""
        insert into users(username,tg_id,is_admin)
        values
        ($1,$2,False)
        """,username,str(tg_id))
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

async def add_question(question,answer,user_id):
    conn=await get_connection()
    try:
        await conn.execute("""
        insert into questions(question,answer,user_id)
        values
        ($1,$2,$3)
        """,question,answer,user_id)
    except Exception as er:
        print("Add quetion error:",er)

    finally:
        await conn.close()

async def get_user_quetions(user_id):
    conn=await get_connection()
    try:
        quetions=await conn.fetch("""
        select question from questions
        where user_id=$1
        """,user_id)
        return quetions
    except Exception as er:
        print("Get questions error:",er)
    finally:
        await conn.close()




 