from django.shortcuts import render 

def show_main(request):
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
        'stok5' : '120 meter'

    }


    return render(request, "main.html", context)

