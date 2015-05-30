# -*- coding: utf-8 -*-
from django.http import HttpResponse


def benchmark(request):
    return HttpResponse('benchmarking...')
