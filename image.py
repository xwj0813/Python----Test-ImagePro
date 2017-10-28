#利用PIL进行简单的图像处理

from PIL import Image

#读入图像
I=Image.open('20.jpg')
#显示图像
#I.show()
#保存图像
I.save('newimg.jpg')
#从图像截取一部分
box=(100,100,200,200)
rect=I.crop(box)
#rect.show()
rect.save('rect.jpg')
rect=rect.transpose(Image.ROTATE_90)
I.paste(rect,box)
#I.show()
#旋转图像

def rollImg(image,delta):
    xsize,ysize =image.size

    delta=delta % xsize
    if delta==0:
        return image
    part1=image.crop((0,0,delta,ysize))
    part2=image.crop((delta,0,xsize,ysize))
    image.paste(part2,(0,0,xsize-delta,ysize))
    image.paste(part1,(xsize-delta,0,xsize,ysize))
    return image

IMG=Image.open('newimg.jpg')
img=rollImg(IMG,200)
#img.show()
img.save('rool.jpg')
#几何旋转
out=IMG.rotate(45)#逆时针旋转45度
out.show()
out=IMG.transpose(Image.ROTATE_270)#旋转270度

##转为灰度图
gray=I.convert('L')
gray.save('gray.jpg')
