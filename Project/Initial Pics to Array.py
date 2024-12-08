import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('data_sum_of_all.jpeg')

image0 = Image.open('data0.jpeg')
image2 = Image.open('data2.jpeg')
image4 = Image.open('data4.jpeg')
image6 = Image.open('data6.jpeg')
image8 = Image.open('data8.jpeg')
image10 = Image.open('data10.jpeg')
image12 = Image.open('data12.jpeg')
image14 = Image.open('data14.jpeg')
image16 = Image.open('data16.jpeg')
image18 = Image.open('data18.jpeg')
image20 = Image.open('data20.jpeg')
image22 = Image.open('data22.jpeg')
image24 = Image.open('data24.jpeg')
image26 = Image.open('data26.jpeg')
image28 = Image.open('data28.jpeg')
image30 = Image.open('data30.jpeg')
image32 = Image.open('data32.jpeg')
image34 = Image.open('data34.jpeg')
image36 = Image.open('data36.jpeg')
image38 = Image.open('data38.jpeg')
image40 = Image.open('data40.jpeg')
image42 = Image.open('data42.jpeg')
image44 = Image.open('data44.jpeg')
image46 = Image.open('data46.jpeg')
image48 = Image.open('data48.jpeg')
image50 = Image.open('data50.jpeg')
image52 = Image.open('data52.jpeg')
image54 = Image.open('data54.jpeg')
image56 = Image.open('data56.jpeg')
image58 = Image.open('data58.jpeg')
image60 = Image.open('data60.jpeg')
image62 = Image.open('data62.jpeg')
image64 = Image.open('data64.jpeg')
image66 = Image.open('data66.jpeg')
image68 = Image.open('data68.jpeg')
image70 = Image.open('data70.jpeg')
image72 = Image.open('data72.jpeg')
image74 = Image.open('data74.jpeg')
image76 = Image.open('data76.jpeg')
image78 = Image.open('data78.jpeg')
image80 = Image.open('data80.jpeg')
image82 = Image.open('data82.jpeg')
image84 = Image.open('data84.jpeg')
image86 = Image.open('data86.jpeg')
image88 = Image.open('data88.jpeg')
image90 = Image.open('data90.jpeg')
image92 = Image.open('data92.jpeg')
image94 = Image.open('data94.jpeg')
image96 = Image.open('data96.jpeg')
image98 = Image.open('data98.jpeg')









width, height = image.size
pixels = image.load()


# width_new = 0.225 *width, 0.8* width
# height_new = 0.121 * height, 0.891*height

width0,height0 = image0.size 
width2,height2 = image2.size 
width4,height4 = image4.size 
width6,height6 = image6.size 
width8,height8 = image8.size 
width10,height10 = image10.size 
width12,height12 = image12.size 
width14,height14 = image14.size 
width16,height16 = image16.size 
width18,height18 = image18.size 
width20,height20 = image20.size 
width22,height22 = image22.size 
width24,height24 = image24.size 
width26,height26 = image26.size 
width28,height28 = image28.size 
width30,height30 = image30.size 
width32,height32 = image32.size 
width34,height34 = image34.size 
width36,height36 = image36.size 
width38,height38 = image38.size 
width40,height40 = image40.size 
width42,height42 = image42.size 
width44,height44 = image44.size 
width46,height46 = image46.size 
width48,height48 = image48.size 
width50,height50 = image50.size 
width52,height52 = image52.size 
width54,height54 = image54.size 
width56,height56 = image56.size 
width58,height58 = image58.size 
width60,height60 = image60.size 
width62,height62 = image62.size 
width64,height64 = image64.size 
width66,height66 = image66.size 
width68,height68 = image68.size 
width70,height70 = image70.size 
width72,height72 = image72.size 
width74,height74 = image74.size 
width76,height76 = image76.size 
width78,height78 = image78.size 
width80,height80 = image80.size 
width82,height82 = image82.size 
width84,height84 = image84.size 
width86,height86 = image86.size 
width88,height88 = image88.size 
width90,height90 = image90.size 
width92,height92 = image92.size 
width94,height94 = image94.size 
width96,height96 = image96.size 
width98,height98 = image98.size 

