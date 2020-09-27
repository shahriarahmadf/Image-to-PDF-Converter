# Multiple Images to PDF Converter
# Developed by - Shahriar Ahmad Fahim
# E-mail: shahriarahmadf@gmail.com

import img2pdf

print('Note: The images you want to convert and the python converter should be in the same directory.')
n = int(input('What is the number of images you want to convert?\n '))
imglist = []
print('Note: Olease add .jpg or .png at the end e.g. "Photo.jpg"')
for i in range (0,n):
    x = input('Enter the image name in the directory: ')
    imglist.append(x)

PDFname= input('Note: Please add .pdf at the end of the name please e.g. myImageInpdf.pdf.\nEnter the PDF Name you want: ')

outputFile = open(PDFname,"wb")

outputFile.write(img2pdf.convert(imglist))
outputFile.close()


print('Your work is done. Please check.')