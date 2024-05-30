import os
import pandas as pd
"""
这个程序只是把word文档的文件命名获取并保存到excel文件里面
注意：看好文件存放路径，会自动生成excel文件。
"""

def get_word_filenames(directory):
    # 获取指定目录下的所有文件
    files = os.listdir(directory)
    # 筛选出Word文件（扩展名为 .docx 或 .doc）
    word_files = [f for f in files if f.endswith('.docx') or f.endswith('.doc')]
    return word_files


def save_filenames_to_excel(filenames, excel_path):
    # 创建一个DataFrame
    df = pd.DataFrame(filenames, columns=['Word Filenames'])
    # 将DataFrame保存到Excel文件
    df.to_excel(excel_path, index=False,engine='openpyxl')


def main():
    # 指定文件夹路径
    folder_path = r'C:\Users\SFZDSB\Documents\WXWork\1688857527541678\Cache\File\2024-05\文章'
    # 指定保存Excel文件的路径
    excel_path = r'C:\Users\SFZDSB\Documents\output1.xlsx'

    # 获取Word文件名
    word_filenames = get_word_filenames(folder_path)
    # 将文件名保存到Excel文件
    save_filenames_to_excel(word_filenames, excel_path)
    print(f"Word filenames have been saved to {excel_path}")


if __name__ == "__main__":
    main()
