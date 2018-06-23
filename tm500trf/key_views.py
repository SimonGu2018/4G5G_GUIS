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

#----------------------------------------------------------------
def configPage(request):
    return render(request, 'config.html')


@csrf_exempt
def sendCfgData(request):
    Testline.objects.all().delete()
    print "sendCfgData - key\n"	
	
    for i in range(1):
        Testline.objects.get_or_create(
            project = "5g"
            , dltput = "150"
            , rsrp = "-60,-61,-62,-63,-64,-65,-66,-67,-68,-69"
            , sinr = "1,2,3,4,5,6,7,8,9,10"
        )
    cfgdata = []
    testlines =  Testline.objects.all()
    print testlines	
    for idx,testline in enumerate(testlines):
        #dltput = testline.dltput
        timestamp = str(int(round(time.time()*1000)))
        dltput = str(randint(500,1500))
        rsrp = [timestamp+"_-"+str(randint(60,80)) for value in testline.rsrp.split(",")]
        sinr = [timestamp+"_"+str(randint(1,20)) for value in testline.sinr.split(",")]
        #sinr = testline.sinr.split(",")
        cfgdata.append({"dltput":dltput
                       , "rsrp":rsrp
                       , "sinr":sinr
                      })
    return JsonResponse(cfgdata, safe=False)

def scheduler(request):
    print "scheduler - key"
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        if "cmd" in data:
            cmd = data["cmd"]
            msg = data["data"]
            logging.info(dd_msg(CYAN.format("Get Msg : %s" % str(data))))
            del_supervisorlog()
            try:
                if cmd == "dl":
                    dltput = msg["dl"]
                    Testline.objects.filter(**{"project":"5g"}).update(**{"dltput":dltput})
                if cmd == "rsrp":
                    value = msg["rsrp"]
                    testlines =  Testline.objects.all()
                    for idx,testline in enumerate(testlines):
                        timestamp = str(int(round(time.time()*1000)))
                        rsrp = [value for value in testline.rsrp.split(",")]
                   
                    Testline.objects.filter(**{"project":"5g"}).update(**{"dltput":dltput})
     
            except Exception as e:
                logging.error(dd_msg(RED.format("scheduler error:%s" % str(e))))
    return HttpResponseRedirect('/')
