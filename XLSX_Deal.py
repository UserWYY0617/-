import pandas as pd

def XLSX_Deal(File_Path):
    df = pd.read_excel(File_Path, dtype={'电池包SOC(%)': str,})
    new_df = pd.DataFrame(columns=df.columns)

    charge = 0
    charge_row = []
    charge_num = 0
    soc_delay = 0
    soc = 0
    for index, row in df.iterrows():
        if row['电池包SOC(%)']!= '-':
            soc_delay = soc
            soc = float(row['电池包SOC(%)'])
            if soc_delay>soc:
                charge = 1
                charge_num = 0
                new_df = pd.concat([new_df, row.to_frame().T], ignore_index=True)
            elif soc_delay<soc:
                charge = 0
            else:
                if charge == 1&charge_num<10:
                    new_df = pd.concat([new_df, row.to_frame().T], ignore_index=True)
                    charge_num=charge_num+1
    with pd.ExcelWriter('D:\\charge.xlsx') as writer:
        new_df.to_excel(writer, sheet_name='sheet', index=False)