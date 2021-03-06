import os
from glob import glob
import chardet  # 확정적인 방식이 아닌, 해당 파일에 대한 "가장 가능성 높은 인코딩 방식"
import numpy as np
import pandas as pd

# encoding_types = [
#     'utf-8',
#     'utf-16',
#     'utf-16le',
#     'utf-32-le',
#     'ISO_8859-1',
#     'windows-1251',
#     'euc-kr'
# ]
class WIN_CSV:
    def __init__(self, dpath=None, check_num=0):
        self.dir_path = os.getcwd()
        assert dpath is not None
        self.data_dir = os.path.join(self.dir_path, dpath)
        self.csv_list = glob(self.data_dir + "/*.csv")
        self.check_num = check_num
        print(f"\n\nFileName : {self.csv_list[self.check_num]}\n")
        self.data, self.col_list, self.dtypes = self.preprocess()
    
    def preprocess(self, **kwargs):
        try:
            self.data = pd.read_csv(self.csv_list[self.check_num], encoding="utf-8", **kwargs)
        except:
            try:
                self.data = pd.read_csv(self.csv_list[self.check_num], encoding="cp949", **kwargs)
            except:
                try:
                    self.data = pd.read_csv(self.csv_list[self.check_num], encoding="euc-kr", **kwargs)
                except:
                    try:
                        self.data = pd.read_csv(self.csv_list[self.check_num], encoding="utf-16", **kwargs)
                    except:
                        try:
                            self.data = pd.read_csv(self.csv_list[self.check_num], encoding="utf-16le", **kwargs) 
                        except:
                            pass
            
        self.col_list = self.data.columns
        self.dtypes = [self.data[fcol].dtype for fcol in self.col_list]
        return self.data, self.col_list, self.dtypes
    
    # def return_blen(self, col_type, srs):
    #     if col_type == object:
    #         self.blens = [len(blen) for blen in srs]
    #     elif (col_type == float) or (col_type == int):
    #         srs = srs.apply(lambda x: str(x))
    #         self.blens = [len(blen.encode()) for blen in srs]
    #     else:   # datetime
    #         self.blens
    #         self.blens = [len(blen) for blen in srs]
    #     return self.blens

    # def fnum_bnum(self):
    #     self.fnum_col = []
    #     self.bnum_col = []
    #     return self.fnum_col, self.bnum_col