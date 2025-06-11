import pandas as pd
import os
import traceback
import XLS_Deal
import XLSX_Deal

# 主程序
if __name__ == "__main__":
    file_path = input("请输入历史工况的xls文件或者xlsx文件路径: ").strip()
    if not os.path.isfile(file_path):
        print("文件不存在或者已加密")
    else:
        file_path_end = os.path.splitext(file_path)[1][1:]
        if file_path_end == 'xls':
            XLS_Deal.XLS_Deal(file_path)
        elif file_path_end == 'xlsx':
            XLSX_Deal.XLSX_Deal(file_path)
        else:
            print("输入文件类型不匹配")
