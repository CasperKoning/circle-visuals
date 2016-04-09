### What is this?

This is a python script for combining two images together into one where we treat one general image as
a background, and the other image is layered over the other, but only if it is contained within some circles.
See the `Examples` section below for a more visual example.

### Dependencies

Tested with both python2 and python3.

Requires Pillow. `pip install Pillow` should work. If not, see [here](https://pillow.readthedocs.org/en/3.0.0/installation.html#linux-installation) for details.

There is also a requirements file which pretty much does the same via `pip install -r requirements.txt`.

### Usage

From the command line:
```
python3 circles_images.py %PathToGeneralImage% %PathToImageInCircles% [options]
```

### Parameters

Parameter 	 | Flag | Description
-------------|------|------------
Inner radius | `-r1`| The radius of the inner circle. Default value is 0.
Outer radius | `-r2`| The radius of the outer circle. Default value is 0.
Output file  | `-o`	| Path of output file. Randomly generates a file name by default.

### Examples

`python3 circles_images.py examples/mountain.jpg examples/nebula.jpg -r1 600 -r2 900 -o examples/combined.jpg`

![output](/examples/combined.jpg)

### Known issues and todo's

- We use quite a low level approach of merging the images by analyzing the pixels of images.
There are probably more high level ways to do this using Pillow.
- Images are required to have the same size. This should not be the case.
- We want to use more images.
- We want to use more circles.
- We want to do this for video as well.