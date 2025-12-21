import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import os
import shutil  
# 可见光图像和红外图像的文件夹路径
rgb_folder_path =  r"G:\KeYan\DATA\VEDAI_1024\images\train_RGB"
ir_folder_path = r"G:\KeYan\DATA\VEDAI_1024\image\train_IR"
rgb_output_folder = r"G:\KeYan\DATA\VEDAI_1024\images\train"
ir_output_folder =  r"G:\KeYan\DATA\VEDAI_1024\image\train"

# 确保输出文件夹存在
if not os.path.exists(rgb_output_folder):
    os.makedirs(rgb_output_folder)
if not os.path.exists(ir_output_folder):
    os.makedirs(ir_output_folder)

# 读取文件夹中的所有文件名
rgb_image_names = [f for f in os.listdir(rgb_folder_path) if f.endswith('.png')]
ir_image_names = [f for f in os.listdir(ir_folder_path) if f.endswith('.png')]
# rgb_image_names = [f for f in os.listdir(rgb_folder_path) if f.endswith('.png')]
# ir_image_names = [f for f in os.listdir(ir_folder_path) if f.endswith('.png')]
# 确保两个文件夹中的文件名是对应的
assert set(rgb_image_names) == set(ir_image_names), "文件名不匹配"

# 参数设置
N = 20
K =10
p =5  # 假设P<K
process_ratio = 0.3 # 处理的图像比例

# 随机选择30%的图像进行处理
process_indices = random.sample(range(len(rgb_image_names)), int(len(rgb_image_names) * process_ratio))

# 批量处理图像
for i, image_name in enumerate(rgb_image_names):
    # 读取可见光图像和红外图像
    rgb_image_path = os.path.join(rgb_folder_path, image_name)
    ir_image_path = os.path.join(ir_folder_path, image_name)
    rgb_image = np.array(Image.open(rgb_image_path).convert('RGB'))
    ir_image = np.array(Image.open(ir_image_path).convert('L'))  # 假设红外图像是灰度图

    # 如果当前图像索引在处理索引列表中，则进行掩膜处理
    if i in process_indices:
        # 将图像划分为N×N个补丁
        height, width, _ = rgb_image.shape
        patch_height = height // N
        patch_width = width // N

        # 初始化存储补丁和它们平均亮度的列表
        patches_rgb = []
        brightness = []

        # 提取补丁并计算亮度
        for i in range(N):
            for j in range(N):
                patch = rgb_image[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width]
                patches_rgb.append(patch)
                # 计算亮度（这里使用简单的平均值作为示例）
                brightness.append(np.mean(patch))

        # 根据亮度排序补丁索引
        sorted_indices = np.argsort(brightness)#亮度升序排列

        # 选择暗区K（最小亮度）与亮区K（最大亮度）的 patch 索引
        top_k_indices = sorted_indices[:K]#前K个，即最小亮度值，暗区
        bottom_k_indices = sorted_indices[-K:]#亮区

        # 随机选择P个后K个补丁在RGB图像上添加掩膜
        random_indices_rgb = random.sample(bottom_k_indices.tolist(), p)

        # 创建原始图像的副本以添加掩膜
        augmented_rgb_image = rgb_image.copy()
        augmented_ir_image = ir_image.copy()

        # 暗区K个补丁，常代表黑夜，在RGB图像上对应补丁位置添加黑色的掩膜，强制学习红外特征
        for idx in top_k_indices:
            i, j = divmod(idx, N)
            augmented_rgb_image[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width] = 0
        #亮区K个补丁，常代表白天，应多学习可见光信息，但考虑强光和曝光，应综合学习可见光和红外模态
        # 对于随机选择的P个后K个补丁，在RGB图像上添加掩膜
        for idx in random_indices_rgb:
            i, j = divmod(idx, N)
            augmented_rgb_image[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width] = 0

        # 对于剩余的K-P个后K个补丁，在红外图像上添加掩膜
        remaining_indices_ir = [idx for idx in bottom_k_indices.tolist() if idx not in random_indices_rgb]
        for idx in remaining_indices_ir:
            i, j = divmod(idx, N)
            augmented_ir_image[i*patch_height:(i+1)*patch_height, j*patch_width:(j+1)*patch_width] = 0

        # 保存增强后的图像
        plt.imsave(os.path.join(rgb_output_folder, image_name), augmented_rgb_image)
        plt.imsave(os.path.join(ir_output_folder, image_name), augmented_ir_image, cmap='gray')
    else:
        # 如果当前图像不在处理索引列表中，则直接复制原始图像到输出文件夹
        shutil.copy(rgb_image_path, os.path.join(rgb_output_folder, image_name))
        shutil.copy(ir_image_path, os.path.join(ir_output_folder, image_name))