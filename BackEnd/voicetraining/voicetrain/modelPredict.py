import re
import pickle
from hanspell import spell_checker
from konlpy.tag import Kkma

import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from .apps import VoicetrainConfig

# token_ls path
token_ls_path = ''
word_to_index_path = ''

def re_sub(self):
    sample = re.sub(r',', '', self)
    self= re.sub(r'(.)(\d)\s(\d)\s(\d)\s(\d)', r'\1\2\3\4\5', sample)
    self = re.sub("\d\d\d\d", " @", self)
    self = re.sub("\d\d분", " #분", self)

    return self


## 띄어쓰기, 맞춤법
def check_spell(self):
    spelled_sent = spell_checker.check(self)
    self = spelled_sent.checked

    return self


# kkma 형태소 토큰화 함수정의
def kkma_tokenizer(self):
    kkma = Kkma()
    valid_pos = ['NNG', 'VV', 'SW', 'MAG']

    # tokenize
    token_text = kkma.pos(self)

    # 불용어 제거
    ls = []
    for token in token_text:

        if token[1] in valid_pos:
            ls.append(token[0])
    self = ls
    return self


## df의 정수인코딩 column 생성 및 반영 함수화
# tokenizer.fit_on_texts 에서 특수문자 @,# 을 자체적으로 없앰, 이 부분 보완 필요

def int_encode(self):
    # word_to_index 불러오기
    wti = open(word_to_index_path, 'rb')
    word_to_index = pickle.load(wti)

    # 토크나이저 최적화
    tokenizer = Tokenizer()
    tokenizer.word_index = word_to_index
    seq = tokenizer.texts_to_sequences(self)
    ls = sum(seq, [])
    self = ls
    return self


def padding(self):
    max_len = 8
    pad = [0] * (max_len - len(self))
    self = pad + self
    return self


def pred(self):
    self = np.array(self).reshape(-1, 8)
    model = VoicetrainConfig.model
    pred = model.predict(self)

    if np.max(pred[0]) < 0.3:
        self = 99
    else:
        self = np.argmax(pred)
    return self


def start_predict(self):
    re_self = re_sub(self)
    re_self = check_spell(re_self)
    re_self = kkma_tokenizer(re_self)
    re_self = int_encode(re_self)
    intent = {0: '운행시작', 1: '가게전화', 2: '가게도착', 3: '픽업완료', 4: '영수증번호', 5: '소요시간선택', 6: '배달완료', 99: 'fallback_intent'}

    if re_self == []:
        result = 99
    else:
        pad_self = padding(re_self)
        result = pred(pad_self)

    if result == 4:
        strip = re.sub(' +', '', self)
        numbers = re.findall("\d+", strip)[0]
        print(strip)
        print(numbers)
        if len(numbers) != 4:
            numbers = [99]
    else:
        numbers = 0

    # print(result, intent[result], self, numbers)
    return result, int(numbers)
