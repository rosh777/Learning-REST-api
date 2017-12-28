
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

#Lists all stocks or create a new one
#stocks/
class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serialzers = StockSerializer(stocks, many=True)
        return Response(serialzers.data)

    def post(self):
        pass
