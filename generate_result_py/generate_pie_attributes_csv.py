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
def generate_pie_attributes_csv(path_name):
    prefix_types = ["all", "router", "seed"]
    type_names = ["AS-Num-ORG", "CGBC-Num", "FGBC-Num", "ORG-AS-Num", "Country-Num"]
    type_names = ['as','category','sub_category','org_name','country']
    # Iterate through different combinations
    for prefix_type in prefix_types:
        csv_file_name = f"{prefix_type}_six_month_64.csv"
        df=pd.read_csv(path_name+csv_file_name)
        for type_name in type_names:
            if type_name == 'as':
                df1=df.groupby([type_name]).sum(numeric_only = True)
                df2=df.groupby([type_name])['org_name'].apply(set)
                df_data=df1.merge(df2,how='inner',on='as')
                as_list=df_data.index.tolist()
                df_data.index = [int(i) for i in as_list]
                df_data.index.name='as'
                org_name_list=df_data['org_name'].tolist()
                org_name=[]
                for org_line in org_name_list:
                    value_list=[i for i in org_line]
                    org_name.append(value_list[0])
                df_data['org_name']=org_name
                print(df_data['alias_prefix_num'].sum(),df_data['alias_prefix_64_num'].sum())
                df_data['alias_prefix_ratio']=df_data['alias_prefix_num']/df_data['alias_prefix_num'].sum()
                df_data['alias_prefix_64_ratio']=df_data['alias_prefix_64_num']/df_data['alias_prefix_64_num'].sum()
            elif type_name == 'org_name':
                df1=df.groupby([type_name]).sum(numeric_only = True)
                df2=df.groupby([type_name])['as'].apply(set)
                df_data=df1.merge(df2,how='inner',on='org_name')
                as_y_list=df_data['as_y'].tolist()
                as_y=[]
                for as_line in as_y_list:
                    value_list=[int(i) for i in as_line]
                    as_y.append(value_list)
                df_data['as_y']=as_y
                df_data.index.name='org_name'
                df_data['alias_prefix_ratio']=df_data['alias_prefix_num']/df_data['alias_prefix_num'].sum()
                df_data['alias_prefix_64_ratio']=df_data['alias_prefix_64_num']/df_data['alias_prefix_64_num'].sum()
                print(df_data['alias_prefix_num'].sum(),df_data['alias_prefix_64_num'].sum())
            else:
                df_data=df.groupby([type_name]).sum(numeric_only = True)
                df_data.index.name=type_name
                df_data['alias_prefix_ratio']=df_data['alias_prefix_num']/df_data['alias_prefix_num'].sum()
                df_data['alias_prefix_64_ratio']=df_data['alias_prefix_64_num']/df_data['alias_prefix_64_num'].sum()
                print(df_data['alias_prefix_num'].sum(),df_data['alias_prefix_64_num'].sum())
            df_data.to_csv(path_name+f"{prefix_type}_six_month_"+type_name+'.csv')
