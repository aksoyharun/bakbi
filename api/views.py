from rest_framework.views import Response
from rest_framework.decorators import api_view
from .models import Trade
from django.db.models import Min
from .serializers import *
import datetime
import json
import requests 
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings

# Create your views here.
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@api_view(['POST'])
def get_currency(request):
    
    currency=request.data['currency']
   
    
    if  currency in cache:
        print('cache deeeee ',currency)
        
        data=cache.get(currency)
        print(data,123123)
        return Response(data=data,status=200)
    else:
        print(currency,1)
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)

        
        data = Trade.objects.values('currency').filter(currency=currency,cdate__gte=date_from).annotate(value=Min('value'))[0]
        
        #data =Trade.objects.values('currency', 'value', 'cdate').filter(currency=currency)[:1]
        print(data)
        serialized_data=TopTradeSerializer(data,many=False)
        cache.set(currency,serialized_data.data,timeout=CACHE_TTL)

        print(data,222222)
        return Response(data=serialized_data.data,status=200)


@api_view(['GET','POST'])
def provider_view(request):
    if  request.method == 'GET':
        url_list = ['http://www.mocky.io/v2/5d19ec932f00004e00fd7326',
                    'http://www.mocky.io/v2/5d19ec692f00002c00fd7324']
        for i in url_list:
            r = requests.get(i, data=request.GET)
            data = r.json()
            print(data)
            for d in data:
                trade = Trade()

                print(d)
                trade.currency = d["code"]
                trade.value = float(d["rate"])
                trade.save()
                # r.text, r.content, r.url, r.json
        return Response(r.text)

    return Response('Could not save data')