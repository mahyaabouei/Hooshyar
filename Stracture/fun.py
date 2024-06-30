

def groupingTime(df):
    times = df['time'].to_list()
    df = df[df.index==df.index.min()]
    df['time'] = [times]
    df = df[['time']]
    return df