# !/opt/homebrew/bin/python3.9
# -*- coding: utf-8 -*-
"""
@Author         :  Edwin Gao
@Version        :  macos 14.0, python3.9
------------------------------------
@IDE            ： PyCharm
@Description    :  
@CreateTime     :  7/1/24 8:19 PM
------------------------------------
"""

import os
import csv

# 定义文件路径
source_directory = '../sgg/'  # 存放.pose文件的源文件夹路径
csv_file_path = '/Users/wenyaogao/PycharmProjects/spoken-to-signed-translation/assets/dummy_lexicon/index.csv'

# 读取现有的CSV文件内容
csv_rows = []
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        csv_rows = list(reader)

# 添加新的.pose文件信息到CSV文件内容
for filename in os.listdir(source_directory):
    if filename.endswith('.pose'):
        # 获取单词和gloss
        word = filename[:-5]  # 去掉文件后缀.pose
        gloss = word.upper()

        # 构建新行
        new_row = [
            f'sgg/{filename}',  # path
            'en',               # spoken_language
            'sgg',              # signed_language
            '0',                # start
            '0',                # end
            word,               # words
            gloss,              # glosses
            '0'                 # priority
        ]
        csv_rows.append(new_row)

# update with new content
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_rows)

print('All .pose files have been imported into the CSV file.')
