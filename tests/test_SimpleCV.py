#!/usr/bin/env python
#
# Testing indexer with the Image.getNumpy result of SimpleCV framework.
#

from SimpleCV import Image

from NdArrayIndexer import NdArrayIndexer

print '========================================================================'
print 'RGB Image'
print '========================================================================'

print

print 'Converting RGB image to ndarray'

img = Image("img/rgb2x3.png")

rgb_img = img.getNumpy()

print

print 'Original ndarray after conversion from RGB image:'
print rgb_img

print

print 'rgb_img is array([[[r1, g1, b1], [rn, gn, bn]], [...]])'
print 'Where r is Red, g is Green and b is Blue dimensions by pixel.'
print 'The axe 0 is the coordinate y and the axe 1 is the coordinate x.'
print 'Now we are going to get the coordinates per pixel.'

print

indexer = NdArrayIndexer(rgb_img)
indexer.run()
img_with_coords = indexer.get()

print 'img_with_coords has now the (y, x) coordinates into the highest axe:'
print 'array([[[y1, x1, r1, g1, b1], [yn, xn, rn, gn, bn]], [...]])'

print

print 'Indexed RGB dimensions image:'
print img_with_coords

print

print '========================================================================'
print 'HSV Image'
print '========================================================================'

print

print 'Converting HSV image to ndarray'

img = Image("img/hsv2x3.png")
hsv = img.toHSV()

hsv_img = img.getNumpy()

print

print 'Original ndarray after conversion from HSV image:'
print hsv_img

print

print 'hsv_img is array([[[h1, s1, v1], [hn, sn, vn]], [...]])'
print 'Where r is Red, g is Green and b is Blue dimensions by pixel.'
print 'The axe 0 is the coordinate y and the axe 1 is the coordinate x.'
print 'Now we are going to get the coordinates per pixel.'

print

indexer = NdArrayIndexer(hsv_img)
indexer.run()
img_with_coords = indexer.get()

print 'img_with_coords has now the (y, x) coordinates into the highest axe:'
print 'array([[[y1, x1, h1, s1, v1], [yn, xn, hn, sn, vn]], [...]])'

print

print 'Indexed RGB dimensions image:'
print img_with_coords

print
print '------------------------------------------------------------------------'
