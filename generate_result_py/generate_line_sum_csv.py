import os

import pandas as pd

def generate_line_sum_csv(path_name):
    file_name_router = "router_frp.csv"
    file_name_seed = "seed_frp.csv"
    df_router = pd.read_csv(path_name+file_name_router)
    df_seed = pd.read_csv(path_name+file_name_seed)

    df_router["frp"] = df_router["frp"] + df_seed["frp"]
    df_all = pd.DataFrame(round(df_router,2))
    df_all.columns = ["frp"]
    df_all.to_csv(path_name+"sum_frp.csv", index=False)

    file_name_router_64 = "router_frp_64.csv"
    file_name_seed_64 = "seed_frp_64.csv"
    df_router_64 = pd.read_csv(path_name+file_name_router_64)
    df_seed_64 = pd.read_csv(path_name+file_name_seed_64)

    df_router_64["frp"] = df_router_64["frp"] + df_seed_64["frp"]
    df_all_64 = pd.DataFrame(round(df_router_64,2))
    df_all_64.columns = ["frp"]
    df_all_64.to_csv(path_name+"sum_frp_64.csv", index=False)

