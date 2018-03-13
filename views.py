# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from django.http import HttpResponseRedirect
import datetime
import xlrd


def home(request):
	[year,month,day] = datetime.date.today().strftime("%Y-%m-%d").split("-")

	return render(request,'index.html')
