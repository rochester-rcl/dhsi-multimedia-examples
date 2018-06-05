## ImageMagick Example Commands

#### 1. Converting Files
Basic conversion
```
convert /path/to/image.jpg /path/to/image.png
```
Setting the quality
```
convert /path/to/image.jpg -quality 75 /path/to/image.png
```

#### 2. Image Manipulation

Rotating images (rotates 90deg clockwise)
```
convert /path/to/image.jpg -rotate 90 /path/to/image.png
```

Resizing  / scaling images (resizes to 50% of original size)
```
convert /path/to/image.jpg -resize 50 /path/to/image.png
```

Cropping images (crops 100px x 100px square from top left corner)
```
convert /path/to/image.jpg -crop 100x100+0+0 /path/to/image.png
```

#### 3. Image Filtering

Denoise an image (with an aggression level of 5)
```
convert /path/to/image.jpg -noise 5 /path/to/image.png
```

Sharpen an image (with an aggression level of 5)
```
convert /path/to/image.jpg -sharpen 5 /path/to/image.png
```

Add contrast to an image
```
convert /path/to/image.jpg -contrast /path/to/image.png
```

#### 4. Image Analysis
Display technical metadata
```
identify /path/to/image.jpg
```
Produce a histogram
```
convert /path/to/image.jpg histogram:/path/to/image.png
```
