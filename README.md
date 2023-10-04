Nama    : Dyandra Nadine Zahira

NPM     : 2206028264

Kelas   : PBP B

Link adaptable : https://tugas-2-pbp.adaptable.app/main/

##TUGAS-5##

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

    - Element selector membantu dalam menerapkan gaya atau aturan tertentu hanya pada tipe elemen tertentu tanpa perlu menambahkan atribut khusus seperti class. Contohnya adalah memilih elemen berdasarkan tipe yang ingin diubah dalam dokumen HTML.

    - Element selector bermanfaat dalam memastikan desain yang digunakan konsisten sehingga tampilan web terlihat seragam/serasi.

    - Element selector dapat digabung dengan selector lain sehinnga fleksibilitas pemrograman lebih tinggi.

    Element selector tepat digunakan dalam styling umum seperti saat mendesain suatu web karena element selector dapat digunakan untuk mengatur tata letak dan struktur umum sebuah halaman web. Selain itu, element selector juga tepat digunakan untuk mereset atau menghilangkan default pada browser seperti margin '<li>'.

2. Jelaskan HTML5 Tag yang kamu ketahui.

    HTML5 adalah versi terbaru dari bahasa markup HTML yang dapat digunakan untuk merancang dan membangun sebuah halaman web. HTML5 memiliki beberapa kelebihan termasuk elemen atau tag baru yang dapat menciptakan pengalaman web yang lebih dinamis. HTML5 dapat memisahkan konten web dengan desain, mendorong markup semantik, menghilangkan kebutuhan plugin seperti Java, dan mengurangi terjadinya tumpang tindih antara HTML, CSS, serta JavaScript. 

3. Jelaskan perbedaan antara margin dan padding.

    Margin merupakan ruang di luar elemen yang berfungsi mengatur jarak antarelemen yang berada di ruang luar. Sementara itu, padding merupakan rung dalam elemen yang berfungsi mengatur jarak atau tata letak konten di dalam elemen tersebut. Contohnya adalah saat kita memiliki beberapa elemen yang di dalamnya terdapat konten-konten pada sebuah tampilan web, maka kita dapat mengatur jarak atau letak elemen-elemen tersebut menggunakan margin. Setiap konten dalam elemen-elemen tersebut dapat diatur jaraknya atau letaknya menggunakan padding.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    - Tailwind mendefinisikan gaya elemen langsung pada markup HTML menggunakan kelas-kelas yang telah disediakan, sedangkan bootstrap mendefinisikan gaya elemen secara terpisah dalam berkas CSS Bootstrap yang kemudian akan diimplementasikan ke elemen HTML dengan menggunakan kelas-kelas Bootstrap yang sudah disediakan.

    - Tailwind memiliki tingkat fleksibilitas lebih tinggi dalam menentukan tampilan elemen, sedangkan Bootstrap memiliki fleksibilitas lebih rendah karena perlu menyesuaikan gaya CSS Bootstrap.

    - Karena gaya didefinisikan dalam HTML, Tailwaind akan terlihat lebih berantakan dibandingkan Bootstrap yang mendefinisikan gaya pada kelas CSS terpisah.

    - Tailwind memiliki ukuran berkas yang lebih besar dibanding ukuran berkas dari Bootstrap. Selain itu, Bootstrap menyediakan banyak komponen dan gaya yang sudah siap pakai salah satunya seperti navigasi.

    Gunakan Tailwind saat memerlukan tingkat felksibilitas tinggi dalam merancang tampilan web, ingin menentukan gaya langsung dalam markup HTML, menghindari penumpukan kelas yang tidak dipakai, dan mengelola tema khusus untuk proyek. Sementara itu, gunakan Bootsrap saat ingin mengembangkan situs web dengan cepat menggunakan gaya yang sudah disediakan, ingin tampilan markup lebih bersih, dan menyesuaikan tampilan elemen dalam waktu yang lebih singkat.

    

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    checklist (ck)

    ck1 : Pertama-tama saya membuka berkas login.html yang ada pada direktori main/templates di vscode. Kemudian, saya mengubah kode dengan menggunakan CSS. Saya menggunakan Card css pada halaman login, register, edit item, dan tambah inventori. Saya juga melakukan perubahan warna background, warna card, dan hover pada setiap tombol yang ada. Saya juga melakukan perubahan CSS tersebut pada berkas file edit_item.html, register.html, dan create_product.html. Sebelumnya, saya menambahkan tombol edit item dengan cara membuka berkas views.py pada direktori main. Selanjutnya saya membuat fungsi bernama edit_item dan menambahkan routing fungsi tersebut ke dalam urlpatterns pada berkas file urls.py di direktori main. Kemudian, saya menambahkan tombol edit pada tabel di main.html.  

    ck2 : Pertama-tama saya membuka berkas file main.html pada direktori main. Kemudian saya menambahkan style css di dalam berkas tersebut, seperti kustomisasi tombol, tabel, letak teks, hover tombol, dan lainnya. Untuk kustomisasi tombol saya menerapkan css menjadi class yang diimplementasikan di HTML seperti <button class "custom-button">.

    ck3 : Saya membuka berkas file README.md pada root direktori, kemudian memberi batasan tugas 4 dan tugas 5 PBP. Terakhir, saya mengisi berkas readme tersebut dengan pertanyaan-pertanyaan tugas 5.

    ck(bonus) : Saya menambahkan style css pada berkas main.html. Saya membuat style table tr : last-child untuk mengubah warna background dari item terakhir yang di tambahkan ke inventori dan tabel tr : last-child td untuk mengubah teks/isi baris terakhir tabel / item terakhir yang ditambahkan.

    ck4 : Saya membuka comment prompt dan mengaktifkan virtual environtment. Setelah itu saya melakukan git add ., git commit -m "pesan commit", dan git push -u origin main.


