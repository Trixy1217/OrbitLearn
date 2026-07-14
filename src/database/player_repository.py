from src.database.connection import get_connection

def create_player(name,password, player_class):
    connection = None


    try:
            connection = get_connection()

            connection.execute(
                """
            INSERT INTO players(name,pass,class)
            VALUES (?,?,?)
        """, (name,password,player_class)
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
        
    

def set_learning_style(player_id, learning_style):
    connection = None

    try:
        connection = get_connection()

        connection.execute(
            """
            UPDATE players
            SET learning_style = ?
            WHERE id = ?
            """,
            (learning_style, player_id)
        )

        connection.commit()
        return True

    except Exception as e:
        print(e)
        return False

    finally:
        if connection:
            connection.close()
    
def get_player(player_id):

    connection = get_connection()

    try:
            cursor = connection.execute("""
            SELECT * FROM players WHERE id = ?



            """,(player_id,) )
            
            player = cursor.fetchone()
            connection.close()
            return player ##ESO RETRONA TUPLA CAMBIAR A DICCIONARIO LUEGO el codigoe sta aabajo

            """def get_player(player_id):
            connection = get_connection()

            cursor = connection.execute("""
            ### SELECT * FROM players WHERE id = ?
            """, (player_id,))

                row = cursor.fetchone()
                connection.close()

                if row is None:
                    return None

                return {
                    "id": row[0],
                    "nombre": row[1],
                    "contraseña": row[2]
                    "clase": row[3]
                }"""
            

    except Exception as e:
         
             return print(f"Ha ocurrido un error seguramente el usuario no se encontró: {e}")
    finally:
         if connection:
          connection.close()


def get_player_with_nickcname(name):

    connection = get_connection()

    try:
            cursor = connection.execute("""
            SELECT * FROM players WHERE name = ?



            """,(name,) )
            
            player = cursor.fetchone()
            connection.close()
            return player ##ESO RETRONA TUPLA CAMBIAR A DICCIONARIO LUEGO el codigoe sta aabajo

            """def get_player(player_id):
            connection = get_connection()

            cursor = connection.execute("""
            ### SELECT * FROM players WHERE id = ?
            """, (player_id,))

                row = cursor.fetchone()
                connection.close()

                if row is None:
                    return None

                return {
                    "id": row[0],
                    "nombre": row[1],
                    "contraseña": row[2]
                    "clase": row[3]
                }"""
            

    except Exception as e:
         
             return print(f"Ha ocurrido un error seguramente el usuario no se encontró: {e}")
    finally:
         if connection:
          connection.close()


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

