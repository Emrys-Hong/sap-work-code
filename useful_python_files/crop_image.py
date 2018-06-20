import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
import cv2




onlyfiles = [f[:-4] for f in listdir('/Users/i351707/Desktop/images/xml_label1') if isfile(join('/Users/i351707/Desktop/images/xml_label1', f))]


for number in onlyfiles:
    img = cv2.imread("/Users/i351707/Desktop/images/"+number+".png")
    tree = ET.parse('/Users/i351707/Desktop/images/xml_label1/'+number+'.xml')
    root = tree.getroot()

    for i in root.findall('./object'):
        if i[0].text == 'ad':
            xmin = int(i[4][0].text)
            ymin = int(i[4][1].text)
            xmax = int(i[4][2].text)
            ymax = int(i[4][3].text)
            crop_img = img[ymin:ymax, xmin:xmax]
            cv2.imwrite('/Users/i351707/Desktop/cropped_images/'+number+'.png', crop_img)