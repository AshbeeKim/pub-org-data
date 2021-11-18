import os
import numpy as np
import pandas as pd

def compDataAll():
    # tasklist
    datalist_path = "개별 데이터 포털 비교업무_ 파일 목록 리스트_20211027_통합본.xlsx"

    if os.getcwd()=='/Volumes/WORK/OpenData':
        datalist_path = os.path.join(os.getcwd(), 'script', datalist_path)
    else:
        datalist_path = os.path.join('/Volumes/WORK/OpenData', 'script', datalist_path)
        
    sheet1 = pd.read_excel(datalist_path, sheet_name="Sheet1")
    sheet1['파일 목록명'] = sheet1['파일 목록명'].apply(lambda x: x.rstrip().lstrip()) 
    return sheet1

def ToDoDF(tasks, data=None):
    if data==None:
        data = compDataAll()

    for num in range(len(tasks)):
        ref = data[data['파일 목록명']==tasks[num]]
        if num==0:
            todoDF = pd.DataFrame(ref)
        else:
            todoDF = pd.concat([todoDF, ref])
    todoDF.reset_index(drop=True, inplace=True)
    # print(sheet[sheet['파일 목록명'].apply(lambda x: x.split(' ')[-1])=='경로'])
    
    # sheet2 = pd.read_excel(datalist_path, sheet_name="Sheet2")

    # org_name = sheet1['기관명'].to_list()
    # site_name = sheet1['사이트명'].apply(lambda x: ' '.join(x.split(' ')[:-1])).to_list()
    # site_usl = sheet1['사이트명'].apply(lambda x: x.split(' ')[-1]).to_list()
    # file_name = []
    # for name in sheet1['파일 목록명'].values:
    #     try:
    #         if int(name.split('.')):
    #             fname = '.'.join(fname[1:])
    #     except:
    #         fname = name
    #     fname = fname.rstrip().lstrip()
    #     file_name.append(fname)
    # # file_type = sheet1['포털 메뉴'].apply(lambda x: (x.split('(')[-1])[:-1]).to_list()
    # file_type = sheet1['확장자'].apply(lambda x: 'filedata' if x=='파일' else 'openapi')
    # open_type = sheet1['제공방식 구분'].to_list()
    idpw = list(map(lambda x, y: (x.split('(')[-1])[:-1] if y==False else "None/None", data['로그인계정'], data['로그인계정'].isna()))
    return todoDF, np.unique(np.array(idpw))
# 크롤링으로 바로 작성하기는 검색까지 들어갔을 경우, 이번 주 안으로 작성 불가
# 간단한 True.False로 데이터 목록 유무에 따른 필수 작성 파일리스트 도출하기
# sheet, xlsx, csv가 아니면, metadata만 작성
# 대회부터 끝내고, html페이지 값을 metadata, filedata, openapi에 따라 xlsx로 작성하는 함수 작성
# "개방", "개방/통계", "통계", "공시" # 제공방식 구분 == '통계'면 'filedata'만 작성, 
# 일단 사이트 url로 접근한 뒤, 키워드에 파일 목록명 검색
# 검색 결과 없을 시, 검색 키값 clear하고 () -, 등을 기준으로 키워드 검색
# 검색 결과는 maximum 5페이지까지 받아오도록 하고 없기
    
def NOrMultiDF(path, days, fname, encoding=None, **kwargs):
    extension = fname.split('.')[-1]
    fpath = f'{path}/{days}/{fname}'
    if days==None:
        fpath = f'{path}/{fname}'
    if extension=='xls' or extension=='xlsx':
        data = pd.read_excel(fpath, **kwargs)
    else:
        if encoding:
            data = pd.read_csv(fpath, encoding=encoding, **kwargs)
        else:
            data = pd.read_csv(fpath, **kwargs)
    return data

# pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, 
                # dtype=None, engine=None, converters=None, true_values=None, false_values=None, 
                # skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, 
                # verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, 
                # skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)

# # header, index_col, sep, index_col=[1,2], skiprows=lambda x: x in range(4)
# print(data.columns)
# print(data.index)
# print(data.head())
# col_name = []
# col_vals = []
# for cn_n, cv_n in zip(range(1,14,3), range(2,15,3)):
#     cn = data.iloc[cn_n,:].values
#     cv = data.iloc[cv_n,:].values
#     for n, v in zip(cn, cv):
#         col_name.append(n)
#         col_vals.append(v)  
# print(len(col_name))
# print(len(col_vals))

