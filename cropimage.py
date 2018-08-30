from PIL import Image, ImageFilter
import os
import glob

def resize(img_path, max_px_size, output_folder):
  images= glob.glob(img_path)
  for image in images:
      with Image.open(image) as img:
          width_0, height_0 = img.size
          out_f_name = os.path.split(image)[-1]
          out_f_path = os.path.join(output_folder, out_f_name)

          if max((width_0, height_0)) == max_px_size:
              print('writing {} to disk (no change from original)'.format(out_f_path))
              img.save(out_f_path)
          else:
              img = img.resize((28, 28), Image.ANTIALIAS)
              print('writing {} to disk'.format(out_f_path))
              img.save(out_f_path)

resize("uploads/*",28,"output")



# size_300 = (300, 300)
# size_700 = (700, 700)
# for f in os.listdir('.'):
#     if f.endswith('.png'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)

#         i.thumbnail(size_700)
#         i.save('700/{}_700.png'.format(fn, fext))

#         i.thumbnail(size_300)
#         i.save('300/{}_300.png'.format(fn, fext))


# image1 = Image.open("start.png")
# image1.convert(mode='L').save("start.png")

# def imageprepare(argv):
#     """
#     This function returns the pixel values.
#     The imput is a png file location.
#     """
#     size_28 = (28, 28)
#     im = Image.open(argv).convert('L')
#     width = float(im.size[0])
#     height = float(im.size[1])
#     newImage = Image.new('L', size_28, (255))  # creates white canvas of 28x28 pixels

#     if width > height:  # check which dimension is bigger
#         # Width is bigger. Width becomes 20 pixels.
#         nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
#         if (nheight == 0):  # rare case but minimum is 1 pixel
#             nheight = 1
#             # resize and sharpen
#         img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
#         wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
#         newImage.paste(img, (4, wtop))  # paste resized image on white canvas
#     else:
#         # Height is bigger. Heigth becomes 20 pixels.
#         nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
#         if (nwidth == 0):  # rare case but minimum is 1 pixel
#             nwidth = 1
#             # resize and sharpen
#         img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
#         wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
#         newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

#         # newImage.save("28/{}_28.png")

#     tv = list(newImage.getdata())  # get pixel values

#     # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
#     tva = [(255 - x) * 1.0 / 255.0 for x in tv]
#     print(tva)
#     return tva

# x=imageprepare('1256.png')#file path here
# print(len(x))# mnist IMAGES are 28x28=784 pixels
