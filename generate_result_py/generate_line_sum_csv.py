import pandas as pd

def generate_line_sum_csv(path_name):
    file_name_router = "router_prefix_sat_change.csv"
    file_name_seed = "seed_prefix_sat_change.csv"
    df_router = pd.read_csv(path_name+file_name_router)
    df_seed = pd.read_csv(path_name+file_name_seed)

    df_router["aliased prefix"] = df_router["aliased prefix"] + df_seed["aliased prefix"]
    df_router["all prefix"] = df_router["all prefix"]
    df_router["sat aliased prefix"] = df_router["sat aliased prefix"] + df_seed["sat aliased prefix"]
    df_router["sat all prefix"] = df_router["sat all prefix"] + df_seed["sat all prefix"]
    df_all = pd.DataFrame(df_router)
    # df_all.columns = ["aliased prefix", "all prefix", "sat aliased prefix", "sat all prefix"]
    df_all.to_csv(path_name+"sum_prefix_sat_change.csv", index=False)

