# MRAnnotator: Multi-Anatomy and Many-Sequence MRI Segmentation of 44 Structures
MRAnnotator is a tool for segmenting 44 anatomical structures in MR images across various sequences, with publicly available weights and a fully-annotated multi-anatomy evaluation dataset for MRI segmentation benchmarking. 

Details about this tool and dataset can be found in our paper, available on [*Radiology Advances*](https://academic.oup.com/radadv/advance-article/doi/10.1093/radadv/umae035/7926889).

The structure segmentation classes for MRAnnotator are shown below:

<img src=resources/label_figure.png alt="Example segmentations illustrating all structure classes" style="width:65%;"/>

# Installation
The model weights of MRAnnotator can be downloaded here: [https://drive.google.com/file/d/1bqBmvq84ImOZMDtsXWIyMSvE0m-gDzBL/view?usp=drive_link](https://drive.google.com/file/d/15gQuvmaDlbs7HlGpISWNqnnWYGp9-Xc4/view?usp=sharing). 
**The use of MRAnnotator is under CC-BY-NC (non-commercial) license.**

The fully-annotated evaluation test dataset is available by request here: [RadImageNet](https://www.radimagenet.com/).

Package dependencies:
* Python >= 3.9
* [Pytorch](http://pytorch.org/) >= 2.0.0 according to your hardware (cuda, mps, cpu)
* nnU-Net V2 (see below)

MRAnnotator was developed on nnU-Net V2 (version>=2.3.1); follow the installation instructions from https://github.com/MIC-DKFZ/nnUNet/tree/master:
```
pip install nnunetv2
```
or
```
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
pip install -e .
```
# Usage
To prepare your data for segmentation, input image data (NIfTI format) should be placed in **LAS** orientation, to enable MRANnotator to determine the laterality of the image volume. The **confirm_LAS.py** script will check the orientation of the nifti volume, and conduct RAS-LAS transformation if needed. After confirming the image data in the correct orientation, datasets are stored in the `nnUNet_raw` folder like this:

    Dataset001_Abdomen/
    ├── dataset.json
    ├── imagesTs
    └── labelsTs # if have ground truth testing labels

For the setup of MRAnnotator, please follow the same instruction as the nnU-Net

 how to setup location for model weights and datasets

MRAnnotator contains model weights specifically for Abdomen (Dataset001), Shoulder/Knee (Dataset002), Pelvis/Prostate (Dataset003), and Spine (Dataset004) anatomic regions. 
```
###segmentation of 8 abdomen organs
CUDA_VISIBLE_DEVICES=0 nnUNetv2_predict -i image_path  -o  prediction_path  -d 001 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring

###segmentation of 10 shoulder/knee structures
CUDA_VISIBLE_DEVICES=0 nnUNetv2_predict -i image_path  -o  prediction_path  -d 002 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring

###segmentation of 4 pelvis/prostate structures
CUDA_VISIBLE_DEVICES=0 nnUNetv2_predict -i image_path  -o  prediction_path  -d 003 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring

###segmentation of 22 shoulder/knee structures
CUDA_VISIBLE_DEVICES=0 nnUNetv2_predict -i image_path  -o  prediction_path  -d 004 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring
```
# Training MRI dataset details
The details of collected MRI data used to train the model weights are described in the following table:

|Anatomic study protocol|Anatomical structures|Sequences/Techniques|
|:-----|:-----|:-----|
|Abdomen (axial) | spleen, kidney_right, kidney_left, gallbladder, liver, aorta, inferior vena cava, pancreas  | T1GRE, In/out of phase, T2, T2 FS, post-contrast, Dixon, LAVA |
|Pelvis (coronal) | upper_femora, pelvis, sacrum | T1, T2, T2 FS, STIR, PD |
|Prostate (axial) | prostate | T1, T2 | 
|Shoulder (coronal) | humerus_right, clavicle_right, scapula_right, humerus_left, clavicle_left, scapula_left | PD, PD FS, T2, T2 FS | 
|Knee (sagittal) | femur, patella, fibula, tibia | PD, PD FS, T2, T2 FS | 
|Cervical spine (sagittal) | Vertebrae C3-C7  | T1, T1 FLAIR, T1 FS, T2, T2 FS, STIR | 
|Thoracic spine (sagittal) | Vertebrae T1-T12  | T1, T1 FLAIR, T2, T2 FS, STIR | 
|Lumbar spine (sagittal) | Vertebrae L1-L5  | T1, T1 FLAIR, T1 FS, T2, T2 FS, STIR | 
|Total | 44 structures | 11 | 

# Segmentation details
Structure classes within each anatomic region are assigned as follows:

|Index of Task001 Abdomen|Class name|
|:-----|:-----|
|1 | spleen |
|2 | kidney_right |
|3 | kidney_left |
|4 | gallbladder |
|5 | liver |
|6 | aorta |
|7 | inferior vena cava |
|8 | pancreas | 

|Index of Task002 ShoulderKnee|Class name|
|:-----|:-----|
|1 | femur |
|2 | patella |
|3 | fibula |
|4 | tibia |
|5 | humerus_right |
|6 | clavicle_right |
|7 | scapula_right |
|8 | humerus_left |
|9 | clavicle_left |
|10 | scapula_left |

|Index of Task003 PelvisProstate|Class name|
|:-----|:-----|
|1 | upper_femora |
|2 | pelvis |
|3 | sacrum |
|4 | prostate |

|Index of Task004 Spine|Class name|
|:-----|:-----|
|1 | Vertebrae C3 |
|2 | Vertebrae C4 |
|3 | Vertebrae C5 |
|4 | Vertebrae C6 |
|5 | Vertebrae C7 |
|6 | Vertebrae T1 |
|7 | Vertebrae T2 |
|8 | Vertebrae T3 |
|9 | Vertebrae T4 |
|10 | Vertebrae T5 |
|11 | Vertebrae T6 |
|12 | Vertebrae T7 |
|13 | Vertebrae T8 |
|14 | Vertebrae T9 |
|15 | Vertebrae T10 |
|16 | Vertebrae T11 |
|17 | Vertebrae T12 |
|18 | Vertebrae L1 |
|19 | Vertebrae L2 |
|20 | Vertebrae L3 |
|21 | Vertebrae L4 |
|22 | Vertebrae L5 |


# Citation
Please cite the following paper if using MRAnnotator model weights or the benchmark houldout test dataset:
```
@article{10.1093/radadv/umae035,
    author = {Zhou, Alexander and Liu, Zelong and Tieu, Andrew and Patel, Nikhil and Sun, Sean and Yang, Anthony and Choi, Peter and Lee, Hao-Chih and Tordjman, Mickael and Deyer, Louisa and Mei, Yunhao and Fauveau, Valentin and Soultanidis, George and Taouli, Bachir and Huang, Mingqian and Doshi, Amish and Fayad, Zahi A and Deyer, Timothy and Mei, Xueyan},
    title = {MRAnnotator: Multi-Anatomy and Many-Sequence MRI Segmentation of Forty-four Structures},
    journal = {Radiology Advances},
    pages = {umae035},
    year = {2024},
    month = {12},
    issn = {2976-9337},
    doi = {10.1093/radadv/umae035},
    url = {https://doi.org/10.1093/radadv/umae035},
    eprint = {https://academic.oup.com/radadv/advance-article-pdf/doi/10.1093/radadv/umae035/61218148/umae035.pdf},
}
```

# Acknowledgement
Please also cite [nnUNet](https://github.com/MIC-DKFZ/nnUNet), as MRAnnotator was developed using its framework. MRAnnotator is inspired by [TotalSegmentator](https://github.com/wasserth/TotalSegmentator/tree/master?tab=readme-ov-file) and [MRSegmentator](https://github.com/hhaentze/MRSegmentator).
