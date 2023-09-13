Nama    : Dyandra Nadine Zahira

NPM     : 2206028264

Kelas   : PBP B

Link adaptable : https://tugas-2-pbp.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab : ck (cheklist)

ck1 : Sebelum membuat proyek Django, perlu untuk membuat direktori lokal, membuat repositori baru di GitHub dengan status public, melakukan inisiasi repositori baru dengan perintah - init di command (cmd), melakukan konfigurasi username dan email GitHub di cmd, dan menghubungkan direktori lokal kita dengan repositori di git. Cara mengubungkannya dapat dilakukan dengan menjalankan perintah branch -M (nama branch) dilanjutkan dengan melakukan git remote add origin (link repositori) di cmd proyek. Kemudian, untuk membuat proyek Django kita memerlukan virtual environment (env) agar tidak terjadi konflik dependensi dengan proyek lain. Yang pertama adalah menginisiasi env dan mengaktifkannya di command (cmd). Setelah memastikan env telah aktif, kita perlu menambahkan berkas requirements.txt beserta dependensinya ke dalam direktori proyek lokal yang telah dibuat dan melakukan instalasi pada berkas tersebut. Instalasi dilakukan di cmd setelah menambahkan file requirements. Setelah itu, lakukan perintah pada cmd untuk memulai proyek Django. Agar aplikasi web dapat diakses, kita perlu memberikan izin pada semua host yang mengakses. Hal tersebut dilakukan dengan membuka berkas file settings.py yang ada dalam direktori lokal pada IDE seperti vscode. Terakhir tambahkan ["*"] pada ALLOWED_HOST. Dengan demikian, proyek Django baru telah dibuat.

ck2 : Sebelum membuat aplikasi, pastikan sudah mengaktifkan virtual environment (env) di cmd proyek kita. Setelah aktif, lakukan perintah python manage.py startapp (nama apk, yakni main) agar terbentuk struktur awal bagi aplikasi kita. Struktur tersebut berada dalam direktori main dengan isian berupa _init_.py, admin.py, apps.py, models.py, tests.py, urls.py, dan views.py. Kemudian, buka berkas file settings.py di direktori proyek pada IDE seperti vscode. Setelah itu, kita perlu mendaftarkan aplikasi main ke dalam proyek kita, yakni dengan menambahkan 'main' ke INSTALLED_APPS yang ada pada berkas file tersebut. Dengan demikian, kita telah membuat aplikasi main.

ck3 : Routing proyek dilakukan agar proyek terhubung dengan tampilan main sehingga aplikasi main dapat dijalankan. Pertama-tama buka berkas urls.py yang ada dalam direktori proyek pada IDE seperti vscode. Selanjutnya, kita perlu mengimport path dan include agar dapat mengambil URL aplikasi lain (main) ke dalam berkas urls.py yang ada dalam direktori proyek bukan direktori main. Kemudian, tambahkan path URL ('/main') agar rute mengarah ke berkas urls.py yang ada dalam direktori main. Dengan demikian, proyek kita dan aplikasi main telah terhubung.

ck4 : Pertama-tama buka berkas file models.py yang ada dalam direktori main (struktur awal aplikasi) pada IDE seperti vscode. Yang kedua, kita perlu mengimport models dari django.db. Setelah melakukan import, buat class dengan nama Item dan parameternya adalah models.Model. Kita dapat membuat atribut name, amount, description, dan lainnya dengan menggunakan parameter models tersebut serta menyesuaikan jenis/tipe dari atribut. Contohnya seperti amount dengan tipe atribut IntegerField.

ck5 : Pertama buka berkas file views.py yang ada dalam direktori main pada IDE seperti vscode. Kedua, kita perlu melakukan import render dari django.shortcuts agar dapat menggunakan render. Ketiga, buat fungsi seperti di python (menggunakan def dan parameter request) dengan isian seperti dictrionary (key-value) bernama context agar dapat dikembalikan ke dalam template HTML. Terakhir, kita perlu me-return isi fungsi menggunakan render. Render digunakan agar dapat mengisi template dengan data dinamis sebelum mengirimkan ke client sebagai respon.

ck6 : Routing pada aplikasi main dilakukan agar aplikasi tersebut dapat diakses di web. Pertama buka berkas file urls.py yang ada dalam direktori main (bukan proyek) pada IDE seperti vscode. Kedua, kita perlu melakukan import dari django.urls berupa path dan fungsi pada views.py, yakni show_main agar bisa digunakan. Ketiga, buat variabel app_name berisi nama aplikasi, yaitu main. Terakhir masukkan urlpattern atau path yang berkaitan dengan aplikasi main, seperti show_main.

ck7 : Pertama-tama buka web adaptable dan login menggunakan akun GitHub yang terhubung. Kemudian, pilih buat aplikasi baru dan isi syarat-syarat yang diperlukan, seperti nama aplikasi, repositori yang akan dihubungkan, versi python yang dipakai, tipe basis data yang akan digunakan, branch yang digunakan di GitHub, dan start command. Terakhir, lakukan proses deployment aplikasi.

