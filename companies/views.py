from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from stock_service.forms import CompanyForm
from stock_service.stock_api import FinnhubApi
from .models import *


class CompanyView(ListView):
    model = Company
    companies = Company.objects.all()
    template_name = 'companies/company_list.html'

    @staticmethod
    def get_company(request):
        if request.method == 'POST':
            form = CompanyForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/thanks/')

        else:
            form = CompanyForm()
        return render(request, 'companies/company_list.html', {'form': form})


class CompanyDetailView(DetailView):
    model = Company
    slug_field = 'url'
    template_name = 'companies/companysingle.html'


async def your_view(request):
    api = FinnhubApi()
    list = await api.list(query='apple')
    return JsonResponse(list, safe=False)


