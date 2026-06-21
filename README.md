# 📐 Graph Calculator - Algebraisk Kalkylator

A comprehensive 3D vector and plane calculator with graphical visualization capabilities. This Python application allows you to perform various vector operations and visualize them in 3D space using Matplotlib.

## 📋 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Menu Options](#-menu-options)
- [Input Format](#-input-format)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### Vector Operations
- **Vector Input**: Enter 3D vectors (x, y, z) with support for fractions
- **Vector Addition**: Calculate and visualize a + b
- **Vector Subtraction**: Calculate and visualize a - b
- **Scalar Multiplication**: Multiply vectors by a scalar value
- **Dot Product**: Calculate scalar product between two vectors
- **Cross Product**: Calculate vector product between two vectors

### Plane Operations
- **Plane Input**: Define planes using equation `a*x + b*y + c*z + d = 0`
- **Plane Visualization**: Display 3D plane with adjustable axes
- **Vector Projection**: Project vectors onto a plane with graphical representation

### Visualization Features
- 3D interactive plots using Matplotlib
- Color-coded vectors for easy identification
- Customizable save options (PNG, PDF, SVG formats)
- Automatic axis scaling based on vector magnitudes

## 🔧 Requirements

### System Requirements
- Python 3.6 or higher
- Operating System: Windows, macOS, or Linux

### Python Packages
| Package | Version | Purpose |
|---------|---------|---------|
| NumPy | ≥1.19.0 | Numerical computations |
| Matplotlib | ≥3.3.0 | 3D visualization |

## 📦 Installation

### Step 1: Install Python
Download and install Python from [python.org](https://python.org)
- **Windows**: Make sure to check "Add Python to PATH" during installation
- **macOS**: Python comes pre-installed, but you may need to install pip
- **Linux**: Use your package manager (e.g., `sudo apt-get install python3 python3-pip`)

### Step 2: Install Required Packages
Open terminal/command prompt and run:

```bash
# Install required packages
pip install numpy matplotlib

# If you have multiple Python versions
python -m pip install numpy matplotlib

# For user installation (if you don't have admin rights)
pip install --user numpy matplotlib
