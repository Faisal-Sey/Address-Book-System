from django.urls import path
from .views import create_contact, upload_contacts, delete_contact, \
  edit_contact, get_all_contacts, get_contact, get_contacts_page

urlpatterns = [
  path("create", create_contact, name="create_contact"),
  path("upload", upload_contacts, name="upload"),
  path("update", edit_contact, name="edit_contact"),
  path("delete", delete_contact, name="delete_contact"),
  path("contact", get_contact, name="get_contact"),
  path("contacts/", get_all_contacts, name="get_contacts"),
  path("contacts/<int:id>/", get_contacts_page, name="get_contacts_page")
]
