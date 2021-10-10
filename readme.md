### What is image quantization?

Use Point Operator (pixel-by-pixel) to quantize the image.

Quantization means rounding the gray values to a set of discrete values.

Actually, binary image with two values is a special case of quantization.

For a optimal image encoding: use the quantization that minimize the rounding error given the image.

### example
<img src="https://github.com/YANG-SOBER/Image_Quantization/blob/main/milan.jpeg" width=50% height=50%>

<img src="https://github.com/YANG-SOBER/Image_Quantization/blob/main/img_hist.png" width=75% height=75%>

We can find that **with the increment of number of discrete values, the rounding error will get smaller**.
