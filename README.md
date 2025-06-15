# Bot de WhatsApp - Radar Reforma Tributária

Este projeto conecta o WhatsApp (via Twilio) com um agente GPT-4 especializado na Reforma Tributária, utilizando Flask + OpenAI + Render para deploy.

## Como funciona
- O Twilio envia mensagens recebidas via webhook
- O Flask trata essas mensagens e envia para o GPT-4
- O GPT responde como especialista em reforma tributária

## Deploy
- Configure o Render com:
  - Build command: pip install -r requirements.txt
  - Start command: gunicorn chatbot_whatsapp_reforma:app
  - Python 3.11
  - Variável de ambiente: OPENAI_API_KEY