from django.shortcuts import render 
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Item.objects.all()
    jumlah = Item.objects.count()

    context = {
        'apk' : 'Nadterial Store',
        'nama' : 'Dyandra Nadine Zahira',
        'kelas' : 'PBP B',
        'material1' : 'Semen 3 roda',
        'material2' : 'Paku Payung',
        'material3' : 'Batu Bata',
        'material4' : 'Cat Nibbonpen',
        'material5' : 'Kabel',
        'deskripsi1': 'Semen dengan kualitas tinggi untuk konstruksi',
        'deskripsi2': 'Paku tahan karat dengan berbagai ukuran',
        'deskripsi3': 'Batu bata merah untuk bangunan anti-goyah',
        'deskripsi4': 'Cat tembok anti-rontok',
        'deskripsi5': 'Kabel untuk menyalurkan energi listrik',
        'harga1' : 'Rp 50.000 per sak',
        'harga2' : 'RP 10.000 per kg',
        'harga3' : 'RP 5.000 per pcs',
        'harga4' : 'RP 45.000 per kaleng',
        'harga5' : 'RP 7.000 per meter',
        'stok1' : '20 sak',
        'stok2' : '50 kg',
        'stok3' : '1000 pcs',
        'stok4' : '30 kaleng',
        'stok5' : '120 meter',
        'products': products,
        'jumlah' : jumlah

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")