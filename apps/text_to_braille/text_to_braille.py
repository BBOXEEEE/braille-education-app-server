import hgtk
from . import braille_list


onsetList = {
    'ㄱ': "⠈", 'ㄲ': "⠠⠈", 'ㄴ': "⠉", 'ㄷ': "⠊", 'ㄸ': "⠠⠊",
    'ㄹ': "⠐", 'ㅁ': "⠑", 'ㅂ': "⠘", 'ㅃ': "⠠⠘", 'ㅅ': "⠠", 'ㅆ': "⠠⠠",
    'ㅇ': "⠛", 'ㅈ': "⠨", 'ㅉ': "⠠⠨", 'ㅊ': "⠰", 'ㅋ': "⠋", 'ㅌ': "⠓",
    'ㅍ': "⠙", 'ㅎ': "⠚"
}
nucleuseList = {
    'ㅏ': "⠣", 'ㅐ': "⠗", 'ㅑ': "⠜", 'ㅒ': "⠜⠗", 'ㅓ': "⠎", 'ㅔ': "⠝",
    'ㅕ': "⠱", 'ㅖ': "⠌", 'ㅗ': "⠥", 'ㅘ': "⠧", 'ㅙ': "⠧⠗", 'ㅚ': "⠽",
    'ㅛ': "⠬", 'ㅜ': "⠍", 'ㅝ': "⠏", 'ㅞ': "⠏⠗", 'ㅟ': "⠍⠗", 'ㅠ': "⠩",
    'ㅡ': "⠪", 'ㅢ': "⠺", 'ㅣ': "⠕"
}
codaList = {
    '': "", 'ㄱ': "⠁", 'ㄲ': "⠁⠁", 'ㄳ': "⠁⠄", 'ㄴ': "⠒", 'ㄵ': "⠒⠅",
    'ㄶ': "⠒⠴", 'ㄷ': "⠔", 'ㄹ': "⠂", 'ㄺ': "⠂⠁", 'ㄻ': "⠂⠢", 'ㄼ': "⠂⠃",
    'ㄽ': "⠂⠄", 'ㄾ': "⠂⠦", 'ㄿ': "⠂⠲", 'ㅀ': "⠂⠴", 'ㅁ': "⠢", 'ㅂ': "⠃",
    'ㅄ': "⠃⠄", 'ㅅ': "⠄", 'ㅆ': "⠌", 'ㅇ': "⠶", 'ㅈ': "⠅", 'ㅊ': "⠆",
    'ㅋ': "⠖", 'ㅌ': "⠦", 'ㅍ': "⠲", 'ㅎ': "⠴"
}

def get_abbreviation2(nucleus, coda):
    abbr_map = {
        ('ㅓ', 'ㄱ'): "⠹", ('ㅓ', 'ㄴ'): "⠾", ('ㅓ', 'ㄹ'): "⠞", ('ㅕ', 'ㄴ'): "⠡", 
        ('ㅕ', 'ㄹ'): "⠳", ('ㅕ', 'ㅇ'): "⠻", ('ㅗ', 'ㄱ'): "⠭", ('ㅗ', 'ㄴ'): "⠷", 
        ('ㅗ', 'ㅇ'): "⠿", ('ㅜ', 'ㄴ'): "⠛", ('ㅜ', 'ㄹ'): "⠯", ('ㅡ', 'ㄴ'): "⠵", 
        ('ㅡ', 'ㄹ'): "⠮", ('ㅣ', 'ㄴ'): "⠟",
    }
    return abbr_map.get((nucleus, coda), "")

