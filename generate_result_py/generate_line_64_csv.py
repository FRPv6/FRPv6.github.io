import os
import pandas as pd
from datetime import datetime, timedelta
def generate_line_router_64_csv(router_prefix,path_name):
    data_frp_list=[]
    directory_name_prefix='month_'
    month_days_dict={
        "1":28,#11
        "2":30,#12
        "3":31,#1
        "4":29,#2
        "5":29,#3
        "6":30#4
    }
    file_name_prefix='router_prefix_day_'
    for month in range(1,7):
        directory_name=directory_name_prefix+str(month)+'/'
        days=month_days_dict[str(month)]
        for day in range(1,days+1):
            file_name=file_name_prefix+str(day)+'.txt'
            with open(router_prefix+directory_name+file_name) as f:
                datas=f.readlines()
            num_sum=0
            for line in datas:
                line_list=line.split(',')
                prefix=line_list[0]
                prefix_num=prefix.split('/')
                num=128-int(prefix_num[-1])
                num_sum+=pow(2,num)
            num_sum=num_sum/pow(2,64)
            num_sum_conversion=round(num_sum*pow(10,-9),2)#10^9单位换算
            data_frp_list.append(num_sum_conversion)
    data_df=pd.DataFrame(data=data_frp_list)
    data_df.columns=['frp']
    data_df.to_csv(path_name+'router_frp_64.csv',index=False)

def generate_line_seed_64_csv(seed_prefix,path_name):
    data_frp_list=[]
    file_name_list=os.listdir(seed_prefix)
    file_name_list.sort()
    flag=False
    for file in file_name_list:
        file_name=file.split('.')[0]
        date_list=file_name.split('_')
        start_date = datetime.strptime(date_list[-2], "%Y%m%d")
        end_date = datetime.strptime(date_list[-1], "%Y%m%d")
        intervals=end_date-start_date
        days=intervals.days+1
        with open(seed_prefix+file) as f:
            datas=f.readlines()
        num_sum=0
        sum=0
        for line in datas:
            prefix_num=line.split('/')
            num=128-int(prefix_num[-1])
            sum=sum+num
            num_sum+=pow(2,num)
        num_sum=num_sum/pow(2,64)
        num_sum_conversion=round(num_sum*pow(10,-9),2)#10^9单位换算
        # print(days,num_sum_conversion,num_sum)
        num_sum_list=[num_sum_conversion]*days
        data_frp_list=data_frp_list+num_sum_list
    data_df=pd.DataFrame(data=data_frp_list)
    data_df.columns=['frp']
    data_df.to_csv(path_name+'seed_frp_64.csv',index=False)
