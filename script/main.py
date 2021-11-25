'''
# TASK : Compare OpenData between Public and Organization databases
# script
'''
# load library - init
import os
import numpy as nps
import pandas as pd

# init path
if os.getcwd().split('/')[-1]=='OpenData':
    path = os.path.join(os.getcwd(), 'script')
else:
    path = os.getcwd()

'''
CheckPoint_1
: main.ipynb "markdown"으로 확인

case 1. 파일 오류를 제외하곤, 기관 데이터는 무조건 존재함.
case 2. 동일 확장자로 중복 입력된 경우는 몰라, 아니 무엇보다 서버 터트려놓고,,,,,,휴
'''
# load library - custom
from config.repeatContents import *
from config.loaddata import ToDoDF, NOrMultiDF, pdDPoptions
from config.savedata import METADF, FILEDF, OAPIDF

# init pandas options
pdDPoptions()
    
# *** scraping ***
# DAYS, TASKS, SITES = jsd['date'], jsd['tasks'], jsd['org_url']
# UpdateJSON(DAYS, TASKS, urls=SITES, path=path)

URL, DAY, SITE, TASK = NessFromJSON(path)
# URL, DAY, SITE, TASK = NessFromJSON(path, 5)

if not os.path.isdir(os.path.join(path, DAY)):
    os.mkdir(os.path.join(path, DAY))
    
TodayDF, idpw = ToDoDF(TASK)
# print(TodayDF.to_markdown())

# # '''
# # days = "day12"
# # TASK[1] -> 보류
# # TASK[5:]
# # '''

'''
완성되기 전까지 반복작업해야 할 부분
반복작업하면서 경우에 따라, 어떤 로직을 가질지 코멘트 달아놓기
--> 서울 데이터는 구에 따라 공데 있는 것도 없는 것도 있음. 대체적으로 .api, .csv/.xlsx가 같이 있기 때문에 api입출력 변수에 따라서 처리하면 될 듯?

'''
data = NOrMultiDF(path, DAY, TASK[5]+'.csv', encoding='cp949', header = [1])
data = data.iloc[:, 3:]

# pub_name = ["파일데이터명", "분류체계", "제공기관", "관리부서명", "관리부서 전화번호", "보유근거", "수집방법", "업데이트 주기", "차기 등록 예정일", "매체유형", "전체 행", "확장자", "다운로드(바로가기)", "데이터 한계", "키워드", "등록", "수정", "제공형태", "설명", "기타 유의사항", "비용부과유무", "비용부과기준 및 단위", "이용허락범위"]
# pub_vals = ["대구광역시 서구_협동조합 현황_20210531", "산업·통상·중소기업 - 산업·중소기업일반", "대구광역시 서구", "경제과", "", "", "", "연간", "2022-06-08", "텍스트", 49, "CSV", 333, "", "소비자생활협동조합현황,사회적협동조합,일반협동조합", "2019-10-16", "2021-06-08", "공공데이터포털에서 다운로드(원문파일등록)", "대구광역시 서구 관내에 존재하는 협동조합 명단으로 조합명, 주요사업, 주소를 포함하고 있습니다.\n협동조합 종류 : 소비자생활협동조합, 사회적협동조합, 일반협동조합\n(협동조합 설립, 변경에 관한 사항은 대구광역시 소관)", "", "무료", "건", "이용허락범위 제한 없음"]
org_name = [
    "공개일자",
    "최신수정일자",
    "갱신주기",
    "분류",
    "원본시스템",
    "저작권자",
    "제공기관",
    "제공부서",
    "담당자",
    "원본형태",
    "제3저작권자",
    "라이센스",
    "관련태그"
]
org_name = [
    "데이터개방일",
    "키워드",
    "원시시스템",
    "제공기관",
    "관리부서",
    "관리부서 전화번호",
    "업데이트 주기",
    "수정일",
    "차기등록예정일",
    "비용부과유무",
    "제공형태",
    "다운로드 횟수",
    "이용허락범위"
]
org_vals = [
    "2016-04-11",
    "기업유치",
    "파일시스템",
    "전북도청",
    "투자유치과",
    None,
    "연간",
    "2016-04-11",
    None,
    "무료",
    "빅데이터허브포털에서 다운로드(원문파일등록)",
    11,
    "이용허락범위 제한 없음"
]
# org_fcol = ['연번', '조합명', '주요사업', '주소']
metadata = METADF(path, DAY, TASK[5], org_name, org_vals)
filedata = FILEDF(path, DAY, TASK[5], org_fcol=[col for col in data.columns])
# name = "서울특별시 노원구 건물위생관리업 인허가 정보"
# icol = ["인증키", "요청파일타입", "서비스명", "요청시작위치", "요청종료위치", "개방자치단체코드"]
# openapi = OAPIDF(path, DAY, TASK[4], Name=name, I_col=icol, O_col=[col for col in data.columns], option="repeat")


