import os

if os.path.exists("game.db"):
    os.remove("game.db")
    print("Base de datos eliminada.")
else:
    print("La base de datos no existe.")