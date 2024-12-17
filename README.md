# MRAnnotator: Multi-Anatomy and Many-Sequence MRI Segmentation of Forty-four Structures
MRAnnotator is a tool for segmenting 44 anatomical structures in MR images across various sequences. A holdout independent test dataset can be downloaded here: .

Main classes for MRAnnotator:
![Alt text](resources/label_figure.png)

# Installation
The model weights of MRAnnotator can be downloaded via the request: . 

Package dependency:
* Python >= 3.9
* [Pytorch](http://pytorch.org/) >= 2.0.0 according to your hardware (cuda, mps, cpu).

MRAnnotator is developed on nnU-Net V2(version>=2.3.1) and follow the installation instruction from https://github.com/MIC-DKFZ/nnUNet/tree/master.
```
pip install nnunetv2
```
or
```
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
pip install -e .
```