REFERENSI :

- https://kodekreasi.com/fungsi-margin-dan-padding-pada-css/

##TUGAS-4##

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

    Django UserCreationForm merupakan import formulir bawaan Django yang memudahkan proses pendaftaran pengguna dalam suatu aplikasi web (register). Form tersebut memiliki 3 default fitur yang harus dimasukkan pengguna, yaitu nama pengguna (username), kata sandi(password), dan konfirmasi kata sandi. Tujuannya adalah agar aplikasi web hanya bisa diakses oleh pengguna yang telah terdaftar dan terverifikasi. Terdapat beberapa kelebihan dari penggunaan UserCreationForm, antara lain :
   
    - Implementasi mudah : UserCreationForm merupakan buit-in dari Django sehingga programmer hanya perlu melakukan import tidak perlu menulis kode program dari awal.
    - Terintegrasi dengan Model : UserCreationForm sudah terintegrasi dengan model sehingga penyimpanan data pengguna sudah terhubung langsung dengan database.
    - Validasi built-in : UserCreationForm sudah memiliki bentuk validasi bawaan, salah satunya seperti password yang tidak boleh hanya terdiri dari angka dan memiliki minimal 8 karakter.

    Selain memiliki kelebihan, UserCreationDjango juga memiliki beberapa kelemahan, antara lain :
   
    - Tampilan terbatas : UserCreationForm hanya berupa formulir Python yang tidak memiliki tampilan HTML sehingga programmer perlu membuat tampilan kustom pada aplikasi web.
    - Fitur terbatas : UserCreationForm hanya memiliki 3 default fitur, yakni username, password, dan konformasi password sehingga programmer perlu menambahkan kode jika ingin menambahkan fitur lain seperti verifikasi email.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Django memiliki built-in autentikasi dan otorisasi yang dapat digunakan langsung oleh programmer. Autentikasi merupakan proses verifikasi identitas pengguna yang akan mengakses aplikasi web. Sementara itu, otorisasi merupakan proses pemberian izin apa yang dimiliki oleh pengguna setelah terverifikasi sebelumnya. Autorisasi akan mengecek apakah pengguna tersebut memiliki hak untuk mengakses aplikasi web dengan cara memeriksa keseluruhan data pengguna (username dan password). Sedangkan, otorisasi akan memastikan bahwa pengguna hanya memiliki akses ke sumber daya atau fitur yang sesuai dengan izin mereka dalam aplikasi web. Kedua hal tersebut memiliki peranan penting dalam menjaga keamanan data terutama data sensitif serta fungsionalitas aplikasi web dari pengguna yang tidak memiliki hak sah (izin).


3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    Cookies merupakan mekanisme penyimpanan kecil untuk menyimpan informasi pada browser pengguna dan mengirimkannya kembali ke server web di setiap permintaan HTTP. Dalam django, cookies digunakan untuk mengelola data sesi pengguna (informasi tentang pengguna selama berinteraksi dengan aplikasi web) sebagai berikut :

    - Autentikasi pengguna : cookies digunakan untuk menyimpan informasi pengguna yang telah berhasil login.
    - Melacak aktivitas pengguna : cookies akan menyimpan hasil pelacakan aktivitas apa saja yang dilakukan pengguna selama berinteraksi di aplikasi web.
    - Preferensi pengguna : cookies dapat menyimpan informasi mengenai preferensi atau pengaturan pengguna.

    Pengelolaan data pada sesi pengguna tersebut dilakukan oleh Django melalui beberapa tahapan, seperti mengaktifkan middleware, mengelola sesi dengan melakukan konfigurasi pengaturan sesi, dan menyimpan data sesi pengguna.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    Penggunaan cookies aman jika diimplementasikan dengan baik dan benar. Namun, terdapat beberapa risiko potensial yang tetap harus diwaspadai, antara lain :

    - Pelanggaran privasi : data cookies yang menyimpan aktivitas pengguna selama berinteraksi dalam web dapat menjadi masalah pelanggaran privasi jika data tersebut disalahgunakan.

    - Pencurian cookies : cookies yang tersimpan di browser pengguna dapat dicuri datanya oleh pelaku tindakan kriminal pencurian data. Hal tersebut dapat terjadi jika ada celah keamanan dalam aplikasi web atau jika penggunamengakses web melalui koneksi (HTTP) yang tidak aman.

    - Overhead : jumlah cookies yang banyak dapat menyebabkan overhead pada kinerja situs dan lalu lintas web.

    - Cross-Site Scripting (XSS) : data-data sensitif yang ada dalam cookies dapat dicuri maupun dimanipulasioleh penyerang dengan cara menyisipkan skrip berbahaya ke dalam halaman web. 

    Dengan demikian, penggunaan cookies yang tepat tetap perlu diawasi agar dapat terhindar dari risiko potensial yang ada.
    
