import os
import openpyxl
from docx import Document
# 配置部分
folder_path = r'C:\Users\SFZDSB\Desktop\文章5'  # 文章所在的文件夹路径
excel_path = r'C:\Users\SFZDSB\Desktop\domain name.xlsx'  # 存储域名的Excel文件路径
domain_column = 'A'  # 域名所在的Excel列
articles_per_domain = 5  # 每个域名添加到几篇文章中

# 读取Excel文件中的域名
wb = openpyxl.load_workbook(excel_path)
sheet = wb.active
domains = [cell.value for cell in sheet[domain_column] if cell.value]

# 打印域名和数量
print("读取到的域名：", domains)
print("域名数量：", len(domains))

# 获取文件夹中的所有.docx文章文件
articles = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.docx')]

# 打印文章文件和数量
print("读取到的文章文件：", articles)
print("文章文件数量：", len(articles))

# 确保域名数量和文章数量匹配
if len(domains) * articles_per_domain != len(articles):
    raise ValueError("文章数量与域名数量不匹配。请检查配置。")

# 为每篇文章添加对应的域名
for i, article_path in enumerate(articles):
    document = Document(article_path)
    domain = domains[i // articles_per_domain]
    document.add_paragraph(f"想了解更多文章：{domain}")
    document.save(article_path)

print("操作完成，每篇文章已添加相应的域名。")