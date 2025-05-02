import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    res = world.query("area >= 3000000 or population >= 25000000")

    return res[['name', 'population', 'area']] #return the specified dataframes

    
    