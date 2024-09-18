from services.classes import *
from services.utils import *
import asyncio

def define_format_prompt(gen_details: GenerationDetails) -> str:
    """
    Generates the style prompt for the job description.

    Args:
        gen_details (GenerationDetails): Parameters containing details of the generation style and format.

    Returns:
        str: A string indicating the format of the job description.
    """
    content = ''
    if gen_details.tone: 
        if gen_details.tone == 'persuasivo':
            content += f'Crea una oferta de trabajo alegre pero profesional con una mezcla de oraciones y viñetas. Redacta una oferta que sea animada y entusiasta. Asegúrate de que la oferta capte la atención y esté llena de entusiasmo. '
        else:
            content += f'Crea una oferta de trabajo formal y profesional con una mezcla de oraciones y viñetas. '
    if gen_details.language: content += f'Escribe toda la oferta de trabajo estrictamente en {gen_details.language}. ' 
    if gen_details.template_name and gen_details.template_structure.strip() != '':
        content += f'Asegúrate de que la oferta usa solo estos encabezados de plantilla:\n {gen_details.template_structure}\n'
    # Mail
    if gen_details.template_name == 'email_short':  
        content += f'Al principio de la oferta, escribe en una frase un resumen sobre la empresa. ' 
        content += f'Después, añade los encabezados de la plantilla sin repetir información. '
        content += f'Usa entre 150 y 300 palabras en la oferta. '
    elif gen_details.template_name == 'email_long':
        content += f'Empieza con un saludo y presentación del reclutador [NOMBRE] de {gen_details.business_unit} como si fuera un email. '
        content += f'Después, añade los encabezados de la plantilla sin repetir información.\n'
        #content += f'{gen_details.template_structure} \n\n'
        content += f'Acaba la oferta invitando a que se pongan en contacto con nosotros.'
        content += f'Usa más de 400 palabras en la oferta. No repitas información y sé muy original.\n'
    elif gen_details.template_name == 'multiposting':
        content += f'La oferta se estructura únicamente en los encabezados de la plantilla.\n'
        content += f'Usa más de 800 palabras en la oferta generada. No repitas información y sé muy original.\n'
    elif gen_details.template_name == 'linkedin_short':
        content += f'La oferta se estructura únicamente en los encabezados de la plantilla.\n'
        content += f'Usa menos de 300 palabras en la oferta. '
    elif gen_details.template_name == 'linkedin_long':
        content += f'La oferta se estructura únicamente en los encabezados de la plantilla.\n'
        content += f'Usa más de 500 palabras en la oferta. No repitas información y sé muy original.\n'
    else:
        content += f'Usa más de 600 palabras en la oferta. '
        
        
    if gen_details.business_unit == 'LHH':
        content += f'Sustituye el título del puesto de trabajo completando al principio de la oferta esta frase de manera literal: buscamos para cada uno de nuestros clientes... \n'
    if gen_details.business_unit == 'Fundación':
        content += f'Redacta la oferta de forma que sea entendible por una persona con discapacidad. '
    if gen_details.emojis:
        content += f'Añade hasta 10 emoticonos de forma separada en la oferta donde consideres oportuno y con sentido. '
    
    return content


def define_client_prompt(client_params: ClientParams) -> tuple:
    """
    Generates the client prompt for the user using the general details of the client parameters.

    Args:
        client_params (ClientParams): Parameters containing general details of the client.

    Returns:
        tuple[str, str, str]: A tuple-string which contains information about the client.
    """
    content = ''
    if client_params.client_sector: content += f'Sector de la empresa: {client_params.client_sector}\n'
    if client_params.client_url: 
        name, description = get_company_information(client_params.client_url) ## NO VA EL AWAIT - ASYNC (raro)
        if name: 
            content += f'Es muy importante que no escribas el nombre de la empresa, {name}, en ningún momento.\n'
            if name.lower() in description.lower(): 
                description = description.lower().replace(name.lower(), '').capitalize()
        else:
            content += f'Es muy importante que no escribas el nombre de la empresa en ningún momento.\n'
        if description: content += f'Descripción de la empresa: "{description}"\n'
        return content, name, description
    else:
        return content, None, None


def define_job_prompt(job_params: JobParams, 
                      req_params: ReqParams) -> str:
    """
    Generates the job prompt for the user by adding the information of the job offer.

    Args:
        job_params (JobParams): Parameters containing job details of the offer.

    Returns:
        str: A string which contains information about the job offer.
    """
    content = ''
    if job_params.profession: content += f'Nombre del puesto: {job_params.profession}\n'
    if job_params.city: content += f'Localidad: {job_params.city}\n'
    if job_params.province: content += f'Provincia: {job_params.province}\n'
    if job_params.num_employees and int(job_params.num_employees) > 1: content += f'Número de personas requeridas: {job_params.num_employees}\n'
    if job_params.min_pay or job_params.max_pay:
        if job_params.min_pay and job_params.max_pay: 
            if job_params.min_pay != job_params.max_pay:
                content += f'Retribución económica entre {job_params.min_pay} y {job_params.max_pay} euros {job_params.freq_pay}\n'
            else:
                content += f'Retribución económica de {job_params.min_pay} euros {job_params.freq_pay}\n'
        elif job_params.min_pay:
            content += f'Retribución económica desde {job_params.min_pay} euros {job_params.freq_pay}\n'
        elif job_params.max_pay:
            content += f'Retribución económica hasta {job_params.max_pay} euros {job_params.freq_pay}\n'
    if job_params.bonus: content += f'Retribucion economica adicional (bonus) de {job_params.bonus} euros\n'
    if job_params.contract_type: content += f'Tipo de contrato {job_params.contract_type}\n'
    if job_params.work_rate: content += f'Jornada laboral {job_params.work_rate}\n'
    if job_params.schedule: content += f'Horario de trabajo de {job_params.schedule}\n'
    if job_params.contract_type == 'temporal':
        if job_params.start_date: content += f'Fecha de inicio {convert_dates(job_params.start_date)}\n'
        if job_params.end_date: content += f'Fecha de finalización {convert_dates(job_params.end_date)}\n'
    if req_params.skills: 
        content += f'Parafrasea e incluye estos requisitos y funciones: {req_params.skills}\n'
    content += f'Incluye otros requisitos y funciones típicas de un {job_params.profession}\n'
    if req_params.driving_license: 
        content += f'Permiso {req_params.driving_license} de conducción'
        if req_params.vehicle: 
            content += f', disponibilidad de vehículo.\n'
        else: 
            content += f'\n'
    if req_params.work_type: content += f'El trabajo se desarrolla de forma {req_params.work_type}.\n'
    return content
    


def define_benefits_prompt(job_params: JobParams) -> str:
    """
    Generates the benefits prompt for the user by adding the list of benefits.

    Args:
        job_params (JobParams): Parameters containing job details of the offer.
        gen_details (GenerationDetails): Parameters containing job details of the offer.

    Returns:
        str: A string which contains information about the benefits of the job offer.
    """
    content = ''
    if job_params.benefits != '':
        content += f'Añade una frase larga por cada beneficio: ' + job_params.benefits
    if job_params.contract_type == 'Permanente':
        if job_params.bonus: content += f', bonus de {job_params.bonus} euros {job_params.freq_pay}'
    return content
    