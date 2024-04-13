#Image create

#((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)1/2    

import os, time
from PIL import Image
from colorama import *

init(autoreset=True)

colors1 = ['BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX', 'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX',
           'LIGHTRED_EX', 'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET', 'WHITE', 'YELLOW']

colors = {'BLACK':Fore.BLACK,
          'BLUE':Fore.BLUE,
          'CYAN':Fore.CYAN,
          'GREEN':Fore.GREEN,
          'LIGHTBLACK_EX':Fore.LIGHTBLACK_EX,
          'LIGHTBLUE_EX':Fore.LIGHTBLUE_EX,
          'LIGHTCYAN_EX':Fore.LIGHTCYAN_EX,
          'LIGHTGREEN_EX':Fore.LIGHTGREEN_EX,
          'LIGHTMAGENTA_EX':Fore.LIGHTMAGENTA_EX,
          'LIGHTRED_EX':Fore.LIGHTRED_EX,
          'LIGHTWHITE_EX':Fore.LIGHTWHITE_EX,
          'LIGHTYELLOW_EX':Fore.LIGHTYELLOW_EX,
          'MAGENTA':Fore.MAGENTA,
          'RED':Fore.RED,
          'RESET':Fore.RESET,
          'WHITE':Fore.WHITE,
          'YELLOW':Fore.YELLOW}

colorRgb = {'BLACK':[12, 12, 12],
            'BLUE':[8, 48, 218],
            'CYAN':[58, 150, 221],
            'GREEN':[19, 161, 14],
            'LIGHTBLACK_EX':[118, 118, 102],
            'LIGHTBLUE_EX':[59, 120, 220],
            'LIGHTCYAN_EX':[97, 214, 185],
            'LIGHTGREEN_EX':[21, 198, 13],
            'LIGHTMAGENTA_EX':[180, 0, 137],
            'LIGHTRED_EX':[231, 72, 75],
            'LIGHTWHITE_EX':[242, 242, 242],
            'LIGHTYELLOW_EX':[249, 241, 165],
            'MAGENTA':[136, 23, 152],
            'RED':[197, 12, 25],
            'RESET':[204, 204, 204],
            'WHITE':[204, 204, 204],
            'YELLOW':[193, 156, 0]}

def sa(nums):
    return sum(nums)/len(nums)
def getDist3D(color1, color2):
    x1, y1, z1 = color1
    x2 = color2[0]
    y2 = color2[1]
    z2 = color2[2]
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)*0.5 if x2 > x1 and y2 > y1 and z2 > z1 else ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)*0.5

def getColor(color):
    dist = []
    for clr in colors1:
        dist.append(getDist3D(colorRgb[clr], color))
    index = dist.index(min(dist))
    return colors[colors1[index]]

def convertImageRgb(path):

    txt = []
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    for x in range(0, im.height):
        str1 = ''
        for y in range(0, im.width):
            rgb = rgb_im.getpixel((y, x))
            sym = "#"
            str1 += getColor(rgb)+sym
        txt.append(str1)
    return txt
def convertImage(path):
    txt = []
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    grad = ' `.~i!g%#@'
    for x in range(0, im.height):
        str1 = ''
        for y in range(0, im.width):
            rgb = rgb_im.getpixel((y, x))
            sym = "#"
            rgb2 = [rgb[0], rgb[1], rgb[2]]
            if len(rgb) == 4 and rgb[3] <= 10:
                str1 += ' '
                continue
            str1 += grad[int((sa(rgb)-50)/25)]
        txt.append(str1)
    return txt
def convertImageWhite(path):
    txt = []
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    grad = '@#%g!~.` '
    for x in range(0, im.height):
        str1 = ''
        for y in range(0, im.width):
            rgb = rgb_im.getpixel((y, x))
            sym = "#"
            rgb2 = [rgb[0], rgb[1], rgb[2]]
            if len(rgb) == 4 and rgb[3] <= 10:
                str1 += ' '
                continue
            str1 += grad[int((sa(rgb)-50)/25)]
        txt.append(str1)
    return txt
def convertImageRgb2(im):
    txt = []
    rgb_im = im.convert('RGB')
    for x in range(0, im.height):
        str1 = ''
        for y in range(0, im.width):
            rgb = rgb_im.getpixel((y, x))
            sym = "#"
            str1 += getColor(rgb)+sym
        txt.append(str1)
    return txt
def convertImage2(im):
    txt = []
    rgb_im = im.convert('RGB')
    grad = ' `.~i!g%#@'
    for x in range(0, im.height):
        str1 = ''
        for y in range(0, im.width):
            rgb = rgb_im.getpixel((y, x))
            sym = "#"
            rgb2 = [rgb[0], rgb[1], rgb[2]]
            if len(rgb) == 4 and rgb[3] <= 10:
                str1 += ' '
                continue
            str1 += grad[int((sa(rgb)-50)/25)]
        txt.append(str1)
    return txt
def printArr2(arr1):
    for a in arr1:
        str1 = ''
        for b in a:
            str1 += b
        print(str1)
def animation(anim, fps):
    cash = []
    counter = 0
    x = False

    while 1:
        os.system('cls')
        if not x:
            img2 = convertImage(anim[counter])
            cash.append(img2)
            printArr2(img2)
        else:
            printArr2(cash[counter])
        counter += 1
        if counter > len(anim)-1:
            counter = 0
            x = True
        time.sleep(1/fps)

def animationRgb(anim, fps):
    cash = []
    counter = 0
    x = False

    while 1:
        os.system('cls')
        if not x:
            img2 = convertImageRgb(anim[counter])
            cash.append(img2)
            printArr2(img2)
        else:
            printArr2(cash[counter])
        counter += 1
        if counter > len(anim)-1:
            counter = 0
            x = True
        time.sleep(1/fps)
def animationGif(path, fps):
    cash = []
    counter = 0
    x = False
    im = Image.open(path)
    while 1:
        os.system('cls')
        if not x:
            im.seek(counter)
            img2 = convertImage2(im)
            cash.append(img2)
            printArr2(img2)
        else:
            printArr2(cash[counter])
        counter += 1
        if counter > im.n_frames-1:
            counter = 0
            x = True
        time.sleep(1/fps)
def animationRgbGif(path, fps):
    cash = []
    counter = 0
    x = False
    im = Image.open(path)
    anim = []
    while 1:
        os.system('cls')
        if not x:
            im.seek(counter)
            img2 = convertImageRgb2(im)
            cash.append(img2)
            printArr2(img2)
        else:
            printArr2(cash[counter])
        counter += 1
        if counter > im.n_frames-1:
            counter = 0
            x = True
        time.sleep(1/fps)
#for i in range(0, len(colors1)):
#    print(colors[colors1[i]] + colors1[i])
            
