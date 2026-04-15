# C2DFF-Net
Codes for C2DFF-Net for Object Detection in Multimodal Remote Sensing Images.
Yue Zhang, Jinbao Chen, Jianyuan Wang*, Donghao Shi, Shu Han, and Lixiao Deng

---C2DFF.ZIP---
Complete usable project code

---yolov8-twoCSP-64.yaml---

Baseline model architecture configuration.

---C2DFF.yaml---

Network configuration for the proposed C2DFF-Net.

---block.py---

Implements the two core modules proposed in the paper: CDFIM(CPCA_CF) and CGSA(PolarizedSelfAttention_Channel).
Both modules are designed to be plug-and-play, allowing for easy integration into other deep learning models with minimal modification.

---ALM.py

The proposed Adaptive Light-Aware Mask (ALM) method for training dual-modal models.

Datasets：

---VEDAI---
通过网盘分享的文件：VEDAI_1024.zip
链接: https://pan.baidu.com/s/1Nd6GL2honyIH8LSBwrxjiA?pwd=asdf 提取码: asdf 
--来自百度网盘超级会员v5的分享

---DroneVehicle---
通过网盘分享的文件：DroneVehicle
链接: https://pan.baidu.com/s/1XsxCT0cKuz8MbsGH3m50PA?pwd=asdf 提取码: asdf 
--来自百度网盘超级会员v5的分享

---FLIR---
通过网盘分享的文件：FLIR-align-3class
链接: https://pan.baidu.com/s/1oSJJBOox9Q2obwIPP6agFw?pwd=asdf 提取码: asdf 
--来自百度网盘超级会员v5的分享

<img width="1193" height="224" alt="image" src="https://github.com/user-attachments/assets/f71c9700-91d1-479f-950f-927d1baaeae0" />


![image](https://github.com/user-attachments/assets/ca54e8e6-2d8b-4b8f-8259-af924938a205)
![image](https://github.com/user-attachments/assets/782ec178-f05e-44fa-a1bf-d96e2177a9cc)

If our code is helpful to you, please cite:

@ARTICLE{11180153,
  author={Zhang, Yue and Chen, Jinbao and Wang, Jianyuan and Shi, Donghao and Han, Shu and Deng, Lixiao},
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  title={C2DFF-Net for Object Detection in Multimodal Remote Sensing Images}, 
  year={2025},
  volume={63},
  number={},
  pages={1-16},
  doi={10.1109/TGRS.2025.3614295}}
