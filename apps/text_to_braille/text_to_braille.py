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
    '\0': "", 'ㄱ': "⠁", 'ㄲ': "⠁⠁", 'ㄳ': "⠁⠄", 'ㄴ': "⠒", 'ㄵ': "⠒⠅",
    'ㄶ': "⠒⠴", 'ㄷ': "⠔", 'ㄹ': "⠂", 'ㄺ': "⠂⠁", 'ㄻ': "⠂⠢", 'ㄼ': "⠂⠃",
    'ㄽ': "⠂⠄", 'ㄾ': "⠂⠦", 'ㄿ': "⠂⠲", 'ㅀ': "⠂⠴", 'ㅁ': "⠢", 'ㅂ': "⠃",
    'ㅄ': "⠃⠄", 'ㅅ': "⠄", 'ㅆ': "⠌", 'ㅇ': "⠶", 'ㅈ': "⠅", 'ㅊ': "⠆",
    'ㅋ': "⠖", 'ㅌ': "⠦", 'ㅍ': "⠲", 'ㅎ': "⠴"
}

def get_abbreviation(onset, nucleus, coda):
    abbr_map = {
        ('ㄱ', 'ㅏ', ''): "⠫", ('ㄴ', 'ㅏ', ''): "⠉", ('ㄷ', 'ㅏ', ''): "⠊", ('ㅁ', 'ㅏ', ''): "⠑", 
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
    # print(jamo)
    onsets, nucleuses, codas = split_(jamo)
    
    braille = ''
    for i in range(len(onsets)): # 띄어쓰기 처리 
        braille_char = get_abbreviation(onsets[i], nucleuses[i], codas[i])
        if (braille_char == ''): 
            braille_char = noneAbbr(onsets[i], nucleuses[i], codas[i])
        braille += braille_char

    # print(braille)

    arr = []

    for i in braille:
        arr += braille_list.braille_to_array.get(i)

    # print(arr)
    return arr


# hangul_text = "스노우 복드"
# textToBraille(hangul_text)