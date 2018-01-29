# Automatic Gifs with Deep Learning

[![header](https://github.com/burningion/automatic-gifs/raw/master/images/animate.gif)](https://www.makeartwithpython.com/blog/automatic-gifs-with-deep-learning/)

Automatic Gifs in Python with Mask R-CNN

This accompanies a [blog post](https://www.makeartwithpython.com/blog/automatic-gifs-with-deep-learning/), explaining how to use [Mask R-CNN](https://github.com/matterport/Mask_RCNN) for creating animated gifs automatically.

## How to Use 

First, download and install Mask R-CNN. Then you can create image sequences, and run `gif_extract.py` to extract out the objects you want from your video.

With those extracted images, you can then directly use them as input in Pygame sketches like this:

```bash
$ python3 sketch-environment.py pastedGif
```

This loads the Pygame sketch environment I wrote, which then loads the pastedGif.py file, calling `setup`, followed by `draw`. 

Look at the code, this should hopefully make sense.

If you call the Pygame sketch environment with `-r 600`, it will record out an image sequence to save as a video later.

## Making Gifs Directly

If you plan on making gifs, you'll want to run `python3 create-gif.py`. This will loop over all your input images, and rescale them to fit the same, empty size.

You can then run the following to generate an animated gif:

```bash
$ convert -dispose Background *.png outty.gif
```

Good luck!

![me](https://github.com/burningion/automatic-gifs/raw/master/images/automatic.gif)
