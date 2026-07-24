from src.database.connection import get_connection
import bcrypt


def create_user(
    name,
    password,
    email,
    login_method,
    role,
    clase,
    last_signed_in=None
):
    connection = None
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"), bcrypt.gensalt()
    ).decode()

    try:
        connection = get_connection()
        connection.execute(
            """
            INSERT INTO users(
                name,
                password,
                email,
                loginMethod,
                role,
                class,
                lastSignedIn
            )
            VALUES (?, ?, ?, ?, ?, ?,?)
            """,
            (
                name,
                hashed_password,
                email,
                login_method,
                role,
                clase,
                last_signed_in,
            ),
        )
        connection.commit()
        return True
    except Exception as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def set_learning_style(user_id, learning_style, tdah_option):
    connection = None

    try:
        connection = get_connection()
        connection.execute(
            """
            UPDATE users
            SET learningStyle = ?
            WHERE id = ?
            """,
            (learning_style, user_id),
        )
        connection.commit()
        return True
    except Exception as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def get_user(user_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        )
        return cursor.fetchone()
    except Exception as error:
        print(f"No se encontró el usuario: {error}")
        return None
    finally:
        connection.close()


def get_user_by_name(name):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM users WHERE name = ?", (name,)
        )
        return cursor.fetchone()
    except Exception as error:
        print(f"No se encontró el usuario: {error}")
        return None
    finally:
        connection.close()


def get_user_id_by_name(name):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT id FROM users WHERE name = ?", (name,)
        )
        user = cursor.fetchone()
        return user[0] if user else None
    finally:
        connection.close()


def delete_user(user_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        )
        return cursor.fetchone()
    finally:
        connection.close()


def login_user(name, password):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT password FROM users WHERE name = ?", (name,)
        )
        user = cursor.fetchone()

        if user is None:
            return False

        return bcrypt.checkpw(password.encode(), user[0].encode())
    except Exception as error:
        print(f"Login error: {error}")
        return False
    finally:
        connection.close()


# Alias temporales para que las páginas actuales sigan funcionando mientras
# se actualizan gradualmente sus importaciones al vocabulario de users.
create_player = create_user
get_player = get_user
get_player_with_nickcname = get_user_by_name
get_id_player_with_nickname = get_user_id_by_name
delete_player = delete_user
