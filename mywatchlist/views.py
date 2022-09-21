from email import message
from django.shortcuts import render
from mywatchlist.models import watchlist
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist = watchlist.objects.all()
    context = {
        'list_watchlist' : data_watchlist,
        'nama' : 'Muhammad Satria Ramadhan',
        'npm' : '2106751695'
    }
    return render(request, "mywatchlist.html", context)

def show_watchlist_xml(request):
    data_watchlist = watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_watchlist_json(request):
    data_watchlist = watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_watchlist_xml_by_id(request, id):
    data_watchlist = watchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_watchlist_json_by_id(request, id):
    data_watchlist = watchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")