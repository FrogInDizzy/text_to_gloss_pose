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
import os
import sys
import subprocess
from pose_format import Pose
from pose_format.pose_visualizer import PoseVisualizer
from rich import print
from PIL import Image

def generate_pose(text, lexicon_path, output_pose_path):
    # Generate .pose file using text_to_gloss_to_pose command
    command = [
        "text_to_gloss_to_pose",
        "--text", text,
        "--glosser", "simple",
        "--lexicon", lexicon_path,
        "--spoken-language", "en",
        "--signed-language", "sgg",
        "--pose", output_pose_path
    ]
    subprocess.run(command, check=True)

def generate_gif(pose_file_path, gif_path):
    # Open and read the pose file
    with open(pose_file_path, "rb") as f:
        p = Pose.read(f.read())

    # Resize to 256, for visualization speed
    scale = p.header.dimensions.width / 256
    p.header.dimensions.width = int(p.header.dimensions.width / scale)
    p.header.dimensions.height = int(p.header.dimensions.height / scale)
    p.body.data = p.body.data / scale

    # Generate .gif
    v = PoseVisualizer(p)
    v.save_gif(gif_path, v.draw())

    # Open and display the generated GIF
    gif_image = Image.open(gif_path)
    gif_image.show()

    # Optionally print a confirmation message
    print("[bold green]GIF generated and displayed successfully![/bold green]")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_asl_gif.py '<text>'")
        sys.exit(1)

    text_input = sys.argv[1]
    lexicon_path = "/Users/wenyaogao/PycharmProjects/spoken-to-signed-translation/assets/dummy_lexicon"
    output_pose_path = "../assets/dummy_lexicon/output/pose/output_post.post"
    gif_path = "../assets/dummy_lexicon/output/gif/output_gif.gif"

    generate_pose(text_input, lexicon_path, output_pose_path)
    generate_gif(output_pose_path, gif_path)


