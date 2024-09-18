import os
from openai import AsyncAzureOpenAI
from services.classes import *
from services.builder import *
import asyncio
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import streamlit as st

# Carga las variables del archivo .env
load_dotenv()

version_history = []

with open('static/standards/LinkedIn_Template.txt', encoding='UTF-8') as f:
    template_linkedin = f.read()

with open('static/standards/Whatsapp_Template.txt', encoding='UTF-8') as f:
    template_whatsapp = f.read()

# Initial params to test
gen_details = GenerationDetails(
    tone="informal",
    language="español",
    emojis=True,
    template=None,
    business_unit=None
)

client_params = ClientParams(
    client_sector="obras y construcción",
    client_url='https://www.estudio3arquitectos.com/',
)

job_params = JobParams(
    profession="arquitecto",
    city="Bilbao",
    contract_type="permanente",
    min_pay=None,
    max_pay=str(34000),
    freq_pay="año",
    bonus=str(3000),
    num_employees=str(3),
    benefits=['teletrabajo, ticket restaurante, seguro médico'],
    work_rate="completa",
    fill_skills=False,
    skills="conocimientos avanzados de diseño y física de materiales, 3 años de experiencia, habilidad para el trabajo manual."
)



api_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
api_version = os.environ["AZURE_OPENAI_API_VERSION"] 

client = AsyncAzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version
    )


async def call_gpt(client: AsyncAzureOpenAI, messages: str, temperature: float, top_p: float) -> str:
    
    try:
        completion = await client.chat.completions.create(
            model='gpt-35-turbo-0301',
            messages=messages,
            temperature=temperature,
            top_p=top_p
        )
        return completion.choices[0].message.content
    except Exception as ex:
        print(ex)
        return None
    
async def generate(client):
    
    system_prompt = build_system_prompt('a')
    user_prompt = build_user_prompt(gen_details, client_params, job_params)

    version = {
        'gen_details' : gen_details,
        'client_params' : client_params,
        'job_params' : job_params,
        'user_prompt' : user_prompt
    }
    
    print(f'PROMPT:\n {user_prompt} \n\n')
    
    messages = [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
    result = await call_gpt(client, messages, 0.5, 0.8)
    version['result'] = result
    version_history.append(version)


    return st.html(result)

if __name__ == '__main__':
    async def main():
        result = await generate(client)
        print('--------------------------------------- \n--------------------------------------- \n        RESULTADO  \n--------------------------------------- \n---------------------------------------')
        print(result)
        print('--------------------------------------- \n--------------------------------------- \n        historial  \n--------------------------------------- \n---------------------------------------')
        print(version_history)
    
    asyncio.run(main())
    
    
## This is just a random comment
## New comment