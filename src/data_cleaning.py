def clean_data():
    df['data'] = pd.to_datetime(df['date'])
    df.drop_duplicates(inplace= True)
    df.fillna(method= 'ffill', inplace= True)
    return df

    