ck8 : Buka direktori lokal proyek pada IDE seperti vscode. Kemudian buat file baru bernama README.md. Terakhir, isi berkas file tersebut dengan jawaban dari pertanyaan-pertanyaan pada tugas 2 PBP.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Gambar Bagan](https://github.com/nadinezhr/Tugas-2-PBP/blob/main/Bagantugas2PBP.jpeg)
    Penjelasan : client akan melakukan request melalui tampilan web (html), request tersebut akan masuk ke urls.py. urls.py akan meneruskan request tersebut ke views.py untuk diproses. Untuk memproses request, views.py akan mengakses data yang diperlukan di models.py, seperti membaca atau menulis data. Berkas html akan mengakses hasil request client pada views.py sebelum ditampilkan pada tampilan web.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab : Virtual environment memiliki beberapa manfaat dalam mengembangkan suatu perangkat lunak berbasis Python seperti web. Dengan basis Python, virtual environment akan menyesuaikan dan mengatur versi Python yang sesuai dengan proyek. Selain itu, virtual environment akan mengisolasi lingkungan proyek yang sedang dikerjakan agar tidak terjadi konflik dependensi (elemen,komponen,perangkat lunak lain) dengan proyek lain sehingga kebersihan sistem tetap terjaga. Virtual environment juga menyediakan paket Python ('pip') yang dapat digunakan untuk mengupgrade, menginstal, dan menghapus dependensi proyek. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, untuk lebih memudahkan pekerjaan serta menghindari konflik yang mungkin muncul jika tidak melakukan isolasi lingkungan proyek, sebaiknya kita selalu menggunakan virtual environtment dalam membangun aplikasi web berbasis Django agar proyek mudah dikelola, terorganisir, dan independen.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawab :
    1. MVC : Model-View-Controller (MVC) merupakan suatu pola desain yang membagi komponen yang saling berkaitan dalam pengerjaan proyek web menjadi 3 bagian, yakni model, view, dan controller. Tujuan dari pembagian tersebut adalah agar memudahkan programmer dalam memelihara kode, memodifikasi UI(tampilan), dan mengembangkan proyek. Model berhubungan dengan data dan logika yang digunakan sehingga model berperan dalam memodifikasi dan menambahkan data serta mengambil data dari database. Kemudian, view berhubungan dengan interface(tampilan) yang dilihat oleh pengguna sehingga berperan dalam menampilkan data ke pengguna. Terakhir adalah controller sebagai perantara model dan view. Controller berperan dalam memproses interaksi pengguna, kemudian memberitahu model, dan hasilnya akan ditampilkan oleh view.

    2. MVT : Model-View-Template (MVT) merupakan suatu pola desain yang membagi komponen yang saling berkaitan dalam pengerjaan proyek web menjadi 3 bagian, yakni model, view, dan template. Tujuan dari pembagian tersebut adalah untuk memisahkan presentasi, logika aplikasi, dan tampilan sehingga proyek mudah dipelihara, diuji, serta dikembangkan. Model berhubungan dengan struktur basis data Django sehingga berperan dalam menambahkan, menghapus, mengupdate, dan membaca database. Kemudian, view berhubungan dengan pemrosesan respon pengguna dan menggunakan model untuk menampilkan hasil respon. View seperti sebuah fungsi dalam Python. Yang terakhir adalah template yang berhubungan dengan tampilan halaman web dalam Django. Template menggabungkan data dari model ke HTML.

    3. MVVM : Model-View-ViewModel (MVVM) merupakan suatu pola desain yang membagi komponen yang saling berkaitan dalam pengerjaan proyek web menjadi 3 bagian, yakni model, view, dan viewmodel. Tujuan dari pembagian tersebut adalah untuk memudahkan programmer untuk melakukan testing terpisah, memelihara, dan mengembangkan kode. Model berhubungan dengan logika bisnis dan aplikasi salah satunya seperti pemrosesan dan penyimpanan data. Kemudian, view berhubungan dengan presentasi antarmuka seperti teks, tata letak, gambar, dan lainnya. Yang terakhir adalah viewmodel sebagai perantara model dan view. Viewmodel akan mengantarkan input pengguna dari view ke model untuk diproses dan mengantarkan output (hasil proses) dari model ke view. 

    Perbedaan MVC, MVT, dan MVVM :
    - Perbedaan utama terletak pada tugas controller, template, dan viewmodel. Controller bertanggung jawab untuk mengontrol aliran data antara Model dan View, serta mengatur interaksi pengguna. Controller mengambil peran mediator dalam MVC. Template bertanggung jawab untuk merender tampilan HTML dan menggabungkannya dengan data dari Model. Viewmodel bertanggung jawab untuk menghubungkan Model dengan View. ViewModel menyediakan abstraksi atas data yang akan ditampilkan di View, serta mengatur perubahan data agar sesuai dengan tampilan yang ada di View. 
    - Perbedaan MVC, MVT, dan MVVM juga terletak pada data binding (pengikatan data). MVC dan MVT tidak memiliki pengikatan data secara default sehingga memerlukan kode tambahan. Sementara itu, MVVM memiliki default pengikatan data sehingga memungkinkan model dan view terhubung secara otomatis.


REFERENSI :

3. https://revou.co/panduan-teknis/python-virtual-environment#:~:text=Salah%20satu%20manfaat%20utama%20penggunaan,mungkin%20berbeda%20dengan%20proyek%20lainnya.

4. - https://revou.co/kosakata/mvc#manfaat-mvc
   - https://www.educative.io/answers/what-is-mvt-structure-in-django
   - https://revou.co/kosakata/mvvm

