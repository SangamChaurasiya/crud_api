from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.serializers import StudentSerializer
from api.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io


# @csrf_exempt
# def student_data(request):
#     if request.method == "GET":
#         data = request.body
#         stream = io.BytesIO(data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id', None)

#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#         else:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many=True)

#         json_data = JSONRenderer().render(data=serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "POST":
#         data = request.body
#         stream = io.BytesIO(data)
#         python_data = JSONParser().parse(stream)

#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()

#             res = {'msg': 'Data Created !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "PUT":
#         data = request.body
#         stream = io.BytesIO(data)
#         python_data = JSONParser().parse(stream)

#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)

#         # # Complete Update - Required all data from Front-end/Client
#         # serializer = StudentSerializer(stu, data=python_data)

#         # Partial Update - All data not required
#         serializer = StudentSerializer(stu, data=python_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()

#             res = {'msg': 'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)

#         id = python_data.get('id')
#         try:
#             stu = Student.objects.get(id=id)
#             stu.delete()

#             res = {'msg': 'Data Deleted !!'}
#             json_data = JSONRenderer().render(data=res)
#             return HttpResponse(json_data, content_type='application/json')
#         except:
#             res = {'error': 'Data Not Found !!'}
#             # json_data = JSONRenderer().render(data=res)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(res)


# The above function using the Class-Based Views
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)

        json_data = JSONRenderer().render(data=serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()

            res = {'msg': 'Data Created !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')
        stu = Student.objects.get(id=id)

        # # Complete Update - Required all data from Front-end/Client
        # serializer = StudentSerializer(stu, data=python_data)

        # Partial Update - All data not required
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()

            res = {'msg': 'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')
        try:
            stu = Student.objects.get(id=id)
            stu.delete()

            res = {'msg': 'Data Deleted !!'}
            json_data = JSONRenderer().render(data=res)
            return HttpResponse(json_data, content_type='application/json')
        except:
            res = {'error': 'Data Not Found !!'}
            # json_data = JSONRenderer().render(data=res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res)
         