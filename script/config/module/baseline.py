from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPub:
    def __init__(self, keyword, driver_path=None, driver_option=None):
        # driver_option는 조정 이후에 제거하기!!!!!
        self.url = "https://www.data.go.kr/"
        self.keyword = self.encoded(keyword)
        try:
            self.driver = webdriver.Chrome(executable_path=driver_path, options=driver_option)
        except:
            self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
            print("임의로 설정한 경로는 '/usr/local/bin/chromedriver/'이며, 어떠한 옵션도 설정하지 않았습니다.")
        
    def encoded(keyword):
        # 당장 내일부터 다시 업무가 바뀐다고 하던데,.,.하....
        return keyword
        # repeatContents로 옮겨야할지
# filedata        
# https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EC%82%B0%EB%A6%BC%EC%9E%AC%ED%95%B4+%EA%B4%80%EC%8B%AC%EC%9D%B8%EA%B5%AC+%EC%A0%95%EB%B3%B4&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=
# openapi
# https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%82%B0%EB%A6%BC%EC%9E%AC%ED%95%B4+%EA%B4%80%EC%8B%AC%EC%9D%B8%EA%B5%AC+%EC%A0%95%EB%B3%B4&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=

# 상세검색
# #layer_search_more > div.layer-contents > div