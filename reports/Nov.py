import os
import numpy as np
import pandas as pd
'''
A 의 대출 금리 = 변동금리(CD금리 + 2%)
대출 기한 : 5년
시작일 : 2016-01-04
대출금 : 10,000,000(일시상환 대출)
상환일 : 2020-12-30
################################
1. 기간 내 A의 대출 금리/(월) <- 꺽은선 그래프
2. 기간 내 A의 납입 이자금액/(월) <- 막대 그래프
3. 총 납입한 이자금액
### 변동 금리 주기, 이자 납입일 제공 없음 -> 평균
### 근거 : CD금리 자체가 [11:30, 15:30] 10개 금융사의 금리의 최고 금리, 최저 금리, 평균값 제공.
### c.f. LTV, DTI, newDTI, DSR
######## 만기일시 상환방식, 원리금 균등 상환방식, 원금 균등 상환방식
        상기의 과제는 만기일시 상환방식의 단점을 보기 위함인지는 모르겠으나, 전제 조건이 당황스럽긴 함.
        시작일을 기준점으로 잡고, 매월 4일에 변동 금리에 해당하원 이자를 납입하는 것이 보편적(CD)이나,
        이자 납일일에 대한 정보가 제공되지 않았기에, 우선은 각 월의 평균값으로 대체
        정답 범위 : 175만 원 +- (from 매니저)
################################
제출 양식 : pdf, A4
필수 기재사항 :  학습조직, 이름, ID
그들의 의도따위...알 게 뭐람....
'''
##### init #####
path = os.path.join(os.getcwd(), 'reports/2차추가_엑셀데이터분석과제_이름_ID.xlsx')
fdata = pd.read_excel(path, sheet_name="CD금리")#, usecols=col_func)
fdata = fdata.iloc[:-1, :]
fdata = fdata.T
data_info = fdata.iloc[:4, :]
fdata = fdata.iloc[4:, :]
fdata = fdata[(fdata.index>="2016/01/04")&(fdata.index<='2020/12/30')]
fdata.rename(columns={0:"CD금리"}, inplace=True)

principal = 10000000
cvtP = principal / 100
fdata['YYYY'] = [yr.split('/')[0] for yr in fdata.index]
fdata['MM'] = [m.split('/')[1] for m in fdata.index]
fdata['DD'] = [dt.split('/')[-1] for dt in fdata.index]
fdata.reset_index(drop=True, inplace=True)

##### pivot table #####
'''
    ## 월별 mean, mean + adds
    # CD금리 ==> 연금리
    # len <- days
'''
meanPivot = pd.pivot_table(fdata, index=['YYYY', 'MM'], values=['CD금리'], aggfunc=["mean", len]).reset_index()
meanPivot.columns = list(map(lambda x: '_'.join(x) if len(x)>=2 else str(x), meanPivot.columns))
# floating interest per mont림
meanPivot['interests'] = meanPivot['mean_CD금리'].apply(lambda x: (x+2.)/12)
# interest amount per month(%->decimal->*pricipal)
    # 한국 화폐 단위는 소숫점이 없음 -> 반올림
meanPivot['amounts'] = meanPivot['interests'].apply(lambda x: np.ceil(x * cvtP))
print(meanPivot)
TotalI = sum(meanPivot['amounts'])
print(TotalI)

#################################### 재확인 및 시작 범위 ####################################
# double check
# data.iloc[0,len_CDI], data.iloc[-1, len_CDI]로 확인한 바로는 현재까지 이상없음
# 그래도 시각화 하기 전, 날짜 계산과 피벗테이블로 구한 월 카운트, 일 카운트로 제대로 작성했는지 확인해 볼 것!!!
print(meanPivot.shape[0])
print(sum(meanPivot['len_CD금리']))

# visualization 
# 아직 라이브러리 정하질 못함. 주말에 시각화나 정리해야겠음
fname = '[11월과제]_전공_학304_김수빈_서울1센터'
# pdf, A4, infos