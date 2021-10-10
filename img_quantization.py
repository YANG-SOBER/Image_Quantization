import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def img_quantization_2(img_single):
    for i in range(img_single.shape[0]):
        for j in range(img_single.shape[1]):
            if img_single[i, j] < 128:
                img_single[i, j] = 0
            else:
                img_single[i, j] = 1
    return img_single

def img_quantization_4(img_single):
    for i in range(img_single.shape[0]):
        for j in range(img_single.shape[1]):
            if img_single[i, j] < 64:
                img_single[i, j] = 0
            elif img_single[i, j] < 128:
                img_single[i, j] = 1
            elif img_single[i, j] < 192:
                img_single[i, j] = 2
            else:
                img_single[i, j] = 3
    return img_single

def img_quantization_8(img_single):
    for i in range(img_single.shape[0]):
        for j in range(img_single.shape[1]):
            if img_single[i, j] < 32:
                img_single[i, j] = 0
            elif img_single[i, j] < 64:
                img_single[i, j] = 1
            elif img_single[i, j] < 96:
                img_single[i, j] = 2
            elif img_single[i, j] < 128:
                img_single[i, j] = 3
            elif img_single[i, j] < 160:
                img_single[i, j] = 4
            elif img_single[i, j] < 192:
                img_single[i, j] = 5
            elif img_single[i, j] < 224:
                img_single[i, j] = 6
            else:
                img_single[i, j] = 7

    return img_single

def plot_img():
    img_path = 'milan.jpeg'
    fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(36, 8))
    title1 = ['Red', 'Green', 'Blue']
    title2 = ['2_Values_Quantization', '4_Values_Quantization', '8_Values_Quantization']

    for i in range(3):
        img = np.array(Image.open(img_path), dtype='uint8')
        for j in range(3):
            if i == 0:
                img_quantization_2(img[:, :, j])
            elif i == 1:
                img_quantization_4(img[:, :, j])
            elif i == 2:
                img_quantization_8(img[:, :, j])
            axs[i, j].imshow(img[:, :, j], vmin=img[:, :, j].min(), vmax=img[:, :, j].max(), cmap='gray')
            axs[i, j].set_title(title1[j] + ' Channel with ' + title2[i])
            axs[i, j].set_axis_off()
    plt.show()
    fig.savefig('img_quantization.jpg')

if __name__ =='__main__':
    plot_img()
