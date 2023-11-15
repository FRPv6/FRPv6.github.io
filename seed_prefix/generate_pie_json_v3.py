import pandas as pd
import json
import re

select_num=9
prefix_type="seed"
column_name ='ratio of aliased prefix'

csv_file_name_5=f"{prefix_type}_prefix_day_5_sub_category_sat.csv"
csv_file_name_4=f"{prefix_type}_prefix_day_5_org_sat.csv"
csv_file_name_3=f"{prefix_type}_prefix_day_5_country_sat.csv"
csv_file_name_2=f"{prefix_type}_prefix_day_5_category_sat.csv"
csv_file_name_1=f"{prefix_type}_prefix_day_5_as_sat.csv"


pic_name_5="Sub_category-Num"
pic_name_4="Org-AS-Num"
pic_name_3="Country-Num"
pic_name_2="Category-Num"
pic_name_1="AS-Num-Org"

# Assuming prefix_type is defined somewhere before this code snippet

# Define the pattern to extract the number after "prefix_day_"
pattern = re.compile(r"prefix_day_(\d+)_")

for i in range(1, 6):
    # Extract the number from the variable name using the defined pattern
    match = pattern.search(globals()[f'csv_file_name_{i}'])

    if match:
        day_number = match.group(1)
        csv_file_name = f"{prefix_type}_prefix_day_{day_number}_{globals()[f'pic_name_{i}'].lower()}_sat.csv"

        # Your code here, you can use csv_file_name as a variable in your code

        pic_name = globals()[f'pic_name_{i}']

        # Your code here, you can use pic_name as a variable in your code

        # Example: Printing the current file name and picture name
        print(f"Processing CSV File: {csv_file_name}, Picture Name: {pic_name}")
    else:
        print(f"Error: Unable to extract day number from {globals()[f'csv_file_name_{i}']}")