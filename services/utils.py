import requests
from bs4 import BeautifulSoup
import tldextract
from services.classes import *

def get_company_information(url):
    '''
    Web Scrapping - Obtains the name and description of the company from their website
    '''
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        name = tldextract.extract(url).domain.capitalize()
        
        # Company title and description 
        title_1 = soup.find("meta", property="og:title")
        title_2 = soup.find("meta", property="title")
        desc_1 = soup.find("meta", property="og:description")
        desc_2 = soup.find("meta", property="description")

        metas = soup.find_all('meta')
        title_3 = [meta for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'title']
        desc_3 = [meta for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description']
        title_3 = title_3[0] if len(title_3) > 0 else None
        desc_3 = desc_3[0] if len(desc_3) > 0 else None

        if title_3:
            title_3 = title_3.get('content')
        if desc_3:
            desc_3 = desc_3.get('content')

        title = title_1 or title_2 or title_3
        desc = desc_1 or desc_2 or desc_3

        if title and desc:
            title = title.get('content')
            desc = desc.get('content')
        elif desc:
            desc = desc.get('content')
        elif title:
            title = title.get('content')
        
        
    except Exception as ex:
        print(ex)
        title = None
        desc = None
        
    return name, desc


def LHH_format(text):
    initial_text = 'Desde la división de [DIVISIÓN] de LHH Recruitment Solutions, especializada en la selección y/o contratación de perfiles [PERFILES], '
    return initial_text + text[0].lower() + text[1:]

def fundacion_format(text):
    disclaimer_text = '*Porque creemos en el Talento y no en las etiquetas estamos comprometidos con la no discriminación por razón de raza, edad, sexo, estado civil, ideología, opiniones políticas, nacionalidad, religión, orientación sexual o cualquier otra condición personal.* \n*Estos son nuestros principios, los que guían nuestra forma de actuar, nuestra forma de ser, de entender y liderar el mercado laboral.*'
    return text + '\n\n' + disclaimer_text

def convert_dates(date):
    year, month, day = date.split('-')
    formatted_date_str = f"{day}/{month}/{year[2:]}"
    return formatted_date_str

if __name__ == '__main__':
    import asyncio
    url = 'https://www.estudio3arquitectos.com/'
    # url = 'https://www.booker.co.uk/'
    # url = 'https://www.axa.co.uk/'
    # url = 'https://www.moonpig.com/uk/'
    # url = 'https://whiskeywealthclub.com'
    # url = 'https://tfl.gov.uk/'

    #company_name, text = asyncio.run(get_company_information(url))
    company_name, text = get_company_information(url)
    print(company_name)
    print(text)
