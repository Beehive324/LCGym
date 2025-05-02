import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    out = views.query("author_id == viewer_id")
    out = out.sort_values(by="author_id",ascending=True)
    out['id'] = out['author_id']
    out = out.drop(columns =['article_id','viewer_id', 'view_date', 'author_id'])

    out = out.drop_duplicates()

    return out

  

    