6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    checklist (ck)

    ck1 : Pertama-tama saya membuka command prom (cmd) proyek dan mengaktifkan virtual environment (env). Kemudian, saya membuka direktori proyek di IDE (vscode). Setelah itu, saya membuka berkas file views.py pada direktori main dan melakukan beberapa import, salah satunya import UserCreationForm. Setelah import, saya menambahkan fungsi baru bernama register dalam views.py dan membuat berkas file baru bernama register.html. Berkas tersebut diisi dengan kode template. Kemudian, saya melakukan routing dengan membuka berkas file urls.py pada direktori main dan menambahkan import dari fungsi register serta memasukkan path fungsi tersebut ke dalam urlpatterns. Dengan demikian, fungsi register telah dibuat. Setelah itu, saya membuat fungsi login untuk melakukan autentikasi akun pengguna. Pertama, saya membuka berkas file views.py pada direktori main dan melakukan import authenticate, login. Kemudian, saya membuat fungsi baru bernama login_user dalam berkas tersebut. Selanjutnya, saya membuat berkas file baru bernama login.html dan mengisi berkas tersebut dengan kode template. Saya juga melakukan routing untuk fungsi yang baru dibuat dengan membuka berkas file urls.py dan melakukan import fungsi tersebut serta menambahkan path fungsi login ke dalam urlpatterns. Dengan demikian, fungsi login sudah diterapkan. Selain login, saya membuat fungsi logout dan tombolnya. Pertama-tama saya membuka views.py dan melakukan import logout. Kemudian, saya menambahkan fungsi baru bernama logout_user dalam berkas tersebut. Setelah itu, saya membuka main.html untuk menambahkan potongan kode yang akan menjadi tombol logout. Saya juga melakukan routing fungsi logout dengan membuka berkas file urls.py pada direktori main dan melakukan import fungsi logout serta menambahkan path fungsi tersebut ke dalam urlpatterns. Dengan demikian, fungsi logout telah diterapkan. Setelah membuat 3 fungsi, saya merestriksi akses halaman main dengan membuka berkas file views.py pada direktori main dan menambahkan import login_required. Kemudian, saya menambahkan kode login_required di atas fungsi show_main.

    ck2 : Pertama-tama saya memastikan env pada cmd telah aktif. Kemudian, saya menjalankan perintah python manage.py runserver di cmd. Setelah itu, saya membuka link localhost proyek. Tampilan aplikasi web akan berupa login akun. Saya melakukan register terlebih dahulu pada halaman register dan membuat 2 akun berbeda. Setelah melakukan registrasi, saya login menggunakan salah satu akun tersebut dan menambahkan produk (add product) sebanyak 3 dummy data serta melakukan logout. Saya juga melakukan hal yang sama pada akun kedua.

    ck3 : Untuk menghubungkan model item dengan user pertama-tama saya membuka berkas file models.py pada direktori main dan melakukan import user. Kemudian, saya menambahkan potongan kode user di dalam class model (item) yang telah dibuat. Setelah itu, saya membuka berkas views.py pada direktori main dan mengubah isi fungsi create_product dan show_main. Setiap melakukan perubahan pada models.py saya melakukan migrasi kembali di cmd dengan perintah python manage.py makemigrations dilanjutkan dengan perintah python manage.py migrate. Terakhir, saya melakukan runserver dan membuka link localhost.

    ck4 : Untuk menerapkan cookies, pertama-tama saya memastikan aplikasi sedang tidak berjalan (sudah logout). Kemudian, saya membuka berkas views.py pada direktori main dan melakukan beberapa import salah satunya datetime. Setelah itu, saya mengubah isi blok if pada fungsi login_user yang ada di dalam berkas views.py. Saya juga menambahkan potongan kode request cookies pada fungsi show_main (dalam context) di berkas tersebut. Setelah itu, saya mengubah isi fungsi logout_user dengan potongan kode baru. Kemudian, saya membuka main.html dan menambahkan potongan kode di antara tabel dan tombol logout. Terakhir, saya me-refresh halaman aplikasi web dan melakukan login kembali.

    ck5 : Pertama, saya membuka berkas README.md pada vscode. Kemudian, saya mengisi berkas dengan jawaban dari pertanyaan-pertanyaan tugas 4.

    ck6 : Pertama-tama saya membuka cmd dan memastikan env telah aktif. Kemudian saya melakukan perintah git add., git commit -m "pesan", dan git push -u origin main untuk mengumpulkan tugas ke repository yang sebelumnya telah dibuat.

    ck7 (bonus) : Untuk membuat tombol hapus item, tambah stok, dan kurang stok, pertama-tama saya membuat fungsi delete_item, add_stock, dan reduce_stock di berkas views.py pada direktori main. Kemudian, saya melakukan routing untuk ketiga fungsi tersebut dengan membuka urls.py pada direktori main dan melakukan import ketiga fungsi tersebut serta menambahkan path ketiga fungsi tersebut ke dalam urlpatterns. Setelah itu, saya menambahkan potongan kode pada main.html. Saya melakukan for loop produk yang ada dalam tabel, lalu menambahkan potongan kode untuk tombol hapus, tambah, dan kurang sama seperti tombol login dan logout. Terakhir, saya melakukan runserver dan login kembali ke halaman aplikasi web.

