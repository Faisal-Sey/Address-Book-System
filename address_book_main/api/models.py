from django.db import models
from django.forms.models import model_to_dict


class Address(models.Model):
  contact = models.CharField(max_length=50)

  def __str__(self):
    return self.contact

  def to_json(self):
    res = {"id": self.pk, **model_to_dict(self, fields=["contact"])}
    return res
