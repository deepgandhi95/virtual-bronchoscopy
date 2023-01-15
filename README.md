# virtual-bronchoscopy

Description: 
This repository contains a python script using ParaView to create images for virtual bronchoscopy video from neonatal MR UTE images

The python script 'VB_dynamic_OSA_Videotest_2_FPS_VL.py' takes stl surfaces obtained from segmentation of trachea at different points along the respiratory cycle along with the centerline co-ordinates to output virtual bronchoscopy images that can be used to generate a virtual bronchoscopy video

Requirements:
1. python 3.6 or later
2. Paraview 5.10 or later

Usage:
python VB_dynamic_OSA_Videotest_2_FPS_VL.py -stl -ctl

Inputs:
Surface .stl files
Centerline co-ordinates .txt file

Outputs:
.png images 

Author:
Deep B. Gandhi
