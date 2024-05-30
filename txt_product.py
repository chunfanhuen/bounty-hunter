import openpyxl


"""
获取生成的想法内容，自动生成txt文件，并把获取的内容注入进去。

两句
"""

def export_column_to_txt(excel_file, column_letter, output_folder):
    # 打开Excel文件
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # 获取指定列的所有内容
    column_data = sheet[column_letter]

    # 创建输出文件夹（如果不存在）
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历列中的每一行，生成文本文件
    for idx, cell in enumerate(column_data):
        if cell.value is not None:
            file_name = os.path.join(output_folder, f'{idx+1}.txt')
            with open(file_name, 'w', encoding='utf-8') as txt_file:
                txt_file.write(str(cell.value))

# 使用示例
excel_file_path = r'C:\Users\SFZDSB\Desktop\想法.xlsx'  # 请替换为你的Excel文件路径
output_folder_path = r'C:\Users\SFZDSB\Desktop\想法6'      # 请替换为你的输出文件夹路径
column_to_export = 'C'                            # 要导出的列

export_column_to_txt(excel_file_path, column_to_export, output_folder_path)
