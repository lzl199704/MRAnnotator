# MRAnnotator: Multi-Anatomy and Many-Sequence MRI Segmentation of Forty-four Structures
MRAnnotator is a tool for segmenting 44 anatomical structures in MR images across various sequences. A holdout independent test dataset can be downloaded here: . *Highlight the model weights and dataset are released to the public for evaluation.*

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
# Usage
To prepare the data for segmentation, the input image data (in nifti format) should be placed in LAS orientation. This setting could help MRANnotator determine the laterality of the image volume.  

MRAnnotator contains model weights specifically for Abdomen (Task_number:001), ShoulderKnee (Task_number:002), PelvisProstate (Task_number:003), and Spine (Task_number:004). 
```
###segmentation of 8 abdomen organs
CUDA_VISIBLE_DEVICES=0 nnUNetv2_predict -i image_path  -o  prediction_path  -d 001 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring
###segmentation of 10 shoulder/knee organs
CUDA_VISIBLE_DEVICES=0 nnUNetv2_predict -i image_path  -o  prediction_path  -d 002 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring
```
# MRI dataset details
The details of collected MRI data are described in the following table:

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

# Class details
Here you can find the classes of each Task:

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
```

# Acknowledgement
Please also cite [nnUNet](https://github.com/MIC-DKFZ/nnUNet) as MRAnnotator is developed using its framework. The MRAnnotator is inspired from [Totalsegmentator](https://github.com/wasserth/TotalSegmentator/tree/master?tab=readme-ov-file) and [MRSegmentator](https://github.com/hhaentze/MRSegmentator).