pixels0 = image0.load()
pixels2 = image2.load()
pixels4 = image4.load()
pixels6 = image6.load()
pixels8 = image8.load()
pixels10 = image10.load()
pixels12 = image12.load()
pixels14 = image14.load()
pixels16 = image16.load()
pixels18 = image18.load()
pixels20 = image20.load()
pixels22 = image22.load()
pixels24 = image24.load()
pixels26 = image26.load()
pixels28 = image28.load()
pixels30 = image30.load()
pixels32 = image32.load()
pixels34 = image34.load()
pixels36 = image36.load()
pixels38 = image38.load()
pixels40 = image40.load()
pixels42 = image42.load()
pixels44 = image44.load()
pixels46 = image46.load()
pixels48 = image48.load()
pixels50 = image50.load()
pixels52 = image52.load()
pixels54 = image54.load()
pixels56 = image56.load()
pixels58 = image58.load()
pixels60 = image60.load()
pixels62 = image62.load()
pixels64 = image64.load()
pixels66 = image66.load()
pixels68 = image68.load()
pixels70 = image70.load()
pixels72 = image72.load()
pixels74 = image74.load()
pixels76 = image76.load()
pixels78 = image78.load()
pixels80 = image80.load()
pixels82 = image82.load()
pixels84 = image84.load()
pixels86 = image86.load()
pixels88 = image88.load()
pixels90 = image90.load()
pixels92 = image92.load()
pixels94 = image94.load()
pixels96 = image96.load()
pixels98 = image98.load()






# Check if has alpha, to avoid "too many values to unpack" error
has_alpha = len(pixels[0,0]) == 4


has_alpha0 = len(pixels0[0,0]) == 4
has_alpha2 = len(pixels2[0,0]) == 4
has_alpha4 = len(pixels4[0,0]) == 4
has_alpha6 = len(pixels6[0,0]) == 4
has_alpha8 = len(pixels8[0,0]) == 4
has_alpha10 = len(pixels10[0,0]) == 4
has_alpha12 = len(pixels12[0,0]) == 4
has_alpha14 = len(pixels14[0,0]) == 4
has_alpha16 = len(pixels16[0,0]) == 4
has_alpha18 = len(pixels18[0,0]) == 4
has_alpha20 = len(pixels20[0,0]) == 4
has_alpha22 = len(pixels22[0,0]) == 4
has_alpha24 = len(pixels24[0,0]) == 4
has_alpha26 = len(pixels26[0,0]) == 4
has_alpha28 = len(pixels28[0,0]) == 4
has_alpha30 = len(pixels30[0,0]) == 4
has_alpha32 = len(pixels32[0,0]) == 4
has_alpha34 = len(pixels34[0,0]) == 4
has_alpha36 = len(pixels36[0,0]) == 4
has_alpha38 = len(pixels38[0,0]) == 4
has_alpha40 = len(pixels40[0,0]) == 4
has_alpha42 = len(pixels42[0,0]) == 4
has_alpha44 = len(pixels44[0,0]) == 4
has_alpha46 = len(pixels46[0,0]) == 4
has_alpha48 = len(pixels48[0,0]) == 4
has_alpha50 = len(pixels50[0,0]) == 4
has_alpha52 = len(pixels52[0,0]) == 4
has_alpha54 = len(pixels54[0,0]) == 4
has_alpha56 = len(pixels56[0,0]) == 4
has_alpha58 = len(pixels58[0,0]) == 4
has_alpha60 = len(pixels60[0,0]) == 4
has_alpha62 = len(pixels62[0,0]) == 4
has_alpha64 = len(pixels64[0,0]) == 4
has_alpha66 = len(pixels66[0,0]) == 4
has_alpha68 = len(pixels68[0,0]) == 4
has_alpha70 = len(pixels70[0,0]) == 4
has_alpha72 = len(pixels72[0,0]) == 4
has_alpha74 = len(pixels74[0,0]) == 4
has_alpha76 = len(pixels76[0,0]) == 4
has_alpha78 = len(pixels78[0,0]) == 4
has_alpha80 = len(pixels80[0,0]) == 4
has_alpha82 = len(pixels82[0,0]) == 4
has_alpha84 = len(pixels84[0,0]) == 4
has_alpha86 = len(pixels86[0,0]) == 4
has_alpha88 = len(pixels88[0,0]) == 4
has_alpha90 = len(pixels90[0,0]) == 4
has_alpha92 = len(pixels92[0,0]) == 4
has_alpha94 = len(pixels94[0,0]) == 4
has_alpha96 = len(pixels96[0,0]) == 4
has_alpha98 = len(pixels98[0,0]) == 4


# Create empty 2D list
fill = 1
array = [[fill for x in range(width)] for y in range(height)]

