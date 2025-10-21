from django.shortcuts import render
from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  





class LeaveRequestView(APIView):
    def post(self, request):
        
        data = request.data
        try:
            # Process the leave request data
            return Response({
                "message": "Leave request submitted successfully",
                "data": data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
