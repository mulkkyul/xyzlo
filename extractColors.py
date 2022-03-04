import math
import PIL
import extcolors
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import gridspec
import pandas as pd

# https://kylermintah.medium.com/coding-a-color-palette-generator-in-python-inspired-by-procreate-5x-b10df37834ae

def study_image(image_index):
    image_path = './img/'+ image_index + '.png'
    color_path = './color/' + image_index + '.csv'
    img = PIL.Image.open(image_path)
    tolerance = 32
    limit = 10
    colors, _ = extcolors.extract_from_image(img, tolerance, limit)
    df = pd.DataFrame(columns=['color'])
    for i in range(len(colors)):
        row = ['#%02x%02x%02x' % (colors[i][0][0],colors[i][0][1],colors[i][0][2])]
        df.at[len(df)] = row
    df.to_csv(color_path, index=False)
    color_palette = render_color_platte(colors)
    overlay_palette(img, color_palette, image_index)

def render_color_platte(colors):
  size = 100
  columns = 5
  width = int(min(len(colors), columns) * size)
  height = int((math.floor(len(colors) / columns) + 1) * size)
  result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
  canvas = ImageDraw.Draw(result)
  for idx, color in enumerate(colors):
      x = int((idx % columns) * size)
      y = int(math.floor(idx / columns) * size)
      canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
  return result

def overlay_palette(img, color_palette, image_index):
  nrow = 2
  ncol = 1
  f = plt.figure(figsize=(20,20), facecolor='None', edgecolor='k', dpi=50, num=None)
  gs = gridspec.GridSpec(nrow, ncol, wspace=0.0, hspace=0.0)
  f.add_subplot(2, 1, 1)
  plt.imshow(img, interpolation='nearest')
  plt.axis('off')

  f.add_subplot(1, 2, 2)
  plt.imshow(color_palette, interpolation='nearest')
  plt.axis('off')
  plt.subplots_adjust(wspace=0, hspace=0, bottom=0)
  plt.savefig('./color_'+image_index+'.png', bbox_inches='tight')
  #plt.show(block=True)


for idx in range(11):
    image_url = "image%02d"%idx
    study_image(image_url)