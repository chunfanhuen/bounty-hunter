import os
import shutil
import pandas as pd
from natsort import natsorted


def process_files(source_folder, dest_base_folder, questions_excel, titles_excel):
    # Step 1: Get the naturally sorted list of .docx files
    docx_files = natsorted([f for f in os.listdir(source_folder) if f.endswith('.docx')])
    if len(docx_files) < 120:
        raise ValueError("Not enough .docx files in the source folder")

    # Step 2: Create destination folders and move 60 .docx files to each of the new folders
    folder_count = (len(docx_files) + 59) // 60  # Calculate number of folders needed
    for i in range(folder_count):
        dest_folder = f"{dest_base_folder}/Folder_{i + 1}"
        os.makedirs(dest_folder, exist_ok=True)
        for j in range(60):
            file_index = i * 60 + j
            if file_index < len(docx_files):
                src_path = os.path.join(source_folder, docx_files[file_index])
                dest_path = os.path.join(dest_folder, docx_files[file_index])
                shutil.move(src_path, dest_path)

    # Step 3: Read the A columns from the Excel files
    df_questions = pd.read_excel(questions_excel, usecols=[0], header=None)
    df_titles = pd.read_excel(titles_excel, usecols=[0], header=None)

    if len(df_questions) < 120 or len(df_titles) < 120:
        raise ValueError("Not enough rows in the Excel files")

    for i in range(folder_count):
        dest_folder = f"{dest_base_folder}/Folder_{i + 1}"

        # Create txt file for questions with UTF-8 encoding
        questions = df_questions.iloc[i * 60:(i + 1) * 60].squeeze().tolist()
        with open(os.path.join(dest_folder, 'questions.txt'), 'w', encoding='utf-8') as f:
            for question in questions:
                f.write(str(question) + '\n')

        # Create txt file for titles with UTF-8 encoding
        titles = df_titles.iloc[i * 60:(i + 1) * 60].squeeze().tolist()
        with open(os.path.join(dest_folder, 'titles.txt'), 'w', encoding='utf-8') as f:
            for title in titles:
                f.write(str(title) + '\n')


# Example usage:
source_folder = r'C:\Users\14534\Desktop\output'
dest_base_folder = r'C:\Users\14534\Documents'
questions_excel = r'C:\Users\14534\PycharmProjects\zhihu_hottitle_spider\zhihu_hot.xlsx'
titles_excel = r'C:\Users\14534\Desktop\title.xlsx'

process_files(source_folder, dest_base_folder, questions_excel, titles_excel)
