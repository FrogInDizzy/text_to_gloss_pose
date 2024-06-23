# !/opt/homebrew/bin/python3.9
# -*- coding: utf-8 -*-
"""
@Author         :  Edwin Gao
@Version        :  macos 14.0, python3.9
------------------------------------
@IDE            ： PyCharm
@Description    :  
@CreateTime     :  6/19/24 9:29 PM
------------------------------------
"""
from pose_format import Pose
from pose_format.pose_visualizer import PoseVisualizer
from rich import print
from PIL import Image

# Open and read the pose file
pose_file_path = "/Volumes/Untitled/video2.pose"
with open(pose_file_path, "rb") as f:
    p = Pose.read(f.read())

# Resize to 256, for visualization speed
scale = p.header.dimensions.width / 256
p.header.dimensions.width = int(p.header.dimensions.width / scale)
p.header.dimensions.height = int(p.header.dimensions.height / scale)
p.body.data = p.body.data / scale

# Generate .gif
gif_path = "/Users/wenyaogao/Desktop/video1.gif"
v = PoseVisualizer(p)
v.save_gif(gif_path, v.draw())

# Open and display the generated GIF
gif_image = Image.open(gif_path)
gif_image.show()

# Optionally print a confirmation message
print("[bold green]GIF generated and displayed successfully![/bold green]")

