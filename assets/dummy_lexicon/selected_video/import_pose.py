# !/opt/homebrew/bin/python3.9
# -*- coding: utf-8 -*-
"""
@Author         :  Edwin Gao
@Version        :  macos 14.0, python3.9
------------------------------------
@IDE            ： PyCharm
@Description    :  
@CreateTime     :  7/1/24 7:50 PM
------------------------------------
"""

import os
import shutil

# 定义文件路径
source_directory = '/Users/wenyaogao/Desktop/123/pose'  # 源文件夹路径
pose_directory = '/Users/wenyaogao/PycharmProjects/spoken-to-signed-translation/assets/dummy_lexicon/sgg'  # 存放.pose文件的目标文件夹路径
mp4_directory = '/Users/wenyaogao/Desktop/123/video'  # 存放.mp4文件的目标文件夹路径

# 创建目标目录（如果不存在）
os.makedirs(pose_directory, exist_ok=True)
os.makedirs(mp4_directory, exist_ok=True)

# 遍历源文件夹中的文件
for filename in os.listdir(source_directory):
    source_file_path = os.path.join(source_directory, filename)

    # 判断是否是文件（而不是目录）
    if os.path.isfile(source_file_path):
        if filename.endswith('.pose'):
            # 构建.pose文件的目标路径
            target_file_path = os.path.join(pose_directory, filename)
            # 移动.pose文件
            shutil.move(source_file_path, target_file_path)
            print(f'Moved {source_file_path} to {target_file_path}')
        elif filename.endswith('.mp4'):
            # 构建.mp4文件的目标路径
            target_file_path = os.path.join(mp4_directory, filename)
            # 移动.mp4文件
            shutil.move(source_file_path, target_file_path)
            print(f'Moved {source_file_path} to {target_file_path}')

print('All files have been processed.')
