from flask import Flask, request, jsonify
import sqlite3
from email_handler import send_email
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        data = request.json
        print("📩 Recibido:", data)

        # Limpieza de datos
        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        email = data.get("email", "").strip()
        message = data.get("message", "").strip()

        # Validación de datos
        if not all([name, phone, email, message]):
            return jsonify({"success": False, "error": "Todos los campos son obligatorios"}), 400

        # Guardar en la base de datos
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO barber_appointments (name, phone, email, message)
                VALUES (?, ?, ?, ?)
            """, (name, phone, email, message))
            conn.commit()

        # Enviar correo
        send_email(name, phone, email, message)

        print("✅ Datos guardados y correo enviado con éxito.")
        return jsonify({"success": True, "message": "Formulario enviado correctamente"}), 201

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"success": False, "error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


