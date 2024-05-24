import pandas as pd
import json
from datetime import datetime, timedelta
from config import DefaultConfig
config = DefaultConfig()
type_name_dict = {
    "AS-Num-Org": "AS-Num-Org",
    "CGBC-Num": "CGBC-Num",
    "FGBC-Num": "FGBC-Num",
    "ORG-AS-Num": "AS-Num-Org",
    "Country-Num": "Country-Num"
}
def generate_pie_64_csv(path_name):
    prefix_types = ["all", "router", "seed"]
    for prefix_type in prefix_types:
        csv_file_name = f"{prefix_type}_six_month.csv"
        csv_64_file_name= f"{prefix_type}_six_month_64.csv"
        df=pd.read_csv(path_name+csv_file_name)
        alias_prefix_64_num_list=[]
        alias_prefix_num_list=[]
        for item in df['alias_prefix']:
            alias_prefix_64=item.split("/")[-1]
            alias_prefix_64=pow(2,64-int(alias_prefix_64))
            alias_prefix_64_num_list.append(alias_prefix_64)
            alias_prefix_num_list.append(1)
        df['alias_prefix_num']=alias_prefix_num_list
        df['alias_prefix_64_num']=alias_prefix_64_num_list
        df.to_csv(path_name+csv_64_file_name,index=False)

