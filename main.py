import os

from openai import OpenAI

client = OpenAI(
    api_key= "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"
)

respuesta = "s"

while respuesta.upper() == "S":
    os.system('cls')
    prompt = input('Que deseas saber: ')
    chat_completation = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        model="gpt-3.5-turbo"
    )
    print(chat_completation.choices[0].message.content)
    respuesta = input('Quieres seguir aprendiendo S/N?')
print("Hasta la proxima")