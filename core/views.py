from uuid import uuid4
from django.utils import timezone
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http.response import JsonResponse
from .serlizers import TodoSerializers


@csrf_exempt
def index(request):
    if request.method == "GET":
        res = TodoSerializers(Todo.objects.all(), many=True)
        return JsonResponse(res.data, safe=False)


@csrf_exempt
def single_todo(request):
    if request.method == "GET":
        try:
            res = TodoSerializers(Todo.objects.get(
                id=request.GET["id"]), many=False)
            return JsonResponse(res.data, safe=False)
        except Exception as e:
            return HttpResponse(str(e))


@ csrf_exempt
def add_todo(request):
    if request.method == "POST":
        try:
            data = {
                "id": json.loads(request.body)['data'].get("id", str(uuid4())),
                "name": json.loads(request.body)['data']["name"],
                "pub_date": timezone.now(),
                "status": False,
            }
            t = Todo(**data)
            t.save()
            return HttpResponse("Added successfully!")
        except Exception as e:
            return HttpResponse(str(e), status=500)


@ csrf_exempt
def update_todo(request):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)['data']
            Todo.objects.filter(id=str(request.GET.get('id'))).update(**data)

            return HttpResponse("Updated successfully!")
        except Exception as e:
            return HttpResponse(str(e))


@ csrf_exempt
def delete_todo(request):
    if request.method == "DELETE":
        try:
            print(request.GET.get("id", None))
            t = Todo.objects.get(id=request.GET.get("id", None))
            t.delete()
            return HttpResponse("Deleted successfully!")
        except Exception as e:
            return HttpResponse(str(e))
