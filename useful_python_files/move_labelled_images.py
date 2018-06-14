from os import listdir
from os.path import isfile, join
onlyfiles = [f[:-4]+'.png' for f in listdir('/Users/i351707/Desktop/images/xml_label2') if isfile(join('/Users/i351707/Desktop/images/xml_label2', f))]

from shutil import copyfile
for i in onlyfiles:
    copyfile('/Users/i351707/Desktop/images/'+i,'/Users/i351707/Desktop/images/images_for_training2/'+i)