from rest_framework.serializers import ModelSerializer
from .models import *


class TradeSerializer(ModelSerializer):

    class Meta:
        model=Trade
        fields='__all__'



class TopTradeSerializer(ModelSerializer):

    class Meta:
        model=Trade
        fields=('currency','value',)