def get_abbreviation(onset, nucleus, coda):
    abbr_map = {
        ('ㄱ', 'ㅏ', ''): "⠫", ('ㄴ', 'ㅏ', ''): "⠉", ('ㄷ', 'ㅏ', ''): "⠊", ('ㅁ', 'ㅏ', ''): "⠑", ('ㅇ', 'ㅏ', ''): "⠣",
        ('ㅂ', 'ㅏ', ''): "⠘", ('ㅅ', 'ㅏ', ''): "⠇", ('ㅈ', 'ㅏ', ''): "⠨", ('ㅋ', 'ㅏ', ''): "⠋", 
        ('ㅌ', 'ㅏ', ''): "⠓", ('ㅍ', 'ㅏ', ''): "⠙", ('ㅎ', 'ㅏ', ''): "⠚",  ('ㅇ', 'ㅓ', 'ㄱ'): "⠹",
        ('ㅇ', 'ㅓ', 'ㄴ'): "⠾", ('ㅇ', 'ㅓ', 'ㄹ'): "⠞", ('ㅇ', 'ㅕ', 'ㄴ'): "⠡", ('ㅇ', 'ㅕ', 'ㄹ'): "⠳", 
        ('ㅇ', 'ㅕ', 'ㅇ'): "⠻", ('ㅇ', 'ㅗ', 'ㄱ'): "⠭", ('ㅇ', 'ㅗ', 'ㄴ'): "⠷", ('ㅇ', 'ㅗ', 'ㅇ'): "⠿",
        ('ㅇ', 'ㅜ', 'ㄴ'): "⠛", ('ㅇ', 'ㅜ', 'ㄹ'): "⠯", ('ㅇ', 'ㅡ', 'ㄴ'): "⠵", ('ㅇ', 'ㅡ', 'ㄹ'): "⠮", 
        ('ㅇ', 'ㅣ', 'ㄴ'): "⠟", ('ㄱ', 'ㅓ', 'ㅅ') : "⠸⠎", ('ㄲ', 'ㅓ', 'ㅅ'): "⠠⠸⠎", 

        ('ㄲ', 'ㅏ', ''): "⠠⠫", ('ㄸ', 'ㅏ', ''): "⠠⠊", ('ㅃ', 'ㅏ', ''): "⠠⠘", ('ㅆ', 'ㅏ', ''): "⠠⠇",
        ('ㅉ', 'ㅏ', ''): "⠠⠨", ('ㄱ', 'ㅏ', 'ㅅ'): "⠫⠄", ('ㄴ', 'ㅏ', 'ㅅ'): "⠉⠄", ('ㄷ', 'ㅏ', 'ㅅ'): "⠊⠄", 
        ('ㅁ', 'ㅏ', 'ㅅ'): "⠑⠄", ('ㅂ', 'ㅏ', 'ㅅ'): "⠘⠄", ('ㅅ', 'ㅏ', 'ㅆ'): "⠇⠌", ('ㅋ', 'ㅏ', 'ㅆ'): "⠋⠌", 
        ('ㅌ', 'ㅏ', 'ㅆ'): "⠓⠌", ('ㅍ', 'ㅏ', 'ㅆ'): "⠙⠣⠌", ('ㅎ', 'ㅏ', 'ㅆ'): "⠚⠌", ('ㅅ', 'ㅓ', 'ㅇ'): "⠠⠻",
        ('ㅈ', 'ㅓ', 'ㅇ'): "⠨⠻", ('ㅊ', 'ㅓ', 'ㅇ'): "⠰⠻",  ('ㅆ', 'ㅓ', 'ㅇ'): "⠠⠠⠻",  ('ㅉ', 'ㅓ', 'ㅇ'): "⠠⠨⠻",
    }
    return abbr_map.get((onset, nucleus, coda), "")

def split_(jamo):

    onsets = []
    nucleuses = []
    codas = []

    for j in jamo:
        index = 0
        if (j[0] == ' '): 
            index = 1
        onsets.append(j[index])
        nucleuses.append(j[index + 1])
        codas.append(j[index + 2] if len(j) == index + 3 else '')

    return onsets, nucleuses, codas

def noneAbbr(onsets, nucleuses, codas):
    braille = ''
    braille += onsetList.get(onsets)
    braille += nucleuseList.get(nucleuses)
    if (codas != ''): braille += codaList.get(codas)

    return braille


def textToBraille(hangeol):
    jamo = hgtk.text.decompose(hangeol).split('ᴥ')[:-1]
    onsets, nucleuses, codas = split_(jamo)
    
    checkAbbr = False
    tempOnset = ''
    braille = ''
    for i in range(len(onsets)): # 띄어쓰기 처리 
        braille_char = get_abbreviation(onsets[i], nucleuses[i], codas[i]) # 약어 확인 
        if (braille_char != '' and onsets[i] == 'ㅇ' and checkAbbr):
            tempOnset += braille_char
            braille_char = tempOnset
        if (nucleuses[i] == 'ㅏ' and codas[i] == ''): # 가,나,다 ... 약어 다음에 초성이 ㅇ으로 된 글자가 나오는거 어쩌고
            checkAbbr = True
            tempOnset = nucleuseList.get(nucleuses[i])
        if (braille_char == ''): # 약어가 아니었을 때
            braille_abbr = get_abbreviation2(nucleuses[i], codas[i]) # 초성이 'ㅇ'인 약어 확인 
            if (braille_abbr != ''):
                braille_char = onsetList.get(onsets[i]) + braille_abbr
            else: 
                if (onsets[i] == 'ㅇ'): # 초성이 'ㅇ'이고 종성이 없는지 확인 
                    if (checkAbbr):
                        braille_char = tempOnset + nucleuseList.get(nucleuses[i]) + codaList.get(codas[i])
                        checkAbbr = False
                    else: braille_char = nucleuseList.get(nucleuses[i]) + codaList.get(codas[i])
                else:
                    if (nucleuses[i] == 'ㅏ' and onsets[i] != 'ㅊ' and onsets[i] != 'ㄹ'):
                        braille_char = get_abbreviation(onsets[i], nucleuses[i], '') + codaList.get(codas[i])
                        checkAbbr = True 
                    else:
                        braille_char = noneAbbr(onsets[i], nucleuses[i], codas[i])
        braille += braille_char

    arr = []
    for i in braille:
        arr += braille_list.braille_to_array.get(i)
        
    return arr
