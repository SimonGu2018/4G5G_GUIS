"""
Developer : andrew.x.chen@ericsson.com
Date      : May 2018
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from tm500trf.models import Testline
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

import json
import datetime
import logging
import glob
from random import randint
import time
import os
import random
localpath = os.getcwd()
logging.basicConfig(filename=localpath+"/weblog.log", level=logging.INFO)


#----------------------------------------------------------------
def configPage(request):
    return render(request, 'config.html')

def modePage(request):
    return render(request, 'mode.html')


tput4G = 0.1
tput5G = 0.1



@csrf_exempt
def sendInitCfg(request):
    testlines =  Testline.objects.all()
    for idx,testline in enumerate(testlines):
        mode = testline.mode
        tput_range = testline.tput_range

    cfgdata = {}
    try:
        cfgdata = {"mode":mode, "tput_range":tput_range}
    except:
        pass
    return JsonResponse(cfgdata, safe=False)


@csrf_exempt
def sendCfgData(request):
    #rsrp_ = ",".join([str(randint(60,80)) for value in range(10)])
    #sinr_ = ",".join([str(randint(1,20)) for value in range(10)])
    #dltput_ = str(1000)
    ##print rsrp_
    #
    #Testline.objects.all().delete()
    #for i in range(1):
    #    Testline.objects.get_or_create(
    #        project = "5g"
    #        , dltput = dltput_
    #        , rsrp = rsrp_
    #        , sinr = rsrp_
    #        , cell = "on"
    #        , mode = "2"
    #        , tput_range = "1399-1400"
    #    )

   # cfgdata = []
   # testlines =  Testline.objects.all()
   # for idx,testline in enumerate(testlines):
   #     #dltput = testline.dltput
   #     timestamp = str(int(round(time.time()*1000)))
   #     dltput = testline.dltput
   #     print 100*"+" + dltput

   #     #rsrp = testline.rsrp.split(",")
   #     #print 100*"+" + str(rsrp)
   #     #rsrp = [timestamp+"_-"+str(randint(60,80)) for value in testline.rsrp.split(",")]
   #     #sinr = testline.sinr.split(",")
   #     #print rsrp 
   #     #print dltput
   #     #print rsrp
   #     #print sinr
   #     cfgdata.append({"dltput":dltput
   #                    , "rsrp":[timestamp+"_-"+str(randint(60,80)) for value in testline.rsrp.split(",")]
   #                    , "sinr":[timestamp+"_"+str(randint(1,20)) for value in testline.sinr.split(",")]
   #                   })


    cfgdata = []
    testlines =  Testline.objects.all()
    for idx,testline in enumerate(testlines):
        timestamp = str(int(round(time.time()*1000)))
        mode = testline.mode
        cell = testline.cell
        tput_range = testline.tput_range
        min_tput = float(tput_range.split("-")[0])
        max_tput = float(tput_range.split("-")[-1])
		
        if mode == "1":
            dltput4G = tput4G
            dltput5G = tput5G
        elif mode == "2":
            if cell == "on":
                dltput4G = str(round(random.uniform(min_tput,max_tput),4))
                dltput5G = str(round(random.uniform(min_tput,max_tput),4)+1)				
            elif cell == "off":
                dltput = "0"
        elif mode == "3":
            dltput = str(round(random.uniform(min_tput,max_tput),4))

        cfgdata.append({"dltput4G":dltput4G})
        cfgdata.append({"dltput5G":dltput5G})
        print cfgdata		
    return JsonResponse(cfgdata, safe=False)

def dd_msg(msg):#string
     return "%s  %s" % (datetime.datetime.utcnow().strftime('%y-%m-%d-%H:%M:%S'), str(msg))

def changecell(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cell = data["data"]["cell"]
        Testline.objects.filter(**{"project":"5g"}).update(**{"cell":cell})
    return HttpResponseRedirect('/')
    


def scheduler(request):
    global tput4G, tput5G
    print "scheduler - non"
    if request.method == "POST":
        data = json.loads(request.body)
        if "cmd" in data:
            cmd = data["cmd"]
            msg = data["data"]
            logging.info(dd_msg("Get Msg : %s" % str(data)))
            try:
                if cmd == u"dltput4G":
                    tput4G =  msg["dltput4G"]
                    print tput4G;
                    #Testline.objects.filter(**{"project":"5g"}).update(**{"dltput":dltput})
                elif cmd == u"dltput5G":
                    tput5G =  msg["dltput5G"]
                    print tput5G;
                    #Testline.objects.filter(**{"project":"5g"}).update(**{"dltput":dltput})
					
                elif cmd == "updateCfg":
                    mode = msg["mode"]
                    tput_range = msg["tput_range"]
                    Testline.objects.filter(**{"project":"5g"}).update(**{"mode":mode})
                    Testline.objects.filter(**{"project":"5g"}).update(**{"tput_range":tput_range})
                elif cmd == "cell":
                    cell = data["data"]["cell"]
                    Testline.objects.filter(**{"project":"5g"}).update(**{"cell":cell})
            except Exception as e:
                print "ERROR occurs!"			
                logging.error(dd_msg("scheduler error:%s" % str(e)))
    return HttpResponseRedirect('/')
