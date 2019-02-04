# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import JsonResponse
from json import JSONEncoder
#-------------------------------------------------------------
from django.views.decorators.csrf import csrf_exempt
#-------------------------------------------------------------
from web.models import Token, Expense, Income
from django.contrib.auth.models import User
#-------------------------------------------------------------
from datetime import datetime
import pytz


# Create your views here.

@csrf_exempt
def submit_expense(request):

    # TODO: validate data. user might be fake. token might be fake. amount might be fake. text might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' in request.POST:
        date = request.POST['date']
    else:
        tz_TR = pytz.timezone('Asia/Tehran')
        date = datetime.now(tz_TR).strftime("%Y-%m-%d %H:%M:%S")

    Expense.objects.create(user= this_user, amount= request.POST['amount'],
    text= request.POST['text'], date= date)
    print request.POST

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):

    # TODO: validate data. user might be fake. token might be fake. amount might be fake. text might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' in request.POST:
        date = request.POST['date']
    else:
        tz_TR = pytz.timezone('Asia/Tehran')
        date = datetime.now(tz_TR).strftime("%Y-%m-%d %H:%M:%S")

    Income.objects.create(user= this_user, amount= request.POST['amount'],
    text= request.POST['text'], date= date)
    print request.POST

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