Referensi :

- https://docs.djangoproject.com/en/4.2/topics/auth/default/


##TUGAS-3##

1. Apa perbedaan antara form POST dan form GET dalam Django?
    
    POST dan GET dalam Django memiliki beberapa perbedaan, antara lain :

    1. GET method mengirimkan data kepada pengguna melalui URL yang dapat dilihat atau dibaca. Sedangkan, POST mengirimkan data secara tidak terlihat kepada pengguna 
       melalui HTTP POST.

    2. GET tidak bisa mengirimkan data dengan ukuran besar karena terdapat limit pada URL yang diizinkan oleh browser dan server. Sedangkan, POST dapat mengirimkan data           dengan ukuran besar. 

    3. GET memiliki tingkat keamanan yang lebih rendah daripada POST karena data ditampilkan dalam URL atau dapat dilihat dan dibaca oleh pengguna. Dengan demikian,               penggunaan GET juga lebih rentan dicuri oleh pelaku kejahatan IT dibandingkan penggunaan POST.

    4. Berdasarkan tingkat keamanannya, GET digunakan pada data yang bersifat umum (tidak sensitif). Sementara itu, POST digunakan untuk mengirimkan data penting dan              sensitif.

    5. GET hanya mengizinkan penggunaan tipe data karakter ASCII, sedangkan POST mengizinkan penggunaan seluruh tipe data.

    6. Request melalui GET akan ditempatkan pada cache memori dan history milik browser. Sementara itu, request melalui POST tidak ditempatkan pada cache memori dan               history milik browser.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    1. Struktur Data :

        -XML : Bahasa markup dan format file yang digunakan untuk menyimpan, mentransmisikan, dan merekonstruksi data.
        -JSON : Format file standar terbuka dan format pertukaran data dengan teks berbentuk pasangan key-value yang dapat dibaca oleh manusia.
        - HTML : Bahasa markup yang digunakan untuk menentukan struktur halaman dalam pengembangan web.

    2. Tipe Data :

        -XML : Dapat merepresentasikan berbagai jenis data struktural dan semantik dengan tipe data berbeda. Namun, XML tidak mendukung penggunaan array.
        -JSON : Mendukung tipe data dasar seperti string, boolean, array, angka, dan objek.
        -HTML : Dapat merepresentasikan elemen-elemen khusus dalam konten web, seperti teks, gambar, dan lainnya.

    3. Lintas Platform:

        -XML: Mendukung di banyak bahasa pemrograman, tetapi perlu lebih banyak kode untuk mengurai dan memanipulasi data XML.
        -JSON: Didukung oleh hampir semua bahasa pemrograman modern dan memiliki dukungan yang lebih baik untuk mengurai data JSON.
        -HTML: Digunakan dalam pengembangan web dan memiliki dukungan penuh dalam semua peramban web modern.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    Jawab : JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa keunggulan yang mendukung tujuan tersebut. Yang pertama, JSON memiliki format sederhana dan mudah dibaca oleh manusia. Format JSON berbentuk seperti dictionary dalam python, yakni nama(key) dan nilai(value) yang mudah dikelola serta mudah dipahami. Keunggulan yang kedua adalah JSON memiliki format data yang ringan (tidak memiliki overhead signifikan) sehingga pertukaran data dapat berjalan secara efisien dan aplikasi web beroperasi dengan cepat. Keunggulan ketiga adalah JSON memungkinkan komunikasi lintas platform yang mudah antar bagian aplikasi web ataupun antar aplikasi web berbeda karena JSON didukung oleh hampir seluruh bahasa pemrograman, seperti python, java, dan lainnya. Keunggulan yang keempat adalah JSON memiliki struktur yang ringkas sehingga dapat menghemat bandwitch saat mengirim data melalui jaringan. Keunggulan terakhir JSON adalah dapat digunakan dalam pembaruan dinamis pada halaman web tanpa perlu melakukan refresh halaman web. Dari beberapa keunggulan JSON diatas, dapat disimpulkan bahwa JSON memiliki keunggulan utama dalam kesederhanaan struktur dan format sehingga mudah dibaca dan dipahami manusia.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

    Jawab : checklist(ck)

    ck1 : Pertama-tama, saya membuka direktori lokal proyek yang telah dibuat pada tugas 2, yakni direktori Nadterial_store di IDE seperti vscode. Kemudian, saya membuka command prompt (cmd) direktori lokal tersebut dan mengaktifkan virtual environment (env). Setelah env aktif, saya mengubah path pada berkas urls.py yang berada dalam direktori nadterial_store melalui vscode. Path yang sebelumnya berupa main/ diubah menjadi string kosong (''). Sebelum membuat form, saya membuat kerangka dari views web agar tidak terjadi redundansi kode dan desain aplikasi web konsisten. Pertama, saya membuat folder templates dalam folder Nadterial_store yang paling luar pada vscode. Di dalam folder templates tersebut, saya membuat berkas file bernama base.html yang akan menjadi kerangka umum halaman aplikasi web. Setelah itu, berkas tersebut diisi dengan kode-kode yang akan menjadi kerangka umum. Setelah selesai pada berkas base.html, saya membuka berkas settings.py yang juga ada dalam direktori nadterial_store untuk mengubah isi dari 'DIRS'. Isi 'DIRS' yang berada dalam TEMPLATES[] ditambahkan dengan [BASE_DIR/'templates'],. Setelah membuat kerangka umumnya pada base.html, saya mengubah isi dari main.html, yaitu halaman aplikasi web sesuai dengan kerangka dasar. Pertama-tama, saya membuka berkas main.html pada direktori main/templates di vscode. Kemudian, saya menambahkan kode untuk meng-extends base.html dan membuat kode block content serta penutup block tersebut. Setelah itu, saya mengubah format nama,kelas, dan judul tiap kolom tabel yang saya buat di aplikasi web sebelumnya sesuai kerangka serta menghapus kode html isian daftar produk-produk di nadterial_store sebelumnya. Setelah melakukan implementasi kerangka dasar, saya baru membuat form input data pada html. Pertama, saya membuat berkas file baru pada direktori main bernama forms.py. Dalam berkas tersebut, lakukan import ModelForm dari Django.forms dan import Item dari main.models. Kemudian, saya membuat kelas ProductForm dengan parameter ModelForm. Sebelum membuat field, saya membuat objek bernama Product dari model yang digunakan untuk form. Kemudian, saya membuat field dari kelas Meta sesuai dengan elemen yang dibutuhkan pada tabel produk di main.html, yaitu name, description, picture, amount, dan price. Setelah selesai pada file forms.py, saya membuka berkas file views.py yang ada dalam direktori main. Saya menambahkan beberapa import dalam berkas tersbut, antara lain import HttpResponseRedirect dari django.http, import ProductForm dari main.forms, import item dari main.models, dan import reverse dari django.urls. Setelah melakukan import, saya menambahkan sebuah fungsi baru untuk membuat formulir penambahan produk yang akan dimasukkan pengguna. Fungsi tersebut bernama create_product dengan parameter request dan pengembalian fungsi tersebut juga berupa request pengguna. Kemudian, pada fungsi show_main yang telah dibuat sebelumnya, saya menambahkan kode 'products = Item.objects.all()' guna mengambil seluruh object Product pada database. Setelah selesai, saya membuka berkas file urls.py milik direktori main untuk menambahkan import fungsi baru yang telah dibuat, yakni fungsi create_product serta melakukan routing pada fungsi tersebut dengan menambahkan path fungsi ke dalam urlpatterns. Selanjutnya, saya membuat berkas baru bernama create_product.html dalam direktori main/templates dan mengisi file tersebut dengan kode-kode yang akan menampilkan tabel dari produk-produk Nadterial store. Yang terakhir adalah saya menambahkan implementasi kerangka dasar untuk daftar produk - produk Nadterial store menggunakan for-loop serta menambahkan tombol add product pada halaman aplikasi web di berkas main.html. Dengan demikian, saya telah membuat input form pada aplikasi web.

    ck2 dan ck3 : Pertama-tama, saya membuka berkas file views.py yang ada dalam direktori main (seluruh fungsi dibuat dalam berkas tersebut). Kemudian, saya menambahkan beberapa import, yakni import HttpResponse dan import serializers. Fungsi yang pertama telah dibuat bernama create_product. Kemudian, saya membuat fungsi kedua, yakni show_xml dengan parameter request dan pengembalian fungsi tersebut dalam bentuk XML. Setiap membuat fungsi baru, saya juga melakukan routing dengan cara menambahkan path fungsi tersebut ke dalam urlpattern yang ada di berkas urls.py pada direktori main (seluruh routing fungsi dilakukan pada berkas tersebut). Setiap fungsi baru juga saya import di berkas tersebut agar dapat diakses. Setelah itu, saya membuat fungsi ketiga bernama show_json dengan parameter request dan pengembalian fungsi tersebut dalam JSON. Fungsi yang keempat saya buat bernama show_xml_by_id dengan parameter request dan id (data) dan pengembalian fungsi tersebut dalam bentuk XML juga. Fungsi kelima atau terakhir yang saya buat bernama show_json_by_id dengan parameter request dan id (data) dan pengembalian fungsi tersebut dalam bentuk JSON.

    ck4 : Pertama-tama buka berkas README.md pada IDE seperti vscode. Kemudian, saya memberi batasan README antara tugas 2 dan tugas 3. Terakhir, saya mengisi README dengan jawaban dari pertanyaan-pertanyaan tugas 3.

    ck5 : Pertama-tama, saya membuka Postman dan login. Kemudian, saya memasukkan link HTML, XML, JSON, XML[id] (saya mengambil data ke-2), dan JSON [id] (saya mengambil data ke-1) pada kolom method GET. Kemudian, setiap respon yang diberikan dari link tersebut saya screenshot dan saya lampirkan di README.md.

    ck6 : Saya membuka cmd pada direktori lokal proyek kemudian tidak lupa untuk memastikan env telah aktif. Saya lakukan perintah git add ., git commit -m, dan git push -u origin main untuk meng-upload hasil penyelesaian tugas 3.

    ck7 (Bonus) : Pertama, saya membuka berkas views.py pada direktori main. Kemudian, di dalam fungsi show_main saya menambahkan kode 'jumlah = Item.objects.count()' dan kode key-value 'jumlah' : jumlah. Tujuannya adalah untuk menghitung jumlah keseluruhan item/produk yang telah ditambahkan ke aplikasi web. Selanjutnya, saya membuka berkas file main.html dan menambahkan implementasi kerangka dasar di bawah kerangka kelas dengan tulisan berupa 'Kamu menyimpan X item pada aplikasi ini' dengan X menggunakan variable jumlah yang sebelumnya dibuat di views.py. 