fill0 = 1
array0 = [[fill0 for x in range(width)] for y in range(height)]
fill2 = 1
array2 = [[fill2 for x in range(width)] for y in range(height)]
fill4 = 1
array4 = [[fill4 for x in range(width)] for y in range(height)]
fill6 = 1
array6 = [[fill6 for x in range(width)] for y in range(height)]
fill8 = 1
array8 = [[fill8 for x in range(width)] for y in range(height)]
fill10 = 1
array10 = [[fill10 for x in range(width)] for y in range(height)]
fill12 = 1
array12 = [[fill12 for x in range(width)] for y in range(height)]
fill14 = 1
array14 = [[fill14 for x in range(width)] for y in range(height)]
fill16 = 1
array16 = [[fill16 for x in range(width)] for y in range(height)]
fill18 = 1
array18 = [[fill18 for x in range(width)] for y in range(height)]
fill20 = 1
array20 = [[fill20 for x in range(width)] for y in range(height)]
fill22 = 1
array22 = [[fill22 for x in range(width)] for y in range(height)]
fill24 = 1
array24 = [[fill24 for x in range(width)] for y in range(height)]
fill26 = 1
array26 = [[fill26 for x in range(width)] for y in range(height)]
fill28 = 1
array28 = [[fill28 for x in range(width)] for y in range(height)]
fill30 = 1
array30 = [[fill30 for x in range(width)] for y in range(height)]
fill32 = 1
array32 = [[fill32 for x in range(width)] for y in range(height)]
fill34 = 1
array34 = [[fill34 for x in range(width)] for y in range(height)]
fill36 = 1
array36 = [[fill36 for x in range(width)] for y in range(height)]
fill38 = 1
array38 = [[fill38 for x in range(width)] for y in range(height)]
fill40 = 1
array40 = [[fill40 for x in range(width)] for y in range(height)]
fill42 = 1
array42 = [[fill42 for x in range(width)] for y in range(height)]
fill44 = 1
array44 = [[fill44 for x in range(width)] for y in range(height)]
fill46 = 1
array46 = [[fill46 for x in range(width)] for y in range(height)]
fill48 = 1
array48 = [[fill48 for x in range(width)] for y in range(height)]
fill50 = 1
array50 = [[fill50 for x in range(width)] for y in range(height)]
fill52 = 1
array52 = [[fill52 for x in range(width)] for y in range(height)]
fill54 = 1
array54 = [[fill54 for x in range(width)] for y in range(height)]
fill56 = 1
array56 = [[fill56 for x in range(width)] for y in range(height)]
fill58 = 1
array58 = [[fill58 for x in range(width)] for y in range(height)]
fill60 = 1
array60 = [[fill60 for x in range(width)] for y in range(height)]
fill62 = 1
array62 = [[fill62 for x in range(width)] for y in range(height)]
fill64 = 1
array64 = [[fill64 for x in range(width)] for y in range(height)]
fill66 = 1
array66 = [[fill66 for x in range(width)] for y in range(height)]
fill68 = 1
array68 = [[fill68 for x in range(width)] for y in range(height)]
fill70 = 1
array70 = [[fill70 for x in range(width)] for y in range(height)]
fill72 = 1
array72 = [[fill72 for x in range(width)] for y in range(height)]
fill74 = 1
array74 = [[fill74 for x in range(width)] for y in range(height)]
fill76 = 1
array76 = [[fill76 for x in range(width)] for y in range(height)]
fill78 = 1
array78 = [[fill78 for x in range(width)] for y in range(height)]
fill80 = 1
array80 = [[fill80 for x in range(width)] for y in range(height)]
fill82 = 1
array82 = [[fill82 for x in range(width)] for y in range(height)]
fill84 = 1
array84 = [[fill84 for x in range(width)] for y in range(height)]
fill86 = 1
array86 = [[fill86 for x in range(width)] for y in range(height)]
fill88 = 1
array88 = [[fill88 for x in range(width)] for y in range(height)]
fill90 = 1
array90 = [[fill90 for x in range(width)] for y in range(height)]
fill92 = 1
array92 = [[fill92 for x in range(width)] for y in range(height)]
fill94 = 1
array94 = [[fill94 for x in range(width)] for y in range(height)]
fill96 = 1
array96 = [[fill96 for x in range(width)] for y in range(height)]
fill98 = 1
array98 = [[fill98 for x in range(width)] for y in range(height)]





for y in range(int (0.141  * height), int (0.791 * height)):
    for x in range(int (0.225 * width), int (0.8 * width)):
        if has_alpha:
            r, g, b, a = pixels[x,y]
        else:
            r, g, b = pixels[x,y]
        lum = ((r+g+b)/3) 
        array[y][x] = lum/255 # Map values from range 0-255 to 0-1
        




        
print(image)
print(array)