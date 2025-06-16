from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/bot", methods=["POST"])
def bot():
    user_input = request.form.get("Body", "")
    system_prompt = (
        "Você é o Radar Reforma Tributária, um agente especialista na LC 214/2025, "
        "notas técnicas da NF-e e obrigações fiscais. Explique de forma clara, objetiva "
        "e profissional para usuários do setor fiscal."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        bot_reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        print("ERRO AO CHAMAR OPENAI:", e)
        bot_reply = "Erro ao consultar a IA. Verifique a chave da OpenAI ou os logs."

    twilio_response = MessagingResponse()
    twilio_response.message(bot_reply)
    return str(twilio_response)

if __name__ == "__main__":
    app.run()