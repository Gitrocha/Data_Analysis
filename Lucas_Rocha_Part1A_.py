import pandas as pd
from pathlib import Path
import time as t
import numpy as np
import re


def mph_to_kmh(field):
    try:
        return round(1.609*float(re.findall('\d+', field)[0]), 1)
    except:
        return 'NaN'

print('\n* Configuration of System and Paths')
pd.options.mode.chained_assignment = None  # default='warn'
basepath = Path('.')
input_file = basepath / 'data' / 'DataFrame1.csv'
output_file = basepath / 'data' / 'Lucas_Rocha_Part1A_.csv'
print('  - Outputs path: ', output_file)

print('\n* Reading Dataframe')
df = pd.read_csv(input_file, sep=',', encoding='utf8', na_values=np.nan)
df_aux = df.copy()

print('\n* Aplying data Treatment')
df_aux['Production_Years'].replace(' ', '', regex=True, inplace=True)
df_aux.replace('\n', '', regex=True, inplace=True)
df_aux.drop_duplicates(subset='Name', keep="last", inplace=True)

print("\n* Creation of new column 'Top_Speed_KMH_1DEC'")
print("  - Missing information about speed replaced by 'NaN'")
df_aux['Production_Start'], df_aux['Production_End'] = df_aux['Production_Years'].str.split('-', 1).str
df_aux['Top_Speed_KMH_1DEC'] = df_aux['Top Speed_Text'].apply(lambda field: mph_to_kmh(field))

print('\n* Missing data treatment')
df_aux['Production_End'].replace('', np.nan, regex=True, inplace=True)
df_null = df_aux[(df_aux['Production_End'].isnull() | df_aux['Production_Start'].isnull())]
df_ok = df_aux[~(df_aux['Production_End'].isnull() | df_aux['Production_Start'].isnull())]
# TODO: Add dictionary of Production years after new reasearch. Assumptions: Start, End = 2009, 2019
df_null['Production_End'].replace(np.nan, 2019, regex=True, inplace=True)
df_null['Production_Start'].replace(np.nan, 2009, regex=True, inplace=True)
df_final = pd.concat([df_null, df_ok], axis=0)
df_final = df_final.astype({'Production_End': int,
                            'Production_Start': int})
# Data treatment of empty fields
df_final['Comments'].replace(np.nan, 'NaN', regex=True, inplace=True)
df_final['Production_Years'].replace(np.nan, 'NaN', regex=True, inplace=True)
df_final['Top Speed_Text'].replace(np.nan, 'NaN', regex=True, inplace=True)
df_final['Top_Speed_KMH_1DEC'].replace('NaN', 0, regex=True, inplace=True)

print('  - Assumptions of missing years: Start, End = 2009, 2019')
print('  - Assumptions of missing speed info: Top speed = 0')

df_final['Production_Period'] = df_final['Production_End'] - df_final['Production_Start']


print("\n* Saving final dataframe at 'data' folder inside root project folder")
df_final.to_csv(output_file, sep=';', encoding='utf8', index=False)

print("\n* Process finished. Read CSV output file encoded as default UTF-8. Column separator type = ';'.")
print('\n* Closing app')
print('\n* ...')
t.sleep(20)
