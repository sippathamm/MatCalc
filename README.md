# MatCalc &ndash; A simple matrix transformation library

## Overview

This Python library offers functions to perform transformations, 
including rotations and translations.

## Getting Started

To use this library, simply clone this repository to your local machine:

```bash
git clone https://github.com/sippathamm/MatCalc.git
```

Move `MatCalc.py` to your working directory. Then, you can import the library into your Python projects:

```python
from MatCalc import *
```

## Usage

Here's how you can utilize the library in your Python projects:

```python
# Generate a 3D rotation matrix
rotation_3d_matrix = x_rotation_3d(angle=30)

# Generate a 4d rotation matrix
rotation_4d_matrix = z_rotation_4d(angle=90)

# Generate a 4D translation matrix
translation_4d_matrix = translation_4d(x=4.0, y=2.0, z=0)
```

## Available Functions

### 3D transformation matrix

- `x_rotation_3d(angle: float)`: Generate a 3D rotation matrix around the x-axis.
- `y_rotation_3d(angle: float)`: Generate a 3D rotation matrix around the y-axis.
- `z_rotation_3d(angle: float)`: Generate a 3D rotation matrix around the z-axis.
- `rotation_3d(yaw: float, pitch: float, roll: float)`: Generate a combined 3D rotation matrix using yaw, pitch, and roll angles.
- `axis_angle_3d(axis: list, angle: float)`: Generate a 3D rotation matrix based on the axis-angle representation.

### 4D transformation matrix

- `x_rotation_4d(angle: float)`: Generate a 4D rotation matrix around the x-axis.
- `y_rotation_4d(angle: float)`: Generate a 4D rotation matrix around the y-axis.
- `z_rotation_4d(angle: float)`: Generate a 4D rotation matrix around the z-axis.
- `rotation_4d(yaw: float, pitch: float, roll: float)`: Generate a combined 4D rotation matrix using yaw, pitch, and roll angles.
- `axis_angle_4d(axis: list, angle: float)`: Generate a 4D rotation matrix based on the axis-angle representation.
- `translation_4d(x: float, y: float, z: float)`: Generate a 4D translation matrix.

## Dependency

- `python==3.11.7`
- `numpy==1.26.4`

## Author

This repository is maintained by Sippawit Thammawiset. You can contact the author at sippawit.t@kkumail.com
