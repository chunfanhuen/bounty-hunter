import os
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

"""
调整生成文章的格式并且删掉内容第一个的标题（如果有的话）
"""
def set_font_to_songti(doc):
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.font.name = '宋体'
            run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
            run.font.size = Pt(12)  # 小四

def process_docx_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            doc = Document(file_path)

            set_font_to_songti(doc)


            # Save the modified document
            doc.save(file_path)


# 指定文件夹路径
folder_path = r'C:\Users\SFZDSB\Desktop\文章5'

# 处理文件夹中的所有docx文件
process_docx_files(folder_path)
