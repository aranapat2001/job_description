# from emoji import EMOJI_DATA, demojize, emojize
import re


def remove_emoji(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    return text


def brand_level_adjustments(text, brand):
    # Replace exclamation points with full stops
    if brand == 'LHH':
        text = text.replace('!', '.')
    
    return text


def make_headers_bold(text):
    # Use regular expression to identify and replace headers with bold format
    pattern = re.compile(r'^([^:\n]+:|¿.*?\?)', re.MULTILINE)
    text = pattern.sub(r'<strong>\1</strong>', text)

    return text

def highlight_names(text):
    # Use regular expression to identify and highlight [NAMES] 
    pattern = re.compile(r'\[(.*?)\]', re.MULTILINE)
    text = pattern.sub(r'<mark>[\1]</mark>', text)

    return text

def make_disclaimer_italics(text):
    # Use regular expression to identify and replace disclaimers with italics format
    pattern = re.compile(r'\*(.*?)\*', re.MULTILINE)
    text = pattern.sub(r'<i>\1</i>', text)

    return text

def convert_string_to_html(text):
    """Perform actions such as:
        - new lines turn to paragraphs
        - dashes are bullet points
        - headers are bold
    """
    HTML = """"""
    list_has_started = False

    # Apply make_headers_bold to the text
    text = make_headers_bold(text)

    # Apply highlight names to the text
    text = highlight_names(text)
    
    # Apply make_disclaimer_italics to the text
    text = make_disclaimer_italics(text)
    
    # if it is a dash, wrap the line with <li></li>
    # if list hasnt started, open the <ul>
    # if next line doesn't have a dash, close with <ul>

    for line in text.split('\n'):
        line = line.strip()
        if len(line) == 0:
            continue
        # if line starts with emoji
        # starts_with_emoji = line[0] in EMOJI_DATA.keys()
        # print(starts_with_emoji)

        if line[0] == '-':
            if not list_has_started:
                # if list hasn't started, open the <ul> tag
                line = f'<ul><li>{line[1:].strip()}</li>'
            else:
                line = f'<li>{line[1:].strip()}</li>'

            HTML += f'\n{line}\n'

            list_has_started = True

        elif '*' in line:
            # convert text between * as bold
            line = re.sub(r'\*{1,6}(.*?)\*{1,6}', r'<strong>\1</strong>', f'<p>{line}</p>')

        else:
            if list_has_started:
                line = f'</ul><p>{line}</p>'
                list_has_started = False
                HTML += f'\n{line}\n'
            else:
                HTML += f'\n<p>{line.strip()}</p>\n'

    # text = text.split('\n')
    # text = filter(lambda x: len(x)>0, text)
    # text = ''.join([f'\n<p>{x.strip()}</p>\n' for x in text])
    # print(text)

    return HTML


def listify(string: str) -> str:
    split_string = string.split('\n')  # split on new line
    split_string = filter(lambda x: len(x.strip()), split_string)  # remove empty strings
    split_string = list(split_string)
    split_string = [re.sub(r'\d+\.', '', x) for x in split_string]  # remove numbers
    split_string = ''.join([f'<li>{x.strip()}</li>' for x in split_string])
    split_string = f'<ol>{split_string}</ol>'  # ordered list
    return split_string