'''
CheckPoint_2
: CheckPoint_1에 따라 작성 내용 수정
case 1. 통계면 메타데이터 작성할 필요 없음.
case 2. .shp 생략
********************************* 생각 정리 중 *******************************
: 현재는 어려움을 겪고 있지만, 크롤링으로 자동화 가능하도록 하는 것이 목표임.
: 그렇게 하기 위해서는 일단 각 사이트가 어떤 매커니즘으로 돌아가는지 확인해야 함.....
: 모듈 구성도, 일별 업무에 따라 다르게 돌아가야 쓸데없이 크롤링하지 않을 수 있음
    : ToDoDF -> 기관명, 사이트명(->사이트명, 사이트주소) 
        --> ** column 다 영어로 매핑하고 진행하기 **
        --> 포털 메뉴에 따라, searching.py가 다르게 작동되어야 함.
: 데이터별, 기관별, 동일 여부별 작동되는 원리가 다른만큼 여러 모듈을 혼합할 필요가 있음.
    ---> 로그인 및 검색이 필요하다면 -> se
    ---> url로 나오는 화면의 결과를 데이터화 할 때는 -> bs
    : 로 사용해야 효율적인 방법을 사용할 수 있지 않을까...
: 만약 파일 저장말고는 방법이 없다면?????
    : 사이트 예) 문화셈터 stat.mcst.go.kr
: 만약 scraping말고는 방법이 없다면?????
    : 사이트 예) 해양수산 빅데이터 플랫폼 www.vandahub.go.kr
하....진짜 누가 기관이나 공무원한테 표준 규격을 던져주었으면...짱돌던지고싶네...
경우의 수를 너무 많이 계산하다록 하면, 백퍼 중간에 힘들 듯...
    : 데이터별 se.~.Keys()를 어떻게 받아서 검색하면 좋을지
    : 
'''

# # metadata
# ORG_NAME = [
#     [], [], None, None, [], None, [], [], 
# ]
# ORG_VALS = []
# PUB_OPT = []    # pub metadata
# # filedata
# FNAME = []
# PUB_FCOL = []
# ORG_FCOL = []
# # openapi
# NAME = []
# # serialNum = 1
# I_COL = []
# O_COL = []

# # create DF and save to Dirs
# for num, task in enumerate(TASK[5:]):
#     if (ORG_NAME[num]!=None) and (PUB_OPT[num]!=None):
#         metadata = METADF(path, DAY, task)
# data = NOrMultiDF(path, DAY, TASK[1]+'.xls', index_col = [0, 1], header = [0, 1, 2])# encoding='UTF-16')#, sep='\t', index_col=[0,1])
# org_col = list(map(lambda x: '_'.join(x) if x[0]!=x[1] else '_'.join(x[1:]), data.columns))
# # org_col = list(map(lambda x: '_'.join(y.split('.')[-1] for y in x), data.index))
# # org_col = ['전체', '성별_남성', '성별_여성', '연령_15~19세', '연령_20대', '연령_30대', '연령_40대', '연령_50대', '연령_60대', '연령_70대이상', '학력_초졸 이하', '학력_중졸', '학력_고졸', '학력_대졸이상', '동거가구원수_1인', '동거가구원수_2인', '동거가구원수_3인', '동거가구원수_4인', '동거가구원수_5인 이상', '혼인상태별_미혼', '혼인상태별_기혼', '혼인상태별_사별/이혼/기타', '가구주여부_가구주', '가구주여부_가구주 아님', '종사자지위_봉급 근로자', '종사자지위_고용원을 둔 사업자', '종사자지위_고용원이 없는 자영자', '종사자지위_무급가족종사자', '종사자지위_해당없음(무직)', '가구소득_100만원 미만', '가구소득_100~200만원', '가구소득_200~300만원', '가구소득_300~400만원', '가구소득_400~500만원', '가구소득_500~600만원', '가구소득_600만원 이상', '가구소득_무응답', '지역규모_대도시', '지역규모_중소도시', '지역규모_읍면지역', '권역_수도권', '권역_강원/제주권', '권역_충청/세종권', '권역_호남권', '권역_대경권', '권역_동남권', '17개 시도_서울', '17개 시도_부산', '17개 시도_대구', '17개 시도_인천', '17개 시도_광주', '17개 시도_대전', '17개 시도_울산', '17개 시도_세종', '17개 시도_경기', '17개 시도_강원', '17개 시도_충북', '17개 시도_충남', '17개 시도_전북', '17개 시도_전남', '17개 시도_경북', '17개 시도_경남', '17개 시도_제주']
# #     data = NOrMultiDF(path, DAY, FNAME[num])
# #     pubs = metaPubFile(PUB_OPT[num])
# filedata = FILEDF(path, DAY, TASK[1], pub_fcol=org_col, org_fcol=org_col)
    # if task[:2]=='서울':    # 서울열린공공데이터면 거의 openapi가 있었음
    #     openapi = OAPIDF(path, DAY, task,)
        
# # '''
# # CheckPoint_3
# # : 저장한 데이터 중 메타데이터의 경우, 당분간은 재 확인해야 함.
# # '''

