import pandas 
from ek_1_2.assignment_1_2 import convert_names_bd
df = pandas.DataFrame({"abbrev": ["DHK", "BAR", "CTG", "SYL"]})
full_df = convert_names(df)
print(full_df.head())