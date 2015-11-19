# -*- coding: utf-8 -*-
import json

from django.utils import six
from django.http import HttpResponse
from django.db.models import get_model


def filterchain_all(request, **kwargs):
    Model = get_model(kwargs['app_name'], kwargs['model_name'])
    obj = Model.objects.get(pk=kwargs['pk'])
    qs = getattr(obj, kwargs['method_name'])()

    final = [
        {
            'value': item.pk,
            'display': six.text_type(item)
        } for item in qs]

    return HttpResponse(json.dumps(final), content_type='application/json')
