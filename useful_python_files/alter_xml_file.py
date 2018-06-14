from PIL import Image
from os import listdir
from os.path import isfile, join
from xml.dom import minidom
import xml.etree.ElementTree as ET

# tree = ET.parse('/Users/i351707/Desktop/images/labels_from_labelImg/1013.xml')
# root = tree.getroot()

# xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
# # import re
# # re.sub('<annotation>','<width>'+str(3)+'</width>',xmlstr, flags=re.DOTALL)

# firstDelPos=xmlstr.find("<width>") 
# secondDelPos=xmlstr.find("</width>")
# xmlstring = xmlstr.replace(xmlstr[firstDelPos+1:secondDelPos], 'width>'+str(3)) 

# tree = ET.ElementTree(ET.fromstring(xmlstring))

# tree.write('/Users/i351707/Desktop/myxml.xml')



onlyfiles = [f[:-4] for f in listdir('/Users/i351707/Desktop/images/xml_label2') if isfile(join('/Users/i351707/Desktop/images/xml_label2', f))]

for file in onlyfiles:
    image = Image.open('/Users/i351707/Desktop/images/'+file+'.png')
    height=image.size[1];width=image.size[0]
    
    tree = ET.parse('/Users/i351707/Desktop/images/xml_label2/'+file+'.xml')
    root = tree.getroot()

    xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')

    firstDelPos=xmlstr.find("<width>") 
    secondDelPos=xmlstr.find("</width>")
    xmlstr = xmlstr.replace(xmlstr[firstDelPos+1:secondDelPos], 'width>'+str(width))

    firstDelPos=xmlstr.find("<height>") 
    secondDelPos=xmlstr.find("</height>")
    xmlstring = xmlstr.replace(xmlstr[firstDelPos+1:secondDelPos], 'height>'+str(height))     

    tree = ET.ElementTree(ET.fromstring(xmlstring))

    tree.write('/Users/i351707/Desktop/images/changed_xmls/'+file+'.xml')