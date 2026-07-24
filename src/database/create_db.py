import sqlite3


connection = sqlite3.connect("data/game.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    openId TEXT UNIQUE,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    loginMethod TEXT,
    role TEXT NOT NULL DEFAULT 'student'
        CHECK (role IN ('student', 'admin')),
    learningStyle TEXT
        CHECK (learningStyle IN ('visual', 'auditory', 'kinesthetic', 'mixed')),
    createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    class TEXT NOT NULL,
    lastSignedIn TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL UNIQUE,
    estiloAprendizaje TEXT,
    nivelFrustracion INTEGER NOT NULL DEFAULT 0 CHECK (nivelFrustracion >= 0),
    nivelComprension INTEGER NOT NULL DEFAULT 0 CHECK (nivelComprension >= 0),
    sesionesCompletadas INTEGER NOT NULL DEFAULT 0 CHECK (sesionesCompletadas >= 0),
    createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES users(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS roadmaps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    temas JSON,
    temaActual TEXT,
    progreso INTEGER NOT NULL DEFAULT 0 CHECK (progreso BETWEEN 0 AND 100),
    activo INTEGER NOT NULL DEFAULT 1 CHECK (activo IN (0, 1)),
    createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentId) REFERENCES students(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS gamificationProgress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER NOT NULL,
    puntosXp INTEGER NOT NULL DEFAULT 0 CHECK (puntosXp >= 0),
    rachaDias INTEGER NOT NULL DEFAULT 0 CHECK (rachaDias >= 0),
    insignias JSON,
    createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentId) REFERENCES students(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sessionHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER NOT NULL,
    mensajeUsuario TEXT NOT NULL,
    respuestaTutor TEXT NOT NULL,
    explicacionDecision TEXT,
    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentId) REFERENCES students(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS activePauses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER NOT NULL,
    tiempoEstudio INTEGER NOT NULL DEFAULT 0 CHECK (tiempoEstudio >= 0),
    tipoDescanso TEXT NOT NULL,
    completado INTEGER NOT NULL DEFAULT 0 CHECK (completado IN (0, 1)),
    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentId) REFERENCES students(id) ON DELETE CASCADE
)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_students_userId ON students(userId)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_roadmaps_studentId ON roadmaps(studentId)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_gamificationProgress_studentId ON gamificationProgress(studentId)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessionHistory_studentId ON sessionHistory(studentId)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_activePauses_studentId ON activePauses(studentId)")

connection.commit()
connection.close()
