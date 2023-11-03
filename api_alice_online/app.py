import openai

# Configure sua chave de API do OpenAI
openai.api_key = "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"

def obter_resposta_conversa(conversa):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use o modelo apropriado
            messages=conversa,
            max_tokens=2000
        )

        return resposta.choices[0].message["content"]
    except Exception as e:
        return str(e)

# Exemplo de uso
conversa = [
    {"role": "system", "content": "Você é um assistente de chat."},
    {"role": "user", "content": "Quem foi albert einstein?"}
]

resposta = obter_resposta_conversa(conversa)
print(resposta)