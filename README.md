# Introduction

Auto script for UMA

# Test Command

```
pip install .; python .\test_code\screen_shot.py
```

```
pip install .; python .\test_code\mouse_click.py
```

```
pip install .; python .\script\skip_on.py
```

# TODO:

- [x] Random Click
- [x] Slide

# Automation

## Screen Recognition

- state → which page

### main page

### main training page

- ~~skip on~~
- physical strength
    - progress
    - percentage
- train
    - calculation
- race
- skill
- item

### Increased abilities in sub training page

1. Get test data
2. Find best parameters for adaptiveThreshold
3. pytesseract.image_to_string

⇒ Use AI model

### Edge and area (find_contours.count_heads)

1. Convert image to greyscale: Convert the image from RGB format to greyscale for later processing.
2. Extract edges in the image using the Canny Edge Detection algorithm: Use the Canny Edge Detection algorithm to extract edges in the image to make it easier to find the avatar outline.
3. Remove noise from the drawing using morphological operations: Use morphological operations to remove noise from the drawing to improve the accuracy of the contour.
4. Use the findContours() function to find contours in a picture: Use the findContours() function to find contours in a picture and store the contours in the contours list.
5. Calculate the number of avatars in the picture: Iterate through the list of contours and calculate the area of each contour. If the area of a contour is greater than a certain value, it is determined to be an avatar and the number of avatars is increased by one.
6. Output the number of avatars in the picture: Output the number of avatars.

## Mouse Motion

- win32 for BlueStack

# Plan

- Change to Rust?
