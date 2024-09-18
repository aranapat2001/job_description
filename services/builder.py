### BUILDS INPUT PROMPTS: user and system prompt ###

from services.classes import *
from services.prompt_definitions import *

def build_system_prompt() -> str:
    """
    Builds the role prompt passed to the system.
    """
    role_prompt = f'Eres un reclutador de una agencia de empleo escribiendo una oferta de trabajo. \
                    Después de generar la oferta de trabajo, asegúrate de que los pronombres utilizados reflejen a la organización de la empresa cliente del reclutador y no a la agencia de empleo del reclutador. Cuando sea apropiado, usa "su", "ellos", "su equipo" para referirte a la organización de la empresa cliente. No repitas la misma información en el anuncio de trabajo.'
    return role_prompt


def build_user_prompt(gen_details: GenerationDetails,
                      client_params: ClientParams,
                      job_params: JobParams,
                      req_params: ReqParams) -> str:
    """
    Builds the user prompt passed to the system to generate the job description.
    """
    user_prompt = f'Como reclutador de una agencia de empleo, escribe con lenguaje inclusivo un anuncio'
    user_prompt += f' de una oferta de trabajo de {job_params.profession} para una empresa. Incluye la siguiente información solo una vez durante la redacción de la oferta:'
    user_prompt += f'\n'
    content, name, _ = define_client_prompt(client_params)
    user_prompt += content
    user_prompt += f'\n'
    user_prompt += define_job_prompt(job_params, req_params)
    if gen_details.template_name != 'email_short':
        user_prompt += define_benefits_prompt(job_params)
    user_prompt += f'\n'
    user_prompt += define_format_prompt(gen_details)
    user_prompt += '\nUSA LENGUAJE INCLUSIVO. Ejemplo: el/la candidato/a. '
    user_prompt += 'Es muy importante que no uses dos puntos para iniciar una lista, usa en vez una coma. Ejemplo: entre las funciones se incluyen, [lista de funciones]. '
    user_prompt += 'Acaba la oferta sin mencionar ninguna fecha y usando pronombres que hagan referencia a la organización del cliente, como "su", "ellos" o "su equipo". Ejemplo: si la oferta es de tu interés, contacta y unéte a su empresa. '
    user_prompt += 'Las siguientes palabras están prohibidas de usar en la oferta:'
    user_prompt += '\nagencia'
    user_prompt += '\nCV'
    user_prompt += '\ncurrículum'
    if name: user_prompt += f'\n{name}'
    return user_prompt


def summarise_prompt(text: str) -> str:
    """
    Builds the user prompt passed to the system to generate the summary.
    """
    user_prompt = 'Resume de forma muy breve la siguiente oferta de trabajo que será enviada a un candidato. Escríbela de manera atractiva y original.'
    user_prompt += '\n' + text
    return user_prompt


def generate_question_prompt(text: str, 
                             num_questions: int,
                             questions_topic: str) -> str:
    """
    Builds the user prompt passed to the system to generate the questions related to a topic.
    """
    if questions_topic.strip() != '': questions_topic = 'de ' + questions_topic.lower()
    user_prompt = f'Crea una lista de preguntas muy originales, díficiles y muy específicas {questions_topic} para una entrevista del candidato basada en la siguiente oferta de trabajo:'
    user_prompt += '\n' + text
    user_prompt += f'\nEl número de preguntas debe ser exactamente {num_questions}.'
    return user_prompt
