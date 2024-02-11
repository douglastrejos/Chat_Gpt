import openai

import os

from configparser import ConfigParser

config = ConfigParser()

config.read("config_file.ini")

config_data = config["DEFAULT"]

openai.api_key = str(config_data['api_key'])

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"user",
            "content":"dame una lista de proyectos en Python"    
        },        
    ],
    stream=True,
    max_tokens=50
)

#print(response.choices[0].message.content)

collected_message = []

for chunk in response:
    chunk_message = chunk.choices[0].delta.content #.content
    collected_message.append(chunk_message)
    print(collected_message)