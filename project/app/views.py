from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response

class ReactView(APIView):
    def get(self, request):
        output=[
            {"age":output.age,
            "hypertension":output.hypertension,
            "heart_disease":output.heart_disease,
            "ever_married":output.ever_married,
            "avg_glucose_level":output.avg_glucose_level,
            "bmi":output.bmi}
            for output in React.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer=ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
