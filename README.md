# C2DFF-Net
Codes for C2DFF-Net for Object Detection in Multimodal Remote Sensing Images.
Yue Zhang, Jinbao Chen, Jianyuan Wang*, Donghao Shi, Shu Han, and Lixiao Deng


---yolov8-twoCSP-64.yaml---

Baseline model architecture configuration.

---C2DFF.yaml---

Network configuration for the proposed C2DFF-Net.

---block.py---

Implements the two core modules proposed in the paper: CDFIM and CGSA.
Both modules are designed to be plug-and-play, allowing for easy integration into other deep learning models with minimal modification.

---ALM.py

The proposed Adaptive Light-Aware Mask (ALM) method for training dual-modal models.


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
