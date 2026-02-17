import pandas as pd

old = pd.read_csv('/Users/msizemor/dgen/dgen_os/input_data/elec_prices/ATB23_Mid_Case_retail.csv')

new = pd.read_csv('/Users/msizemor/dgen/dgen_os/input_data/elec_prices/rate_projections_aeo25.csv')


# check relevant ba values from old version
mask = new['ba'].isin(old['ba'])
match = new[mask]

print(match.loc[(match['ba']=='p1')&(match['year']==2026)])
print(len(new))
print(len(old))