import asyncio
import os
import openai
import json
from flask import Flask, render_template, request, jsonify
from applicationinsights.flask.ext import AppInsights
from bs4 import BeautifulSoup
from services.classes import *
from services.builder import *
from services.html_format import *
from services.utils import *


# Define AzureOpenAI environment variables
client = openai.AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

# Define generator function
async def completionGPT(client: openai.AzureOpenAI, messages: str, temperature: float, top_p: float) -> str:
    for sleep_time in [1 for i in range(1,11)] + [0]:
        try:
            completion = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
                messages=messages,
                top_p=top_p,
                temperature=temperature
            )
            # completion = await completion
            result = completion.choices[0].message.content
            
            usage = completion.usage
            prompt_tokens = usage.prompt_tokens
            completion_tokens = usage.completion_tokens
            total_tokens = usage.total_tokens
            
            # Define the cost per 1000 tokens
            cost_per_1000_tokens_prompt = 0.003 
            cost_per_1000_tokens_completion = 0.006
        
            # Calculate the total cost
            total_cost = (prompt_tokens / 1000) * cost_per_1000_tokens_prompt + (completion_tokens / 1000) * cost_per_1000_tokens_completion
            
        except:
            result = None
            total_cost = 0 
            
        if result:
            return {
                'result': result,
                'cost': total_cost,
                'prompt_tokens': prompt_tokens,
                'completion_tokens': completion_tokens,
                'total_tokens': total_tokens,
                'completion': completion
            }
        
        
        elif sleep_time:
            await asyncio.sleep(sleep_time)
        else:
            return {
                'result': 'error',
                'cost': 0,
                'prompt_tokens': 0,
                'completion_tokens': 0,
                'total_tokens': 0
            }

# Read the standard templates for Job description generation
with open('static/standards/email_short.txt', encoding='UTF-8') as f:
    template_email_short = f.read()
with open('static/standards/email_long.txt', encoding='UTF-8') as f:
    template_email_long = f.read()
with open('static/standards/linkedin_short.txt', encoding='UTF-8') as f:
    template_linkedin_short = f.read()
with open('static/standards/linkedIn_long.txt', encoding='UTF-8') as f:
    template_linkedin_long = f.read()
with open('static/standards/multiposting.txt', encoding='UTF-8') as f:
    template_multiposting = f.read()

# Start application 
app = Flask(__name__)
app.config['DEBUG'] = True

# Create empty list to store versions of generations
version_history = []

# Get main template
@app.route('/', methods=['GET'])
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/jpp', methods=['GET'])
def jpp_input():
    return render_template('JPP - Input.html',
                           template_email_short=template_email_short,
                           template_email_long=template_email_long,
                           template_multiposting=template_multiposting,
                           template_linkedin_short=template_linkedin_short,
                           template_linkedin_long=template_linkedin_long)

