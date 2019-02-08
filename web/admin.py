# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Expense, Income, Token, Passwordresetcodes


# Register your models here.

admin.site.register(Passwordresetcodes)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)
