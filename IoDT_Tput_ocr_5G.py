# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:48:08 2017

@author: egancen
"""


from PIL import Image, ImageGrab
from pylab import *
import numpy  as np
import time
np.set_printoptions(threshold=np.inf)  
import glob
from trainSet_tput_demo import tran_dict


from PIL import Image, ImageGrab
from pylab import *
import numpy as np
import time
import pytesseract

import requests
import json
import time
from random import randint

def ocr_single_img_tess(full_img, pos_dict):
    final_result_list = []
    for kpi_key, value in pos_dict.items():
        full_img = full_img
        data_img = full_img.crop(value)
        code = pytesseract.image_to_string(data_img)
        return code

    
def ocr():
    for p in glob.glob("./full_img/*"):
        full_img = Image.open(p)
        tput5G = ocr_single_img_tess(full_img, {"tput_pos":[145,254,250,300]})  #5G speed
        print tput5G
        return tput5G
        

            
def main():
    time.sleep(5)
    url = "http://127.0.0.1:8002/scheduler/"
    while True:
        try:
            tput5G=ocr()
            requests.post(url, data = json.dumps({'cmd':"dltput5G", "data":{"dltput5G":tput5G}}, ensure_ascii=False))
        except:
            pass
        
#        full_img.save("%s.png" % str(time.time()))
#        time.sleep(1)    



if __name__ == "__main__":
#    pro_db()
    main()
#    ocr()
    

