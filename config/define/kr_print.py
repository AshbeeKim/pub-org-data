import numpy as np
import pandas as pd

def print_kr_csv(data, org_fcol=None, org_dtype=None):
    org_data = data.copy()
    if org_fcol is None:
        org_fcol = org_data.columns
    if org_dtype is None:
        org_dtype = [org_data[col] for col in org_fcol]
    
    col_dtype = {cols:[] for idx, cols in enumerate(col_list)}
    col_blen ={cols:[] for idx, cols in enumerate(col_list)} 
    
    fnum_col = {}
    bnum_col = {}

    for cols in col_list:
        srs = data.loc[:,cols]
        print('yes' if srs.dtype==object else 'no')
        col_dtype[cols] = srs.dtype

        blens = self.return_blen(srs.dtype, srs)
        col_blen[cols].append(np.min(np.array(blens)))
        col_blen[cols].append(np.max(np.array(blens)))

        if srs.dtypes == int:
            fnum = [len(str(num).split(',')[0]) for num in srs]
            bnum = [len(str(num).split(',')[1]) for num in srs]

            fnum_col[cols] = list(np.unique(np.array(fnum)))
            bnum_col[cols] = list(np.unique(np.array(bnum)))
        
        elif srs.dtypes == float:
            fnum = [len(str(num).split('.')[0]) for num in srs]
            bnum = [len(str(num).split('.')[1]) for num in srs]

            fnum_col[cols] = list(np.unique(np.array(fnum)))
            bnum_col[cols] = list(np.unique(np.array(bnum)))

    print(f'''\tDATA TYPE : \n{pd.Series(col_dtype).to_markdown()}\
        \n\tBYTE LENGTH : \n{pd.Series(col_blen).to_markdown()}\
        \n\tFNUM LENGTH(MIN,MAX) : \n{pd.Series(fnum_col).to_markdown()}\
        \n\tBNUM LENGTH(MIN,MAX) : \n{pd.Series(bnum_col).to_markdown()}''')