import pandas as pd
import re
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    
    valid = users[(users['mail'].str.match(r'[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$'))]


    return valid

    