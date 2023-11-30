import pandas as pd
import numpy as np


def group_fun_org(a):
    value=[]
    # print("#######################################")
    for i in a:
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace(" ", "")
        i = i.split(",")
        value.append(i)
        # print(value)

    return a


def group_fun_as(a):
    # print(type(a))
    # print(a)
    for i in a:
        value=i
        # print(value)
        break
    # print("#######################################")
    return value


def generate_pie_sum_csv(path_name):

    prefix_types = ["sum", "router", "seed"]
    # type_names = ["AS-Num-Org", "Category-Num", "Sub_category-Num", "Org-AS-Num", "Country-Num"]
    type_names = ["as", "category", "sub_category", "org", "country"]
    for type_name in type_names:
        for day in range(1, 8):
            router_csv_file_name = f"router_prefix_day_{day}_{type_name}_sat.csv"
            seed_csv_file_name = f"seed_prefix_day_{day}_{type_name}_sat.csv"
            df_router = pd.read_csv(path_name + router_csv_file_name)
            df_seed = pd.read_csv(path_name + seed_csv_file_name)
            df_concat = pd.concat([df_router, df_seed])
            if type_name=="org":
                group_by_name="org_name"
            else:
                group_by_name=type_name
            df_group = df_concat.groupby([group_by_name])

            if type_name == "as":
                columns_list=["as",f"{type_name}_alias_num",f"{type_name}_all_num",f"{type_name}_ratio",f"sta_{type_name}_alias_num",f"sta_{type_name}_all_num",f"sat_{type_name}_ratio","org_name"]
                df_sum = df_group.agg({f"{type_name}_alias_num":np.sum,
                                       f"{type_name}_all_num":np.sum,
                                       f"{type_name}_ratio":np.sum,
                                       f"sta_{type_name}_alias_num":np.sum,
                                       f"sta_{type_name}_all_num":np.sum,
                                       f"sat_{type_name}_ratio":np.sum,
                                       'org_name': group_fun_org,
                                       })
            elif type_name == "org":
                columns_list=["org_name",f"{type_name}_alias_num",f"{type_name}_all_num",f"{type_name}_ratio",f"sta_{type_name}_alias_num",f"sta_{type_name}_all_num",f"sat_{type_name}_ratio","as"]
                df_sum = df_group.agg({f"{type_name}_alias_num":np.sum,
                                       f"{type_name}_all_num":np.sum,
                                       f"{type_name}_ratio":np.sum,
                                       f"sta_{type_name}_alias_num":np.sum,
                                       f"sta_{type_name}_all_num":np.sum,
                                       f"sat_{type_name}_ratio":np.sum,
                                       'as': group_fun_as
                                       })
            else:
                head_name=type_name.replace("sub_","")
                columns_list=[f"{type_name}",f"{head_name}_alias_num",f"{head_name}_all_num",f"{head_name}_ratio",f"sta_{head_name}_alias_num",f"sta_{head_name}_all_num",f"sat_{head_name}_ratio"]
                df_sum = df_group.agg({f"{head_name}_alias_num":np.sum,
                                       f"{head_name}_all_num":np.sum,
                                       f"{head_name}_ratio":np.sum,
                                       f"sta_{head_name}_alias_num":np.sum,
                                       f"sta_{head_name}_all_num":np.sum,
                                       f"sat_{head_name}_ratio":np.sum,
                                       })
            df_data = []
            for idx, row in df_sum.iterrows():
                if type_name == "sub_category":
                    head_name = "category"
                else:
                    head_name = type_name
                row[f"{head_name}_ratio"] = row[f"{head_name}_alias_num"] / row[f"{head_name}_all_num"]
                row[f"sat_{head_name}_ratio"] = row[f"sta_{head_name}_alias_num"] / row[f"sta_{head_name}_all_num"]
                df_data.append([idx]+row.to_list())
            df_all = pd.DataFrame(data=df_data)
            df_all.columns = columns_list
            # df_all[[f"{head_name}_ratio"]] = df_all[[f"{head_name}_alias_num"]] / df_all[[f"{head_name}_all_num"]]
            # df_all[[f"sat_{head_name}_ratio"]] = df_all[[f"sta_{head_name}_alias_num"]] / df_all[[f"sta_{head_name}_all_num"]]
            df_all.to_csv(path_name+f"sum_prefix_day_{day}_{type_name}_sat.csv",index=False)



if __name__ == '__main__':
    file_path_week1 = "../data/sat_result_20231103_20231109/"
    file_path_week2 = "../data/sat_result_20231110_20231116/"
    file_path_week3 = "../data/sat_result_20231117_20231123/"
    pathArray = [file_path_week1, file_path_week2, file_path_week3]
    for path in pathArray:
        generate_pie_sum_csv(path)
    # df_all = df_router.merge(df_seed, on=type_name, how='outer', suffixes=("_router", "_seed"))
    # df_all[f"{type_name}_alias_num"] = df_all[f"{type_name}_alias_num_router"] + df_all[f"{type_name}_alias_num_seed"]
    # df_all[f"{type_name}_all_num"] = df_all[f"{type_name}_all_num_router"] + df_all[f"{type_name}_all_num+seed"]
    # df_all[f"sta_{type_name}_alias_num"] = df_all[f"sta_{type_name}_alias_num_router"] + df_all[f"sta_{type_name}_alias_num_seed"]
    # df_all[f"sta_{type_name}_all_num"] = df_all[f"sta_{type_name}_all_num_router"] + df_all[f"sta_{type_name}_all_num_seed"]
    # df_all[f"{type_name}_ratio"] = df_all[f"{type_name}_alias_num"] / df_all[f"{type_name}_all_num"]
    # df_all[f"sta_{type_name}_ratio"] = df_all[f"sta_{type_name}_alias_num"] / df_all[f"sta_{type_name}_all_num"]
    # df_all.drop([f"{type_name}_alias_num_router",], axis=1, inplace=True)
