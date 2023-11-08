from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import *
import g4f
from django.urls import reverse


def index(request):
    return HttpResponse(f"Hello World")

@csrf_exempt
def ask_ai(request):
    if request.method != "POST":
        return HttpResponse("Unauthorized access")
    data=request.POST.get("ask_data")
    data_api=request.POST.get("ask_api")
    if not data_api or not data:
        return HttpResponse("Invalid api and bank input found.")
    x=api.objects.filter(api_key=str(data_api))
    if not x.exists():
        return HttpResponse("Unauthorized access")
    if int(x[0].No_use)<=0:
        return HttpResponse("Excide the No of Use.Buy New credits ")
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data}],
            stream=True,
        )
        output_data=""
        for message in response:
            output_data+=message
        m1=asked_Ai.objects.create(api=x[0],question=data,answer=output_data)
        m1.save()
        m=x[0]
        m.No_use=int(m.No_use)-1
        m.save()
        return JsonResponse(output_data ,safe=False)
    except:
        return JsonResponse({"Error":"Cannot Access the Gpt api backend."})
