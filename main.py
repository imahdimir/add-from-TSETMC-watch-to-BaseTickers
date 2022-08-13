##

import pandas as pd
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import read_data_according_to_type as rdata
from mirutil.funcs import save_df_as_a_nice_xl as sxl


btic = 'BaseTicker'

def main() :

  pass

  ##


  df = rdata('Unique-BaseTickers-TSETMC.xlsx')
  ##
  df1 = rdata('watch-14010522.xlsx')
  ##
  df1 = df1.applymap(norm)
  ##
  df2 = df1[~ df1['نماد'].isin(df[btic])]
  ##
  df1 = df1.rename(columns = {
      'نماد' : 'BaseTicker'
      })
  ##
  df = pd.concat([df , df1])
  ##
  df = df.drop_duplicates()
  ##
  df = df.sort_values(btic)
  ##
  sxl(df , 'out.xlsx')


  ##


  ##

##


if __name__ == "__main__" :
  main()