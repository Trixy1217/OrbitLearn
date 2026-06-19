from src.database.connection import get_connection

def create_player(name, player_class):
    connection = None


    try:
            connection = get_connection()

            connection.execute(
                """
            INSERT INTO players(name,class)
            VALUES (?,?)
        """, (name,player_class)
            )

            connection.commit()
            connection.close()

            return True
    except Exception as e:
        
        print(e)
        return False
    finally:
        if connection:
            connection.close()
        
    

    
def get_player(player_id):

    connection = get_connection()

    cursor = connection.execute("""
       SELECT * FROM players WHERE id = ?



""",(player_id,) )
    
    player = cursor.fetchone()
    connection.close()
    return player


def get_id_player_with_nickname(nickname):

    connection = get_connection()

    cursor = connection.execute("""
       SELECT id FROM players WHERE name = ?



""",(nickname,) )
    
    player = cursor.fetchone()
    connection.close()
    return player[0] if player else None

def delete_player(player_id):

    connection = get_connection()

    cursor = connection.execute(
        """
      SELECT * FROM players where id = ?
""", (player_id,)
    )

    player = cursor.fetchone()
    connection.close()
    return player

