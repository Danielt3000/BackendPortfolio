from projects.models import Project
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from rest_framework import viewsets
from projects.serializers import ProjectSerializer




class ProjectViews(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()





# @api_view(["GET","POST"])
# def projects(request):

#     #invoke serialzer and rteturn to client
#     if request.method == "GET":
#         data = Project.objects.all()
#         serializer = ProjectSerializer(data, many=True)
#         return Response({"projects": serializer.data})
#     elif request.method =="POST":
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"customer" :serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# @api_view(["GET","POST", "DELETE"])
# def project(request, id):
#     try:
#         data = Project.objects.get(pk=id)
#     except Project.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":    
#         serializer = ProjectSerializer(data)
#         return Response({"project": serializer.data})
#     elif request.method == "DELETE":
#             data.delete()
#             return Response (status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "POST":
#         serializer = ProjectSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"customer": serializer.data})
#         return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)
  