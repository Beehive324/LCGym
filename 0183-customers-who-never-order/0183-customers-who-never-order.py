import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    res = customers.query('id not in @orders.customerId')

    res['Customers'] = res['name']

    res = res.drop(columns=['id', 'name'])

    return res
    