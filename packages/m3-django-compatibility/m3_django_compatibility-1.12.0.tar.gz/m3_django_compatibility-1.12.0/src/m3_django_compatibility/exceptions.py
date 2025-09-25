# coding: utf-8
from django import VERSION


_VERSION = VERSION[:2]


if _VERSION <= (3, 0):
    from django.db.models.fields import FieldDoesNotExist
else:
    from django.core.exceptions import FieldDoesNotExist
