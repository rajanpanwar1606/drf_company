from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import * 
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class CompanyView(APIView):
    def post(self, request, format=None):
        name = request.data.get("name")
        print("name : ", name)
        get_data = Company.objects.filter(name=name).exists()
        if get_data:
            return Response({"message": "Company with this name already exists."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

class CompanyDetail(APIView):
    def get(self,reuest,pk):
        company = get_object_or_404(Company, id=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        print("company : ", company.id)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        company.delete()
        # if serializer.DoesNotExist:
        #     return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        # else:
        #     serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
