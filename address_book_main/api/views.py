from io import BytesIO
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import Address
from . import signals
import json


@csrf_exempt
def create_contact(request, *args, **kwargs):
  if request.method == "POST":
    data = json.loads(request.body)
    contact = data.get("contact")
    
    try:
      new_contact = Address(contact=contact)
      new_contact.save()
      return JsonResponse({"status": "success"})

    except Exception as e:
      print(e)
      return JsonResponse({"status": "An error occurred"})

  else:
    return JsonResponse({"error": "Not Allowed"})


@csrf_exempt
def edit_contact(request, *args, **kwargs):
  if request.method == "POST":
    data = json.loads(request.body)
    id = data.get("id")
    contact = data.get("contact")

    try:
      address = Address(pk=id)
      address.contact = contact
      address.save()
      return JsonResponse({"status": "success"})

    except Exception as e:
      print(e)
      return JsonResponse({"status": "An error occurred"})
  
  else:
    return JsonResponse({"error": "Not Allowed"})


@csrf_exempt
def get_all_contacts(request, *args, **kwargs):
  if request.method == "GET":
    contacts = Address.objects.all()
    data = {}
    try:
      for address in contacts:
        data[address.id] = address.to_json()

      return JsonResponse({"status": "success", "data": data})

    except Exception as e:
      print(e)
      return JsonResponse({"status": "An error occurred"})
  
  else:
    return JsonResponse({"error": "Not Allowed"})


@csrf_exempt
def get_contacts_page(request, id):
  contacts = Address.objects.all()
  paginator = Paginator(contacts, 20)
  current_page = paginator.page(id)
  data = {}

  for address in current_page.object_list:
    data[address.id] = address.to_json()

  return JsonResponse({"status": "success", "data": data})


@csrf_exempt
def get_contact(request, *args, **kwargs):
  if request.method == "GET":
    post_data = json.loads(request.body)
    id = post_data.get("id")

    data = {}
    try:
      address = Address.objects.get(id=id)
      data = address.to_json()
      return JsonResponse({"status": "success", "data": data})

    except Exception as e:
      print(e)
      return JsonResponse({"status": "An error occurred"})
  
  else:
    return JsonResponse({"error": "Not Allowed"})


@csrf_exempt
def delete_contact(request, *args, **kwargs):
  if request.method == "DELETE":
    post_data = json.loads(request.body)
    id = post_data.get("id")

    try:
      Address.objects.get(id=id).delete()
      return JsonResponse({"status": "success"})

    except Exception as e:
      print(e)
      return JsonResponse({"status": "An error occurred"})
  
  else:
    return JsonResponse({"error": "Not Allowed"})



@csrf_exempt
def upload_contacts(request, *args, **kwargs):
  if request.method == "POST":
    post_data = request.FILES["image"]
    try:
      file = BytesIO(post_data.read())
      content_list = file.getvalue().decode("utf-8").split("\n")

      for address in content_list:
        get_address = address.split(",")[1].strip()
        new_contact = Address(contact=get_address)
        new_contact.save()

      signals.upload_complete.send(sender="upload_complete", bool=True)

      return JsonResponse({"status": "success"})

    except Exception as e:
      print(e)
      return JsonResponse({"status": "An error occurred"})

  else:
    return JsonResponse({"error": "Not Allowed"})


