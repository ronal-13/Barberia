import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "ronalasencio13@gmail.com"
EMAIL_PASSWORD = "uxkw aqan ovkw evqo"
EMAIL_RECEIVER = "ronalasencio06@gmail.com"

def send_email(name, phone, email, message):
    try:
        subject = "🔔 RESERVA IMPORTANTE - Cliente en espera | Barbería ALOJAN"
        body = f"""
        🔔 ¡NUEVA SOLICITUD DE RESERVA!

        Detalles del cliente:

        👤 Nombre: {name}
        📞 Teléfono: {phone}
        📧 Correo electrónico: {email}

        📝 Mensaje o indicaciones especiales:
        {message}

        ✅ Revisa tu agenda y responde lo antes posible para confirmar esta reserva.

        💈 Este mensaje fue generado automáticamente desde tu sitio web ALOJAN-MASTER.
        """

        msg = MIMEMultipart()
        msg["From"] = f"Barbería ALOJAN <{EMAIL_SENDER}>"
        msg["To"] = f"Barbería ALOJAN <{EMAIL_RECEIVER}>"
        msg["Subject"] = subject
        msg["X-Priority"] = "1"  # Alta prioridad

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        print("✅ Correo enviado correctamente.")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
