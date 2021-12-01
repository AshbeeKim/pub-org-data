import re

'''
1. 영어만 있는 경우
2. 숫자만 있는 경우
3. 한글만 있는 경우
4. 영어와 숫자가 있는 경우
5. 한글과 숫자가 있는 경우
6. 영어와 숫자, 한글이 있는 경우
7. 전화번호나 날짜 표기 등이 있을 때를 제외함.
'''

class kr_compiled:
    def __init__(self, cell=None):
        self.cell = cell
        self.cell = self.eng_length()
        self.cell = self.kor_length()
        self.cell = self.num_length()
        self.cell = self.etc_length()
        self.length = int(len(self.cell) + self.kor_compile())
        
    def eng_length(self):
        return re.sub('[a-zA-Z]', 'A', self.cell)
    def kor_length(self):
        return re.sub('[ㄱ-힣]', '가', self.cell)
    def num_length(self):
        return re.sub('[0-9]', '9', self.cell)
    def etc_length(self):
        return re.sub('[^0-9a-zA-Zㄱ-힣\:\-\/]', '*', self.cell)
    def kor_compile(self):
        kr_comp = re.compile('[ㄱ-힣]')
        kr_lens = kr_comp.findall(self.cell)
        return len(kr_lens)