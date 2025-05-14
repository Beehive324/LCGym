import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    def fix_word(a):
        a = str(a)
        res = ""
        res += a[0].upper()
        for i in range(1, len(a)):
            res += a[i].lower()
        
        return res


    users['name'] = users['name'].apply(fix_word)

    return users.sort_values(by='user_id', ascending=True)


    