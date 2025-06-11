import pandas as pd
import os
import XLSX_Deal

def XLS_Deal(File_Path):
    with open(File_Path, 'rb') as f:
        header = f.read(100)

    # 如果是 HTML 文件，则使用 read_html 解析
    if b'<html' in header.lower():
        print("检测到 HTML 文件格式，尝试提取表格")
        print("(徐工汉云的历史工况xls文件实际是html文件，需要先转换成同名XLSX文件)")
        tables = pd.read_html(File_Path)
        if tables:
            dir_path = os.path.dirname(File_Path)
            file_name = os.path.basename(File_Path)
            new_file = os.path.join(dir_path, os.path.splitext(file_name)[0] + ".xlsx")

            with pd.ExcelWriter(new_file) as writer:
                for i, df in enumerate(tables):
                    sheet_name = f"Sheet{i + 1}"
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            XLSX_Deal.XLSX_Deal(new_file)
        else:
            print("文件中没有表格数据")
    else:
        print("文件格式异常！")