# Render and generate job advert
@app.route('/generate', methods=['GET', 'POST'])
async def jpp_generator():
    # Request all inputed parameters
    business_unit = request.form.get('business_unit')
    template_structure = request.form.get('template_structure')
    template_name = request.form.get('template_name')
    emojis = request.form.get('emojis')
    tone = request.form.get('tone')
    language = request.form.get('language')
    client_sector = request.form.get('client_sector')
    client_url = request.form.get('client_url')
    skills = request.form.get('skills')
    driving_license = request.form.get('driving_license')
    vehicle = request.form.get('vehicle')
    work_type = request.form.get('work_type')
    profession = request.form.get('profession')
    city = request.form.get('city')
    province = request.form.get('province')
    min_pay = request.form.get('min_pay')
    max_pay = request.form.get('max_pay')
    benefits_storage = request.form.get('benefits_storage')
    contract_type = request.form.get('contract_type')
    schedule = request.form.get('schedule')
    work_rate = request.form.get('work_rate')
    num_employees = request.form.get('num_employees')
    freq_pay = request.form.get('freq_pay')
    bonus = request.form.get('bonus')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    # Adjust parameters
    if bonus is None: bonus = ''
    city_cap = city.capitalize()
    client_sector_low = client_sector.lower()
    profession_low = profession.lower()
    benefits_low = benefits_storage.lower()

    # Initialize all generation classes
    gen_details = GenerationDetails(
        business_unit=business_unit,
        template_name=template_name,
        template_structure=template_structure,
        emojis=emojis,
        tone=tone,
        language=language
    )

    client_params = ClientParams(
        client_sector=client_sector_low,
        client_url=client_url
    )

    job_params = JobParams(
        profession=profession_low,
        city=city_cap,
        province=province,
        min_pay=min_pay,
        max_pay=max_pay,
        freq_pay=freq_pay,
        bonus=bonus,
        benefits=benefits_low,
        contract_type=contract_type,
        work_rate=work_rate,
        num_employees=num_employees,
        start_date=start_date,
        end_date=end_date,
        schedule=schedule
    )
    
    req_params = ReqParams(
        skills=skills,
        driving_license=driving_license,
        vehicle=vehicle,
        work_type=work_type
    )
    
    # Build the system and user prompts
    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(gen_details, client_params, job_params, req_params)
    
    print(user_prompt)

    # Generate the job description
    messages = [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
    response = await completionGPT(client, messages, temperature=0.5, top_p=0.9)
    
    print(response)
    result = response['result']
    cost = response['cost']
    prompt_tokens = response['prompt_tokens']
    completion_tokens = response['completion_tokens']
    total_tokens = response['total_tokens']
    print(f"Coste: ${cost:.6f}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Resultado tokens: {completion_tokens}")
    print(f"Total tokens: {total_tokens}")
    print(20*'-')
    print(result)
    if result == 'error':
        return render_template('error.html')
    
    if gen_details.template_name not in ['email_short', 'email_long'] and gen_details.business_unit == 'LHH':
        result = LHH_format(result)
    
    if gen_details.business_unit == 'Fundación':
        result = fundacion_format(result)
    
    print(result)
    # Convert result to html
    chat_response = convert_string_to_html(result)
    
    return render_template(
        'JPP - Input.html',
        chat_response=chat_response,
        business_unit=business_unit,
        template_name=template_name,
        template_structure=template_structure,
        emojis=emojis,
        tone=tone,
        language=language,
        client_sector=client_sector,
        client_url=client_url,
        profession=profession,
        city=city,
        province=province,
        min_pay=min_pay,
        max_pay=max_pay,
        freq_pay=freq_pay,
        bonus=bonus,
        benefits_storage=benefits_storage,
        contract_type=contract_type,
        work_rate=work_rate,
        num_employees=num_employees,
        start_date=start_date,
        end_date=end_date,
        schedule=schedule,
        skills=skills,
        driving_license=driving_license,
        vehicle=vehicle,
        work_type=work_type,
        template_email_short=template_email_short,
        template_email_long=template_email_long,
        template_multiposting=template_multiposting,
        template_linkedin_short=template_linkedin_short,
        template_linkedin_long=template_linkedin_long
    )  

@app.route('/generate_summary', methods=['POST'])
async def generate_summary():
    
    data = request.json
    chat_response = data.get('chat_response', '')

    # if chat_response:
    #     # Use BeautifulSoup to parse HTML and extract text
    #     soup = BeautifulSoup(chat_response, 'html.parser')
    #     text_content = soup.get_text(separator=' ')
    
    # Generate the summary job description
    user_prompt = summarise_prompt(chat_response)
    system_prompt = 'Eres una agencia de empleo mensajeando a un candidato sobre un puesto de trabajo.'
    
    messages = [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
    response = await completionGPT(client, messages, temperature=0.5, top_p=0.7)

    result = response['result']
    result = convert_string_to_html(result)
    
    return jsonify({'summary' : result})


@app.route('/generate_questions', methods=['POST'])
async def generate_questions():
    data = request.json
    chat_response = data.get('chat_response', '')
    selected_option = data.get('inlineRadioOptions2')
    questions_topic = data.get('questions_topic', '')

    if chat_response:
        # Use BeautifulSoup to parse HTML and extract text
        soup = BeautifulSoup(chat_response, 'html.parser')
        text_content = soup.get_text(separator=' ')

    num_questions = 10  # Default
    if selected_option == 'few_questions':
        num_questions = 3
    elif selected_option == 'some_questions':
        num_questions = 5
    elif selected_option == 'many_questions':
        num_questions = 10

    user_prompt = generate_question_prompt(text_content, num_questions, questions_topic)
    print(user_prompt)
    system_prompt = 'Eres una agencia de empleo creando una lista de preguntas un candidato sobre una oferta de trabajo para enviar a un candidato.'
    
    messages = [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
    response = await completionGPT(client, messages, temperature=0.5, top_p=0.8)
    
    questions = response['result']

    questions = questions.replace('\n', '<br>')
    questions = questions.replace('I can\'t generate questions and try again.', '')

    return jsonify({'questions': questions})



# Run application
if __name__ == '__main__':
    asyncio.run(app.run())
