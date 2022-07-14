from django.test import TestCase
from ..models import Address

class AddressTestCase(TestCase):
  def setUp():
    Address.objects.create(contact="0500000000")
    Address.objects.create(contact="0544444444")

  def test_create_contact(self):
    contact_1 = Address.objects.create(contact="9999999999")
    contact_2 = Address.objects.create(contact="8888888888")
    self.assertEquals(contact_1.contact, "9999999999")
    self.assertEquals(contact_2.contact, "8888888888")



