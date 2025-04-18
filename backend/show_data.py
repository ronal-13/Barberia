import sqlite3

def show_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM barber_appointments")
    rows = cursor.fetchall()

    if rows:
        print("📋 Reservas registradas:")
        for row in rows:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Teléfono: {row[2]}, Email: {row[3]}, Mensaje: {row[4]}")
    else:
        print("⚠️ No hay reservas registradas.")

    conn.close()

if __name__ == "__main__":
    show_data()
