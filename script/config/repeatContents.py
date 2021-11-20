import json

# https://performance.opendata2021.kr/newtask/index.do
# append -> save -> reload
def UpdateJSON(days, tasks, urls=None, path=None):
    if path==None:
        path = input("tasklist.json이 위치한 경로 : ")
        
    with open(f'{path}/tasklist.json', 'r') as jsf:
        jsd = json.loads(jsf.read())
        
    if jsd['comp_list']['days'][-1]==days:
        print("tasklist.json에는 이미 작성이 완료된 근무일입니다.")
        
    elif (type(days)==str) and (type(tasks)==list):
        jsd['comp_list']['days'].append(days)
        if urls==None:
            urls = [None for num in range(len(tasks))]
        (jsd['comp_list']['org_url']).append(urls)  # 나중에 받아와서 정제 후 입력되도록 수정할 것
        (jsd['comp_list']['tasks']).append(tasks)
        with open(f'{path}/tasklist.json', 'w') as jsf:
            jsf.write(json.dumps(jsd, indent=4, ensure_ascii=False))

# with open('/Volumes/WORK/OpenData/script/tasklist.json', 'w') as jsf:
#     jsf.write(json.dumps(tasklist, indent=4, ensure_ascii=False))
# with open(path, 'a+', encoding='utf-8') as jsf:
    # json.dump(dictobj, jsf, indent=4, ensure_ascii=False)

def NessFromJSON(path, num=-1):
    with open(f'{path}/tasklist.json', 'r', encoding='utf-8') as jsf:
        jsd = json.loads(jsf.read())
    
    URL = jsd['pub_url']
    DAY = jsd['comp_list']['days'][num]
    SITE = jsd['comp_list']['org_url'][num]
    TASK = jsd['comp_list']['tasks'][num]
    # print(jsd)
    return URL, DAY, SITE, TASK

def metaPubFile(option=None):
    PUBS = None
    if option:
        PUBS = {"pub_name":[], "pub_vals":[]}
        if option=="file":
            PUBS['pub_name'] = ['파일데이터명', '분류체계', '제공기관', '관리부서명', '관리부서 전화번호', '보유근거', '수집방법', '업데이트 주기', '차기 등록 예정일', '매체유형', '전체 행', '확장자', '다운로드(바로가기)', '데이터 한계', '키워드', '등록', '수정', '제공형태', '설명', '기타 유의사항', '비용부과유무', '비용부과기준 및 단위', '이용허락범위']
            PUBS['pub_vals'] = []
        elif option=="api":
            PUBS['pub_name'] = ['파일데이터명', '분류체계', '제공기관', '관리부서명', '관리부서 전화번호', '보유근거', '수집방법', '업데이트 주기', '차기 등록 예정일', '매체유형', '전체 행', '확장자', '다운로드(바로가기)', '데이터 한계', '키워드', '등록', '수정', '제공형태', '설명', '기타 유의사항', '비용부과유무', '비용부과기준 및 단위', '이용허락범위']
            PUBS['pub_vals'] = [] 
    return PUBS

    # mtd_col = [col[0] if col[-1][:7]=="Unnamed" else '_'.join(col) for col in metadata.columns]
    # metadata.columns = [c1 if num>3 else c2 for num, (c1, c2) in enumerate(zip(metadata.columns, mtd_col))]
    # metadata.set_index(metadata.columns[0], drop=True, inplace=True)
    # col_lv1 = list(map(lambda x: ' '.join(x[1:]), metadata.columns))

# filedata['기관 항목명'] = ["ADM_SECT_C", "SGG_NM", "SGG_OID", "COL_ADM_SE", "GID"]
# filedata['기관 항목명'] = ['번호', '시도명', '시군구명', '거주자우선주차구획번호', '거주자우선주차구획위도', '거주자우선주차구획경도', '거주자우선주차구역명', '소재지도로명주소',\
#     '소재지지번주소', '운영형태', '사용시간대정보', '사용기간', '이용요금', '이용요금할인정보', '이용요금결제방법', '이용요금환불안내정보', '정기접수시작일자', '정기접수종료일자',\
#     '신청방법', '신청서류', '관리기관전화번호', '관리기관명', '데이터기준일자', '제공기관코드', '제공기관명']
# data_col = ['연도', '기력_무연탄_발전단', '기력_무연탄_송전단', '기력_유연탄_발전단', '기력_유연탄_송전단', '기력_중유_발전단', '기력_중유_송전단', '기력_가스_발전단', '기력_가스_송전단', '기력_계_발전단', '기력_계_송전단', '복합화력_발전단', '복합화역_송전단', '내연력_발전단', '내연력_송전단', '한전 자회사 계_발전단', '한전 자회사 계_송전단', '기타사_발전단', '기타사_송전단', '합계_발전단', '합계_송전단']

# # I_col = ['인증키', '요청파일 타입', '서비스명', '요청시작위치', '요청종료위치', '주소']
# I_col = ['인증키', '호출문서', '페이지 위치', '페이지 당 요청 숫자']
# # O_col = ['총 데이터 건수 (정상조회 시 출력됨)', '요청결과 코드 (하단 메세지설명 참고)', '요청결과 메시지 (하단 메세지설명 참고)', '교육청명', '교육지원청명', '유치원코드', '유치원명', '설립유형',
# #          '교실수', '교실면적', '체육장', '보건/위생공간', '조리실/급식공간', '기타공간', '공시차수', '주소']
# O_col = ['보관측일자', '보관측소구분코드', '보관측소명칭', '보관측소주소', '관할기관명', '보상류수위값(단위:El.m)(El.m)', '보하류수위값(단위:El.m)(El.m)',
#          '유입량(단위:m^3/s)(㎥/s)', '저수량(단위:만m^3)(만m³/s)', '공용량(단위:백만m^3)(백만m³/s)', '총방류량(단위:m^3/s)(㎥/s)']
   
   
# a = [1, 2, 3, 4, 5]
# print(list(filter(lambda x:x%2, list(map(lambda x:x**2, a)))))
# print(type(tuple([idx for idx in range(5)]))
# day 8
# PUBMETA = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# ORGMETA = [0, 0, 1, 1, 1, 1, 1, 1, 1]
# FLDATA = [1, 1, 1, 1, 1, 1, 1, 0, 1]
# OPNAPI = [0, 0, 1, 0, 1, 1, 0, 0, 0]