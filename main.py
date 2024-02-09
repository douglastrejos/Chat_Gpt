import os

from openai import OpenAI

from configparser import ConfigParser

config = ConfigParser()

config.read("config_file.ini")

config_data = config["DEFAULT"]

client = OpenAI(
    api_key= str(config_data['api_key'])
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