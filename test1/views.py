from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from test1.models import Fund
from test1.serializers import UpdateFundSerializer


class IndexView(APIView):
    def get(self, request):
        return JsonResponse("Hello World", safe=False, status=status.HTTP_200_OK)


class UpdateFundView(APIView):
    def put(self, request, fund_id):
        fund = get_object_or_404(Fund, id=fund_id)

        serializer = UpdateFundSerializer(fund, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