# 아직도 안 익숙하고 모르는 부분이 많은만큼 천천히 정리하기!
# 아 근데 아직도 metadata 셀병합 열받게 폼을 만든건....휴.........
# # # multiindex & multicolumn
# data =pd.read_excel(f"./script/{DAY}/{TASK[3]}.xls", index_col=[0,1,2,3], header=[0,1])
# data =pd.read_csv(f"./script/{DAY}/{TASK[0]}.csv", encoding='utf-16', sep='\t', index_col=[0,1], header=[0,1])
# data =pd.read_csv(f"./script/{DAY}/콘텐츠산업 라이선스 매출액 현황.csv", encoding='utf-16', sep='\t', index_col=[0], header=[0,1])
# # print(list(map(lambda x: '_'.join(y.split('.')[-1] for y in x), data.index)))
# # data =pd.read_csv(f"./script/{DAY}/{TASK}.csv", encoding='utf-16', sep='\t', index_col=[0,1], header=[0,1])
# # data =pd.read_csv(f"./script/{DAY}/체지방률 변화 초등학생 여자.csv", encoding='euc-kr')
# data = pd.read_excel(f'./script/{DAY}/청계천 역사문화서비스 비콘데이터.xlsx', header=[0,1])
# skiprows=lambda x: x in range(4)
# pub & org
# data =pd.read_csv(f"./script/{DAY}/{TASK[2]}.csv", encoding="cp949")
# data =pd.read_csv(f"./script/{DAY}/서울시 노원구 공중위생업소 소재지별 운영 현황 (차트).csv", encoding="cp949")
# # data = pd.read_excel(f'./script/{DAY}/청계천 역사문화서비스 비콘데이터.xlsx')
# print(data)
# print(data.columns)

    # filedata['기관 항목명'] = [cont for cont in data['한글 컬럼명'].values]
    
    # filedata['기관 항목명'] = list(map(lambda x: '_'.join(y.split('.')[-1] for y in x), data.index))
    # data_col = list(map(lambda x: '_'.join(y if y[:7]!="Unnamed" else '' for y in x) if x[0]!=x[1] else x[0].rstrip(), data.columns))    
    # filedata['기관 항목명'] = list(map(lambda x: '_'.join(y if y[:7]!="Unnamed" else '' for y in x), data.columns))
    # filedata['기관 항목명'] = [cont for cont in data_col]
    # CMPX_col = [conts[1:3] for conts in data.index]
    # print(CMPX_col)
    # filedata['기관 항목명'] = list(map(lambda x: '_'.join(y.lstrip().rstrip() for y in x) if x[0]!=x[1] else x[0].lstrip().rstrip(), CMPX_col))
    # filedata['공공데이터포털 항목명'] = list(map(lambda x: '_'.join(y.lstrip().rstrip() for y in x) if x[0]!=x[1] else x[0].lstrip().rstrip(), CMPX_col))
    # filedata['기관 항목명'] = [y.split('.')[-1] for y in data.index]
    # filedata['기관 항목명'] = O_col[3:]
    # No_Adds = ['번호']
    # for o in O_col:
    #     No_Adds.append(o)
    # filedata['기관 항목명'] = No_Adds
    # filedata['기관 항목명'] = list(map(lambda x: '_'.join(y for y in x) if np.nan not in x else x[0] , data.index))
    # filedata['공공데이터포털 항목명'] = [cont for cont in filedata['기관 항목명'].values]

#  pd.read_excel(filename, sheet_name='Sheet1', header=None, names=[columns_name], index_col=None, 
                # usecols="A:E", dtype=[columns_dtype], skiprows=None, nrow=False, na_values=np.nan, thousands=',')

    
# data = NOrMultiDF(path, None, '작성기준표_211109.xlsx', index_col=[0], skiprows=[0, 1, 2, 14, 15], header=[0,1])
# data.columns = list(map(lambda x: '_'.join(y.rstrip().lstrip().replace('\\n', '') if y[:7]!="Unnamed" else '' for y in x) if x[0]!=x[1] else x[0].rstrip().lstrip(), data.columns)) 
# print(data.head())
# print(data.to_markdown())

def pdDPoptions() -> None:
    display = pd.options.display
    display.max_columns = 100
    display.max_rows = 100
    display.max_colwidth = 150
    display.width = None