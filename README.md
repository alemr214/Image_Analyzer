# Image Analyzer

An image analyzer on Python that allows loading an image, viewing its details, and applying basic operations such as extracting color channels, applying rotation, and shrinking it.

## Notebook

A Jupyter notebook explaining how the image methods work and viewing some examples with images saved in the images directory on this repository.

[![Abrir notebook](https://img.shields.io/badge/Abrir%20notebook-Notebook-blue)](notebooks/Image_Analyzer.ipynb)

## Description

This repository offers a graphic interface based on Tkinter for:

- Select an image file (`.png`, `.jpg`, `.jpeg`)
- Shows its weight, height, and number of color channels.
- Save every extracted channel image.
- Save a rotated image 90°.
- Save a shrunk version applying a `N` pixel value.

## Requirements

- Python 3.11 or greater.
- Terminal

Dependencies:

- Numpy
- Matplotlib
- Tkinter
- Pillow

To install, execute:

```bash
pip install -r requirements.txt
```

## Use

To run the application execute on console:

```bash
python src/main.py
```

Or make an executable:

```bash
pyinstaller --onefile --windowed --name ImageAnalyzer src/main.py
```

### Steps

1. Click on `Select image`.
2. Choose a valid file.
3. View the properties of the image (weight, height, color channels)
4. Use the buttons to:
   - Extract the color channels.
   - Rotate the image.
   - Shrink the image.
5. The new images will be saved in the same directory as `_red.png`, `_green.png`, `_blue.png`, `_rotated.png` and `_shrunk.png`.

## App structure

```text
src/
├─ model/
│  └─ image.py          # Image class with private properties and methods
├─ ui/
│  └─ window.py         # Graphic interface and interactive logic.
├─ utils/
│  └─ image_utils.py    # Functions to apply on images.
└─ main.py              # Main file to execute.
```
