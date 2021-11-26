import os
import sys
# from config.kr_csv import WIN_CSV
# from config.scrap. ~~
import pandas as pd
# WIN_CSV(4, 0).print_kr_csv()
print(os.getcwd())
# print(os.name(__name__))
'''
# pub_org_data
#     ├ scrap
#     ├ define
#     ├ compare
# ~~~~~~~~~~~~~
반복 작업의 구간을 각 모듈별로 처리되도록 하려면,
'''
print('+'*50, '\n\n\n')

if __name__ == '__main__':
    while True:
        task_name = input('Task : ')
        if task_name=='compare':    # 비교 업무 진행 시, # script로 생성한 파일 옮겨야 함.
            # import config.compare.~~
            # os.getcwd=='/Volumes/WORK/OpenData'
            import script.config.repeatContents as IC
            # 바로 이어지고 받아지도록 하려면, script 안에도 main.py가 있어야 함.
            print(IC.NessFromJSON(f'{os.getcwd()}/{task_name}')[0])
            # if __name__ == '__main__':
            # print(os.name(__name__)) 
        elif task_name == 'define': # 정의 업무 진행 시
            # from config.kr_csv import WIN_CSV
            # filedata = WIN_CSV(18, 0)
            
            # filedata.print_kr_csv()
            path = os.path.join(os.getcwd(), 'data/day_18')
            flist = os.listdir(path)
            print(flist)
            filedata = os.path.join(path, flist[2])
            filedata = pd.read_csv(filedata, encoding='cp949')
            fcols = filedata.columns
            
            # for num in ['2', '3', '4', '5', '11', '25']:
            # print(filedata[filedata['학교급코드'] == 2].to_markdown())#int(num)].to_markdown())
                
            for col in fcols:
                try:
                    filedata[col] = filedata[col].apply(lambda x: (x.rstrip()).lstrip())
                    print(f"{col} : {filedata[col].dtype}")
                except:
                    print(f"{col} : {filedata[col].dtype}")
                    filedata[col] = filedata[col].astype(str)
                filedata[f'{col}_len'] = filedata[col].apply(lambda x: len(x))
            len_col = [col for col in filedata.columns if col not in fcols]
        # print(filedata['정보공시 학교코드'].unique(), len(filedata['정보공시 학교코드'].unique()), '\n\n')
        # import numpy as np
        # print(filedata[filedata['학교특성']!="nan"].to_markdown())
        # print(filedata['학교급코드'].unique(), '\n\n')
        print((((filedata.loc[:,len_col]).describe()).loc[["min", "25%", "50%", "75%", "max"], :]).T, '\n\n')
        # print((((filedata.loc[:,len_col]).describe()).loc[["min","max"], :]).T)
        break