5. Berikut screenshot hasil akses URL pada Postman.
   
![XML](https://github.com/nadinezhr/Tugas-2-PBP/assets/130216958/2eed1775-e7f2-4bc5-85ae-acb6822b007b)

![Json](https://github.com/nadinezhr/Tugas-2-PBP/assets/130216958/293f8d65-675d-46cf-89d1-9cd2d4a6197c)

![XmlID](https://github.com/nadinezhr/Tugas-2-PBP/assets/130216958/341391d7-8ebd-4221-936a-7f60c72fc3e0)

![JsonID](https://github.com/nadinezhr/Tugas-2-PBP/assets/130216958/0d8d00e8-7c79-4ccd-9fc9-f34506c1d90e)

![HTML FIX](https://github.com/nadinezhr/Tugas-2-PBP/assets/130216958/64e7d9d2-e1df-4ab8-996e-e5a87c2f9062)


REFERENSI :

- https://www.geeksforgeeks.org/difference-between-http-get-and-post-methods/
- https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/



##TUGAS-2##

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Jawab : ck (cheklist)

    ck1 : Sebelum membuat proyek Django, perlu untuk membuat direktori lokal, membuat repositori baru di GitHub dengan status public, melakukan inisiasi repositori baru dengan perintah - init di command (cmd), melakukan konfigurasi username dan email GitHub di cmd, dan menghubungkan direktori lokal kita dengan repositori di git. Cara menghubungkannya dapat dilakukan dengan menjalankan perintah branch -M (nama branch) dilanjutkan dengan melakukan git remote add origin (link repositori) di cmd proyek. Kemudian, untuk membuat proyek Django kita memerlukan virtual environment (env) agar tidak terjadi konflik dependensi dengan proyek lain. Yang pertama adalah menginisiasi env dan mengaktifkannya di command (cmd). Setelah memastikan env telah aktif, kita perlu menambahkan berkas requirements.txt beserta dependensinya ke dalam direktori proyek lokal yang telah dibuat dan melakukan instalasi pada berkas tersebut. Instalasi dilakukan di cmd setelah menambahkan file requirements. Setelah itu, lakukan perintah startproject pada cmd untuk memulai proyek Django. Agar aplikasi web dapat diakses, kita perlu memberikan izin pada semua host yang mengakses. Hal tersebut dilakukan dengan membuka berkas file settings.py yang ada dalam direktori lokal pada IDE seperti vscode. Terakhir, tambahkan ["*"] pada ALLOWED_HOST. Dengan demikian, proyek Django baru telah dibuat.

    ck2 : Sebelum membuat aplikasi, pastikan sudah mengaktifkan virtual environment (env) di cmd proyek kita. Setelah aktif, lakukan perintah python manage.py startapp (nama apk, yakni main) agar terbentuk struktur awal bagi aplikasi kita. Struktur tersebut berada dalam direktori main dengan isian berupa _init_.py, admin.py, apps.py, models.py, tests.py, urls.py, dan views.py. Kemudian, buka berkas file settings.py di direktori proyek pada IDE seperti vscode. Setelah itu, kita perlu mendaftarkan aplikasi main ke dalam proyek kita, yakni dengan menambahkan 'main' ke INSTALLED_APPS yang ada pada berkas file tersebut. Dengan demikian, kita telah membuat aplikasi main.

    ck3 : Routing proyek dilakukan agar proyek terhubung dengan tampilan main sehingga aplikasi main dapat dijalankan. Pertama-tama buka berkas urls.py yang ada dalam direktori proyek pada IDE seperti vscode. Selanjutnya, kita perlu mengimport path dan include agar dapat mengambil URL aplikasi lain (main) ke dalam berkas urls.py yang ada dalam direktori proyek bukan direktori main. Kemudian, tambahkan path URL ('/main') agar rute mengarah ke berkas urls.py yang ada dalam direktori main. Dengan demikian, proyek kita dan aplikasi main telah terhubung.

    ck4 : Pertama-tama buka berkas file models.py yang ada dalam direktori main (struktur awal aplikasi) pada IDE seperti vscode. Yang kedua, kita perlu mengimport models dari django.db. Setelah melakukan import, buat class dengan nama Item dan parameternya adalah models.Model. Kita dapat membuat atribut name, amount, description, dan lainnya dengan menggunakan parameter models tersebut serta menyesuaikan jenis/tipe dari atribut. Contohnya seperti amount dengan tipe atribut IntegerField. Terakhir, jangan lupa untuk selalu melakukan migrasi setiap ada perubahan pada models.py agar Django tetap dapat melacak perubahan pada basis data model.

    ck5 : Pertama buka berkas file views.py yang ada dalam direktori main pada IDE seperti vscode. Kedua, kita perlu melakukan import render dari django.shortcuts agar dapat menggunakan render. Ketiga, buat fungsi seperti di python (menggunakan def dan parameter request) dengan isian seperti dictionary (key-value) bernama context agar dapat dikembalikan ke dalam template HTML. Terakhir, kita perlu me-return isi fungsi menggunakan render. Render digunakan agar dapat mengisi template dengan data dinamis sebelum mengirimkan ke client sebagai respon.

    ck6 : Routing pada aplikasi main dilakukan agar aplikasi tersebut dapat diakses di web. Pertama, buka berkas file urls.py yang ada dalam direktori main (bukan proyek) pada IDE seperti vscode. Kedua, kita perlu melakukan import dari django.urls berupa path dan fungsi pada views.py, yakni fungsi show_main agar bisa digunakan. Ketiga, buat variabel app_name berisi nama aplikasi, yaitu main. Terakhir, masukkan urlpattern atau path yang berkaitan dengan aplikasi main, seperti show_main.

    ck7 : Pertama-tama buka web adaptable dan login menggunakan akun GitHub yang terhubung. Kemudian, pilih buat aplikasi baru dan isi syarat-syarat yang diperlukan, seperti nama aplikasi, repositori yang akan dihubungkan, versi python yang dipakai, tipe basis data yang akan digunakan, branch yang digunakan di GitHub, dan start command. Terakhir, lakukan proses deployment aplikasi.

    ck8 : Buka direktori lokal proyek pada IDE seperti vscode. Kemudian buat file baru bernama README.md. Terakhir, isi berkas file tersebut dengan jawaban dari pertanyaan-pertanyaan pada tugas 2 PBP.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Gambar Bagan](https://github.com/nadinezhr/Tugas-2-PBP/blob/b51c650d787e40e610f8948691bef5d710f0c6f3/Bagan%20tugas2%20PBP.jpeg)
    Penjelasan : client akan melakukan request melalui tampilan web (html), request tersebut akan masuk ke urls.py. urls.py akan meneruskan request tersebut ke views.py untuk diproses. Untuk memproses request, views.py akan mengakses data yang diperlukan di models.py, seperti membaca atau menulis data. Berkas html akan mengakses hasil request client pada views.py sebelum ditampilkan pada tampilan web.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Jawab : Virtual environment memiliki beberapa manfaat dalam mengembangkan suatu perangkat lunak berbasis Python seperti web. Dengan basis Python, virtual environment akan menyesuaikan dan mengatur versi Python yang sesuai dengan proyek. Selain itu, virtual environment akan mengisolasi lingkungan proyek yang sedang dikerjakan agar tidak terjadi konflik dependensi (elemen,komponen,perangkat lunak lain) dengan proyek lain sehingga kebersihan sistem tetap terjaga. Virtual environment juga menyediakan paket Python ('pip') yang dapat digunakan untuk mengupgrade, menginstal, dan menghapus dependensi proyek. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, untuk lebih memudahkan pekerjaan serta menghindari konflik yang mungkin muncul jika tidak melakukan isolasi lingkungan proyek, sebaiknya kita selalu menggunakan virtual environtment dalam membangun aplikasi web berbasis Django agar proyek mudah dikelola, terorganisir, dan independen.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    Jawab :

    1. MVC : Model-View-Controller (MVC) merupakan suatu pola desain yang membagi komponen yang saling berkaitan dalam pengerjaan proyek web menjadi 3 bagian, yakni model, view, dan controller. Tujuan dari pembagian tersebut adalah agar memudahkan programmer dalam memelihara kode, memodifikasi UI(tampilan), dan mengembangkan proyek. Model berhubungan dengan data dan logika yang digunakan sehingga model berperan dalam memodifikasi dan menambahkan data serta mengambil data dari database. Kemudian, view berhubungan dengan interface(tampilan) yang dilihat oleh pengguna sehingga berperan dalam menampilkan data ke pengguna. Terakhir adalah controller sebagai perantara model dan view. Controller berperan dalam memproses interaksi pengguna, kemudian memberitahu model, dan hasilnya akan ditampilkan oleh view.

    2. MVT : Model-View-Template (MVT) merupakan suatu pola desain yang membagi komponen yang saling berkaitan dalam pengerjaan proyek web menjadi 3 bagian, yakni model, view, dan template. Tujuan dari pembagian tersebut adalah untuk memisahkan presentasi, logika aplikasi, dan tampilan sehingga proyek mudah dipelihara, diuji, serta dikembangkan. Model berhubungan dengan struktur basis data Django sehingga berperan dalam menambahkan, menghapus, mengupdate, dan membaca database. Kemudian, view berhubungan dengan pemrosesan respon pengguna dan menggunakan model untuk menampilkan hasil respon. View seperti sebuah fungsi dalam Python. Yang terakhir adalah template yang berhubungan dengan tampilan halaman web dalam Django. Template menggabungkan data dari model ke HTML.

    3. MVVM : Model-View-ViewModel (MVVM) merupakan suatu pola desain yang membagi komponen yang saling berkaitan dalam pengerjaan proyek web menjadi 3 bagian, yakni model, view, dan viewmodel. Tujuan dari pembagian tersebut adalah untuk memudahkan programmer dalam melakukan testing terpisah, memelihara, dan mengembangkan kode. Model berhubungan dengan logika bisnis dan aplikasi salah satunya seperti pemrosesan dan penyimpanan data. Kemudian, view berhubungan dengan presentasi antarmuka seperti teks, tata letak, gambar, dan lainnya. Yang terakhir adalah viewmodel sebagai perantara model dan view. Viewmodel akan mengantarkan input pengguna dari view ke model untuk diproses dan mengantarkan output (hasil proses) dari model ke view. 

    Perbedaan MVC, MVT, dan MVVM :
    - Perbedaan utama terletak pada tugas controller, template, dan viewmodel. Controller bertanggung jawab untuk mengontrol aliran data antara Model dan View, serta mengatur interaksi pengguna. Controller mengambil peran mediator dalam MVC. Template bertanggung jawab untuk merender tampilan HTML dan menggabungkannya dengan data dari Model. Viewmodel bertanggung jawab untuk menghubungkan Model dengan View. ViewModel menyediakan abstraksi atas data yang akan ditampilkan di View, serta mengatur perubahan data agar sesuai dengan tampilan yang ada di View. 
    - Perbedaan MVC, MVT, dan MVVM juga terletak pada data binding (pengikatan data). MVC dan MVT tidak memiliki pengikatan data secara default sehingga memerlukan kode tambahan. Sementara itu, MVVM memiliki default pengikatan data sehingga memungkinkan model dan view terhubung secara otomatis.
    - Perbedaan MVC, MVT, dan MVVM juga terletak pada kompatibilitas. MVVM memiliki kompatibilitas paling unggul di antara ketiganya, sedangkan MVC memiliki lebih banyak penyesuaian pola dibanding MVT.


REFERENSI :

3. https://revou.co/panduan-teknis/python-virtual-environment#:~:text=Salah%20satu%20manfaat%20utama%20penggunaan,mungkin%20berbeda%20dengan%20proyek%20lainnya.

4. - https://revou.co/kosakata/mvc#manfaat-mvc
   - https://www.educative.io/answers/what-is-mvt-structure-in-django
   - https://revou.co/kosakata/mvvm

