from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# ✅ Suas credenciais do Twilio – (ok, mas nunca subir isso em um repositório público)
TWILIO_SID = 'SEU_SID'
TWILIO_TOKEN = 'SEU_AUTH_TOKEN'
FROM_WA = 'whatsapp:+14155238886'  # ✅ Número da sandbox do Twilio (fixo)

# ✅ Criação do cliente Twilio
client = Client(TWILIO_SID, TWILIO_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    # ✅ Captura de dados da mensagem recebida
    data = request.form
    msg_recebida = data.get('Body')
    numero = data.get('From')  # número do remetente (quem mandou msg)

    print(f"[Usuário] {numero}: {msg_recebida}")

    # ✅ Aqui respondemos de volta para quem enviou (não use número fixo)
    client.messages.create(
        from_=FROM_WA,
        to=numero,  # envia para o mesmo que mandou
        body='Recebemos sua mensagem! Em breve um atendente entrará em contato.',
    )

    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
