import numpy as np
import pandas as pd

class kr_codes:
    def __init__(self, value=None):
        self.value = value.copy()
        self.unqs = self.compiled_value()
        
    def compiled_value(self):
        from config.define.kr_len import kr_compiled
        try:    # dtype('O')
            self.value = self.value.apply(lambda x: (x.rstrip()).lstrip())
        except: # dtype('int64') or dtype('float64')
            self.value = self.value.astype(str)
            null_bucket = ["nan", "NaN", "None", "none", "na", "Na", "-"]
            self.value = self.value.apply(lambda x: "" if x in null_bucket else x)        
        compileds = self.value.apply(lambda x: kr_compiled(cell=x).cell)
        return [unq for unq in compileds.unique()]