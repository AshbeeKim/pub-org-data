import os
from glob import glob
# import sys
# import functools
'''
1. 데이터 타입 반환
2. 데이터 최소 길이, 최대 길이 반환
3. datetime의 기본 형식과 달라서, 숫자 형태로 표기되지만 날짜 특성을 가진 경우
4. 숫자인데 전체가 nan일 경우
5. 숫자인데 부분 nan일 경우
6. 데이터 길이에 따라 재확인해야 하는 것들(영어, 숫자 <- 1 byte, 
                                한글 <- 2 bytes,,,3 bytes도 있지만 편한 연산을 위해 2bytes로 작성함)
7. 코드성 데이터로 unique를 확인해야 하는 경우
'''
if __name__ == 'config.define':
    from config.define.kr_csv import WIN_CSV
    from config.define.kr_len import kr_compiled
    
    dname = input(f'{os.getcwd()}/data/define 이후의 경로를 입력하세요. : ')
    path = os.path.join(os.getcwd(), f'data/define/{dname}')
    try:
        os.mkdir(path)
    except:
        os.makedirs(path, exist_ok=True)
    for num in range(len(glob(path + "/*.csv"))):
        filedata = WIN_CSV(dpath=path, check_num=num)
        fdata = filedata.data
        fcols = filedata.col_list
        ftypes = filedata.dtypes
        
        len_data = fdata.copy()
        note = []
        for fcol, ftype in zip(fcols, ftypes):
            try:    # dtype('O')
                len_data[fcol] = len_data[fcol].apply(lambda x: (x.rstrip()).lstrip())
            except: # dtype('int64') or dtype('float64')
                len_data[fcol] = len_data[fcol].astype(str)
                null_bucket = ["nan", "NaN", "None", "none", "na", "Na", "-"]
                len_data[fcol] = len_data[fcol].apply(lambda x: "" if x in null_bucket else x)
            len_data[fcol] = len_data[fcol].apply(lambda x: kr_compiled(cell=x).length if x != None else x)
            if list(len_data[fcol].unique())!=list([0]):
                len_data[fcol] = len_data[fcol].apply(lambda x: None if x==0 else x)
                if ftype == 'O':
                    if len_data[fcol].min() != len_data[fcol].max():
                        note.append("VARCHAR")
                    else:
                        note.append(f"CHAR_{int(len_data[fcol].max())}")
                else:
                    if len_data[fcol].min() == len_data[fcol].max():
                        note.append(f"CHAR_{int(len_data[fcol].max())}")
                    else:
                        note.append("NUMERIC")
            elif list(len_data[fcol].unique())==list([0]):
                note.append("항목값없음")
        # len 정보만 담은 데이터 따로 생성 완료
        brief_len_data = ((len_data.describe()).loc[["min", "25%", "50%", "75%", "max", "count"], :]).T
        brief_len_data['dtype'] = ftypes.copy()
        brief_len_data['note'] = note.copy()
        brief_len_data.reset_index(inplace=True)
        # 마지막 print는 markdown 형태로 보기 좋게 출력하기
        print(brief_len_data.to_markdown(), '\n\n')
        
        while True: # 값 비교, 추가 확인 등의 데이터 세부 내용 확인이 필요한 경우
            checkups = input("세부 내용을 확인하겠습니까?(True: 1, False: 0)\t")
            
            try:
                int(checkups)
            except:
                checkups = checkups.lower()
                if (checkups=='t') or (checkups=='true'):
                    checkups = 1
                elif (checkups=='f') or (checkups=='false'):
                    break
                else: 
                    print('"True/False" 로 된 값을 입력해주세요.')
                    continue
            
            if checkups:
                from config.define.kr_unq import kr_codes
                col_num = int(input("확인할 항목 번호를 입력하세요.\t"))
                print(kr_codes(value=fdata.iloc[:,col_num]).unqs)
                continue