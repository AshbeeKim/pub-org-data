import pandas as pd

def init_load(datatype, path, **kwargs):
    if path.split('/')[-1]=='script':
        data = pd.read_excel(f'{path}/{datatype}.xlsx', **kwargs)
    elif path.split('/')[-1]=='OpenData':
        data = pd.read_excel(f'{path}/script/{datatype}.xlsx', **kwargs)
    else:
        try:
            data = pd.read_excel(f'{path}/{datatype}.xlsx', **kwargs)
        except:
            rel_path = input(f'Type the path located {datatype}(e.g. /content/drive/sample_data) : ')
            data = pd.read_excel(f'{rel_path}/{datatype}.xlsx', **kwargs)
    return data

def METADF(path, days, tasks, org_name=None, org_vals=None, **kwargs):
    '''
    셀병합 얘가 가장 큰 문제점인데....아니 파일 작성하고도, 다시 열어봐야 한다는 게 말이 되냐고ㅠㅠㅠㅠㅠ
    '''
    metadata = init_load('metadata', path, header=[0, 1])
    
    for num in range(4):
        metadata.columns[num] = tuple([(metadata.columns[num])[0] if col[:7]=='Unnamed' else col for col in metadata.columns[num]])
    
    metadata[('항목명', '기관 항목명')] = org_name if org_name else None
    metadata[('항목명', '공공데이터포털 항목명')] = kwargs['pub_name'] if kwargs['pub_name'] else None
    metadata[('항목명', '동일여부')] = ['N' if cont1!=cont2 else 'Y' for cont1, cont2 in zip(metadata[('항목명', '공공데이터포털 항목명')].values, metadata[('항목명', '기관 항목명')].values)]
    
    metadata[('메타 데이터', '기관 메타데이터')] = org_vals if org_vals else None
    metadata[('메타 데이터', '공공데이터포털 메타데이터')] = kwargs['pub_vals'] if kwargs['pub_vals'] else None
    
    metadata[('메타 데이터', '동일여부')] = ['N' if cont1!=cont2 else 'Y' for cont1, cont2 in zip(metadata[('메타 데이터', '공공데이터포털 메타데이터')].values, metadata[('메타 데이터', '기관 메타데이터')].values)]
    if metadata[('메타 데이터', '공공데이터포털 메타데이터')]:
        metadata[('메타 데이터', '동일여부')] = [' ' if metadata[('메타 데이터', '기관 메타데이터')][num]==None else cont for num, cont in enumerate(metadata[('메타 데이터', '동일여부')].values)]
    
    metadata[metadata.columns[3]] = [num+1 for num, cont in enumerate(metadata[('항목명', '기관 항목명')].values)]
    metadata.to_excel(f'{path}/{days}/{tasks}_metadata.xlsx', header=[0,1], encoding='cp949')
    print(metadata)
    return print(f'========================================\t메타데이터 : "{path}/{days}/{tasks}_metadata.xlsx" 저장 완료(확인 필수!!!)\t========================================')
# DF.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, 
            # index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, 
            # encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)[source]
# 왜 병합한 셀을 잘 처지하지 못하는지와 메타데이터 열과 값 사이에 빈 행이 하나 추가되는지를 확인하고 고쳐야 함. 너무 번거롭..

def FILEDF(path, days, tasks, pub_fcol=None, org_fcol=None):
    '''
    이제까지는 csv 열을 읽어 와서 처리했는데, 크롤링을 하게 되면 달라질 수 있어서 일단은 이 정도로만 작성
    '''
    filedata = init_load('filedata', path)
    
    filedata['기관 항목명'] = org_fcol if org_fcol else None
    filedata['공공데이터포털 항목명'] = pub_fcol if pub_fcol else None
    try:
        filedata['파일항목순번'] = [num+1 for num, cont in enumerate(filedata['기관 항목명'].values)]
    except:
        filedata['파일항목순번'] = [num+1 for num, cont in enumerate(filedata['공공데이터포털 항목명'].values)]
    filedata['동일여부'] = ['Y' if pub==org else 'N' for pub, org in zip(filedata['공공데이터포털 항목명'], filedata['기관 항목명'])]
    
    filedata.to_excel(f'{path}/{days}/{tasks}_filedata.xlsx', index=False, encoding='cp949')
    print(filedata)
    return print(f'========================================\t파일데이터 : "{path}/{days}/{tasks}_filedata.xlsx" 저장 완료\t========================================')

def OAPIDF(path, days, tasks, Name=None, SN=1, I_col=None, O_col=None, option='repeat'):
    '''
    Name, SN, I_col, O_col은 반복문 내에서 매번 바꿔야 하지만(물론 경우에 따라서 아닐 수도 있음), option은 마지막 회차에만 'fin'으로 바꿀 것!!!
    '''
    openapi = init_load('openapi', path)
    
    if type(Name)==str:
        openapi['오퍼레이션명'] = [Name for cont in openapi['기관사이트 I/O항목명'].values]
        openapi['오퍼레이션 일련번호'] = [SN for cont in openapi['오퍼레이션명'].values]
        
        I_num = len(I_col)  # check IN col number
        for o in O_col:
            I_col.append(o)
        openapi['기관사이트 I/O항목명'] = I_col
        openapi['I/O 일련번호'] = [num+1 for num, cont in enumerate(openapi['기관사이트 I/O항목명'].values)]
        openapi['I/O 구분'] = ['I' if num<I_num else 'O' for num, cont in enumerate(openapi['기관사이트 I/O항목명'].values)]
        openapi['동일여부'] = ['Y' if pub==org else 'N' for pub, org in zip(openapi['공공데이터포털 I/O항목명'], openapi['기관사이트 I/O항목명'])]
        if option.lower() != 'repeat':
            openapi.to_excel(f'{path}/{days}/{tasks}_openapi.xlsx', index=False, encoding='cp949')
            print(openapi)
            return print(f'========================================\t오픈API : "{path}/{days}/{tasks}_openapi.xlsx" 저장 완료\t========================================')
        print(f'\t\t===================================\t>>appended {SN} : {Name}<<\t===================================\t\t')
    else:
        return print(f'========================================\t\t<<USE THIS DEFINITION WITH ITERATION>>\t\t========================================')