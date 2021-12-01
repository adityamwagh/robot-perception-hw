# HW files for Robot Perception - FALL 2021 @ NYU

This repository contains my homework files for Robot Perception - FALL 2021 course taught by Prof. Chen Feng at NYU.

### Create a conda environment and install all the dependencies.

Genral conda environment
```
conda create -n hw --file requirements.txt -c open3d-admin -c conda-forge python=3.7 --yes
```

Pytorch specific conda environment
```
conda create -n pytorch --yes
```

### Install OpenGL

Debian family of  distributions.
```
sudo apt-get update && sudo apt-get install libgl1
```
Fedora family of distributions.
```
sudo dnf install libglvnd-glx
```

### Activate the conda environment
```
conda activate hw
```

### Install pyAprilTag
```
pip install https://github.com/ai4ce/pyAprilTag/releases/download/0.0.6/pyAprilTag-0.0.6-cp37-cp37m-linux_x86_64.whl
```