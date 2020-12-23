import json
import pandas as pd


def lambda_handler(event, context):
    data = pd.read_excel('https://hellaclestestb8d56c4974264760b616d2ac6c94bdf1151142-dev.s3.amazonaws.com/riderRank.xlsx', engine='openpyxl')
    df = pd.DataFrame(data)

    df['rank'] = 0

    for i in df.index:
        if df['alertCount'][i] / df['distance'][i] < 1:
            df['rank'][i] = df['rank'][i]
        elif df['alertCount'][i] / df['distance'][i] < 2:
            df['rank'][i] = df['rank'][i] + 10
        elif df['alertCount'][i] / df['distance'][i] < 3:
            df['rank'][i] = df['rank'][i] + 20
        elif df['alertCount'][i] / df['distance'][i] < 4:
            df['rank'][i] = df['rank'][i] + 30
        elif df['alertCount'][i] / df['distance'][i] > 4:
            df['rank'][i] = df['rank'][i] + 50

    df_user = df.groupby(by=['userID'], as_index=False).mean()
    df_user = df_user.loc[:, ['userID', 'age', 'distance', 'alertCount', 'rank']]

    for i in df_user.index:
        if df_user['rank'][i] < 10:
            df_user['rank'][i] = 'A'
        elif df_user['rank'][i] < 20:
            df_user['rank'][i] = 'B'
        elif df_user['rank'][i] < 30:
            df_user['rank'][i] = 'C'
        elif df_user['rank'][i] < 40:
            df_user['rank'][i] = 'D'
        elif df_user['rank'][i] > 40:
            df_user['rank'][i] = 'E'

    df_user.sort_values(by=['rank'], axis=0, inplace=True)
    result = df_user

    return {
        'statusCode': 200,
        'body': result.values.tolist()
    }