from prittier import print_df
import pandas as pd

df = pd.read_csv("./pandas/lol.csv", sep="\t")

print_df(df.columns)