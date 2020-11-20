import pandas as pd
import numpy as np
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def find_words(text, search):
    """Find exact words"""
    dText   = text.split()
    dSearch = search.split()

    found_word = 0

    for text_word in dText:
        for search_word in dSearch:
            if search_word == text_word:
                found_word += 1

    if found_word == len(dSearch):
        return 1
    else:
        return 0
    
def clean_text(text):
    """
        text: a string
        
        return: modified initial string
        
    """
    
    arabic_diacritics = re.compile("""
                                 ّ    | # Tashdid
                                 َ    | # Fatha
                                 ً    | # Tanwin Fath
                                 ُ    | # Damma
                                 ٌ    | # Tanwin Damm
                                 ِ    | # Kasra
                                 ٍ    | # Tanwin Kasr
                                 ْ    | # Sukun
                                 ـ     # Tatwil/Kashida
                             """, re.VERBOSE)
    
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)


    text = re.sub(arabic_diacritics, '', text)
    
    text =  re.sub(r'(.)\1+', r'\1', text)
    
    replace_by_blank_symbols = re.compile('\u00bb|\u00a0|\u00d7|\u00a3|\u00eb|\u00fb|\u00fb|\u00f4|\u00c7|\u00ab|\u00a0\ude4c|\udf99|\udfc1|\ude1b|\ude22|\u200b|\u2b07|\uddd0|\ude02|\ud83d|\u2026|\u201c|\udfe2|\u2018|\ude2a|\ud83c|\u2018|\u201d|\u201c|\udc69|\udc97|\ud83e|\udd18|\udffb|\ude2d|\udc80|\ud83e|\udd2a|\ud83e|\udd26|\u200d|\u2642|\ufe0f|\u25b7|\u25c1|\ud83e|\udd26|\udffd|\u200d|\u2642|\ufe0f|\udd21|\ude12|\ud83e|\udd14|\ude03|\ude03|\ude03|\ude1c|\udd81|\ude03|\ude10|\u2728|\udf7f|\ude48|\udc4d|\udffb|\udc47|\ude11|\udd26|\udffe|\u200d|\u2642|\ufe0f|\udd37|\ude44|\udffb|\u200d|\u2640|\udd23|\u2764|\ufe0f|\udc93|\udffc|\u2800|\u275b|\u275c|\udd37|\udffd|\u200d|\u2640|\ufe0f|\u2764|\ude48|\u2728|\ude05|\udc40|\udf8a|\u203c|\u266a|\u203c|\u2744|\u2665|\u23f0|\udea2|\u26a1|\u2022|\u25e1|\uff3f|\u2665|\u270b|\u270a|\udca6|\u203c|\u270c|\u270b|\u270a|\ude14|\u263a|\udf08|\u2753|\udd28|\u20ac|\u266b|\ude35|\ude1a|\u2622|\u263a|\ude09|\udd20|\udd15|\ude08|\udd2c|\ude21|\ude2b|\ude18|\udd25|\udc83|\ude24|\udc3e|\udd95|\udc96|\ude0f|\udc46|\udc4a|\udc7b|\udca8|\udec5|\udca8|\udd94|\ude08|\udca3|\ude2b|\ude24|\ude23|\ude16|\udd8d|\ude06|\ude09|\udd2b|\ude00|\udd95|\ude0d|\udc9e|\udca9|\udf33|\udc0b|\ude21|\udde3|\ude37|\udd2c|\ude21|\ude09|\ude39|\ude42|\ude41|\udc96|\udd24|\udf4f|\ude2b|\ude4a|\udf69|\udd2e|\ude09|\ude01|\udcf7|\ude2f|\ude21|\ude28|\ude43|\udc4a|\uddfa|\uddf2|\udc4a|\ude95|\ude0d|\udf39|\udded|\uddf7|\udded|\udd2c|\udd4a|\udc48|\udc42|\udc41|\udc43|\udc4c|\udd11|\ude0f|\ude29|\ude15|\ude18|\ude01|\udd2d|\ude43|\udd1d|\ude2e|\ude29|\ude00|\ude1f|\udd71|\uddf8|\ude20|\udc4a|\udeab|\udd19|\ude29|\udd42|\udc4a|\udc96|\ude08|\ude0d|\udc43|\udff3|\udc13|\ude0f|\udc4f|\udff9|\udd1d|\udc4a|\udc95|\udcaf|\udd12|\udd95|\udd38|\ude01|\ude2c|\udc49|\ude01|\udf89|\udc36|\ude0f|\udfff|\udd29|\udc4f|\ude0a|\ude1e|\udd2d|\uff46|\uff41|\uff54|\uff45|\uffe3|\u300a|\u300b|\u2708|\u2044|\u25d5|\u273f|\udc8b|\udc8d|\udc51|\udd8b|\udd54|\udc81|\udd80|\uded1|\udd27|\udc4b|\udc8b|\udc51|\udd90|\ude0e')
    replace_by_apostrophe_symbol = re.compile('\u2019')
    replace_by_dash_symbol = re.compile('\u2014')
    replace_by_u_symbols = re.compile('\u00fb|\u00f9')
    replace_by_a_symbols = re.compile('\u00e2|\u00e0') 
    replace_by_c_symbols = re.compile('\u00e7') 
    replace_by_i_symbols = re.compile('\u00ee|\u00ef') 
    replace_by_o_symbols = re.compile('\u00f4') 
    replace_by_oe_symbols = re.compile('\u0153')
    replace_by_e_symbols = re.compile('\u00e9|\u00ea|\u0117|\u00e8')
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|,;]')
    REPLACE = re.compile("[@|(|)|\||:|>|<|_|#|\.|+|÷|×|'|!|\?|٪|؟\|&|;|\*|[|]|{|}|-|،|_|’|;|!|:|^|&|%|/]")
    
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u0640"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    chlist = [chr(i) for i in range(1569, 1611)]+[chr(i) for i in range(1646, 1749)]
    text = ''.join([i if i in chlist else ' ' for i in text])
    text = ' '.join([u'{}'.format(i) for i in text.split() if len(i)>1])
    cleanText = re.sub(r'\d+', ' ', text)
    
    cleanText = re.sub(emoj, ' ', cleanText)
    cleanText =  re.sub(REPLACE, ' ', cleanText)
    #cleanText = cleanText.replace('LF'," ")
    cleanText = cleanText.replace('"'," ")
    cleanText = cleanText.replace('…'," ")
    #cleanText =  re.sub(r'\s*[A-Za-z]+\b', ' ' , cleanText)
    
    while '  ' in cleanText:
        cleanText = cleanText.replace('  ', ' ')
    return cleanText


 
def remove_repeated_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
    correct_tokens = [replace(word) for word in tokens]
    return correct_tokens

def removeStopWords(tokens):
    stopwords_list = stopwords.words('arabic')
    listStopWords = stopwords_list
    stopWords = pd.read_excel("../stopWordslist/stopword0.6.xls")
    listStopWords.extend(list(stopWords['الكلمة'].values))
    result = [i for i in tokens if not i in listStopWords]
    return result

def tokenize_text(text):
    tokens = word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens
