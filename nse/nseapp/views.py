import nsepy
from django.contrib import messages
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from nsepy.history import get_price_list
from nsetools import Nse
nse=Nse()
import json
from datetime import date
import datetime
# Create your views here.
def home(request):
    return render(request,'home.html')
def bhavcopy(request):
        try:
            price = get_price_list(dt=datetime.datetime.today() - datetime.timedelta(days=1))
            pd.options.display.max_rows = 9999
            pd.options.display.max_columns = 14
            df = pd.DataFrame(price)
            json_records = df.reset_index().to_json(orient='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'bhavcopy.html', context)
        except:
            messages.warning(request, 'Please Check Your Internet connections..')
            return render(request,'bhavcopy.html')
def gainloose(request):
    try:
        tg=nse.get_top_gainers()
        tl=nse.get_top_losers()
        dg = pd.DataFrame(tg)
        dl = pd.DataFrame(tl)
        json_records_gain = dg.reset_index().to_json(orient='records')
        json_records_lose = dl.reset_index().to_json(orient='records')
        datagain = []
        datalose = []
        datagain = json.loads(json_records_gain)
        datalose = json.loads(json_records_lose)
        context = {
            'dg':datagain,
            'dl':datalose
        }
        return render(request, 'topgainlose.html',context)
    except:
        messages.warning(request, 'Please Check Your Internet connections..')
        return render(request, 'topgainlose.html')
def fpidata(request):
    if request.method=="POST":
        itext=request.POST.get('op')
        url = 'https://www.fpi.nsdl.co.in/web/StaticReports/Fortnightly_Sector_wise_FII_Investment_Data/FIIInvestSector_{}.html'.format(itext)
        return render(request,'fpidata.html',{'url':url})
    else:
        return render(request,'fpidata.html')
