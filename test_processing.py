#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""
def is_vowel(input_character):
    ord_val = ord(input_character)
    if ord_val==65 or ord_val==97:
        return True
    if ord_val==69 or ord_val==101:
        return True
    if ord_val==73 or ord_val==105:
        return True
    if ord_val==79 or ord_val==111:
        return True
    if ord_val==85 or ord_val==117:
        return True
    return False

def normalize(input_string):
    """
     인풋으로 받는 스트링에서 정규화된 스트링을 반환함
     아래의 요건들을 충족시켜야함
    * 모든 단어들은 소문자로 되어야함
    * 띄어쓰기는 한칸으로 되어야함
    * 앞뒤 필요없는 띄어쓰기는 제거해야함

         Parameters:
             input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
             ex - "This is an example.", "   EXTRA   SPACE   "

         Returns:
             normalized_string (string): 위 요건을 충족시킨 정규회된 string
             ex - 'this is an example.'

         Examples:
             >>> import text_processing as tp
             >>> input_string1 = "This is an example."
             >>> tp.normalize(input_string1)
             'this is an example.'
             >>> input_string2 = "   EXTRA   SPACE   "
             >>> tp.normalize(input_string2)
             'extra space'
    """
    # 65~90 ASCII code of capital characters
    normalized_string = None
    for i in input_string:
        if i==' ' :
            if normalized_string==None :
                continue
            elif normalized_string[-1]==' ' :
                continue
            normalized_string += i
        else :
            ascii_code = ord(i)
            if 64<ascii_code and ascii_code<91 :
                normalized_string += chr(ascii_code+32)
            elif 96<ascii_code and ascii_code<123 :
                normalized_string += i
            else :
                normalized_string += i
    
    if len(normalized_string)>0 :
        if normalized_string[-1]==' ' :
            normalized_string = normalized_string[0:-1]
    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호로 이루어진 string
            ex - "This is an example."

        Returns:
            no_vowel_string (string): 모든 모음 (a, e, i, o, u)를 제거시킨 스트링
            ex - "Ths s n xmpl."

        Examples:
            >>> import text_processing as tp
            >>> input_string1 = "This is an example."
            >>> tp.normalize(input_string1)
            "Ths s n xmpl."
            >>> input_string2 = "We love Python!"
            >>> tp.normalize(input_string2)
            ''W lv Pythn!'
    """
    no_vowel_string = None
    for i in range(len(input_string)) :
        if is_vowel(i):
            continue
        no_vowel_string += i
    return no_vowel_string
