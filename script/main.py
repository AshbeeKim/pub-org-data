'''
# TASK : Compare OpenData between Public and Organization databases
# script
case 1. 파일 오류를 제외하곤, 기관 데이터는 무조건 존재함.
case 2. 동일 확장자로 중복 입력된 경우는 몰라, 아니 무엇보다 서버 터트려놓고,,,,,,휴
'''
# load library - init
import os
import numpy as nps
import pandas as pd
# load library - custom
from config.repeatContents import *
from config.loaddata import ToDoDF, NOrMultiDF, pdDPoptions
from config.savedata import METADF, FILEDF, OAPIDF

# init path
if os.getcwd().split('/')[-1]=='OpenData':
    path = os.path.join(os.getcwd(), 'script')
else:
    path = os.getcwd()
    
# init pandas options
pdDPoptions()

# update and init task
# https://performance.opendata2021.kr/newtask/index.do
# https://performance.opendata2021.kr/index.do  
## 업무 페이지 로그인 만료 화면 
    ### <- 웃긴 게 여기서 바로 접근하면, 로그인 아이디랑 비밀번호가 맞는데도 로그인이랑 비밀번호가 맞지 않다는 오류메세지가 출력됨. 어디서 끌어온 html코드로 보임

#  ID : 
    # selector ; #loginId
    # XPATH ; //*[@id="loginId"]
#   PW :
    # selector ; #loginPwd
    # XPATH ; //*[@id="loginPwd"]
#   Login : 
    # selector ; #login
    # XPATH ; //*[@id="login"]
# td.class="jobAsignDt" >>> day99로 출력되는 형식이 아님
DAYS = "day14"
# 나중에 크롤링으로 가져올 부분_1
# tbody@jobGrid
# td>a.class="data"
# a>href로 접근하면 화면이 이상하게 출력됨. selenium으로 접근해야 함.
TASKS = ["전라남도 광양시_민방위대피시설",
         "서울시 청소년 손상 및 안전의식 통계",
         "서울시립미술관 SeMA매거진 정보(영문)",
         "서울특별시 강남구 쓰레기종량제봉투판매업 인허가 정보",
         "업무상재해 부상자 및 사망자(성/산업별)_2000~2006",
         "선박스케줄 수집정보_해양수산부(해운항만물류정보센터(SP-IDC)"]
# SITE 입력하는 부분은 나중에 크롤링이 나은지, 짜증나는 데이터 정제가 빠른지 비교하고 작성
# td.class="siteNm"
SITES = ["gwangyang.go.kr/data",
         "data.seoul.go.kr",
         "data.seoul.go.kr",
         "data.seoul.go.kr",
         "gsis.kwdi.re.kr",
         "www.vadahub.go.kr"]
UpdateJSON(DAYS, TASKS, urls=SITES, path=path)
URL, DAY, SITE, TASK = NessFromJSON(path)
# URL, DAY, SITE, TASK = NessFromJSON(path, -2)

'''
CheckPoint_1
: main.ipynb "markdown"으로 확인
'''
TodayDF, idpw = ToDoDF(TASK)
print(TodayDF.to_markdown())
# # '''
# # days = "day12"
# # TASK[1] -> 보류
# # TASK[5:]
# # '''

'''
CheckPoint_2
: CheckPoint_1에 따라 작성 내용 수정
case 1. 통계면 메타데이터 작성할 필요 없음.
case 2. .shp 파일도 .dbf를 찾아서 작성하는 것을 권장하나, 없으면 생략
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

#     data = NOrMultiDF(path, DAY, FNAME[num])
#     pubs = metaPubFile(PUB_OPT[num])
#     filedata = FILEDF(path, DAY, task)
#     if task[:2]=='서울':    # 서울열린공공데이터면 거의 openapi가 있었음
#         openapi = OAPIDF(path, DAY, task,)
        
# # '''
# # CheckPoint_3
# # : 저장한 데이터 중 메타데이터의 경우, 당분간은 재 확인해야 함.
# # '''

