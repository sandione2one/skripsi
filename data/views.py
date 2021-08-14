from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.views.generic import ListView
from io import BytesIO
from django.template.loader import get_template
from django.views import View



def pdflap(request):
    siswa = Siswa.objects.all()
    
    
    # grafik = Transaksi.objects.filter(periode=periode).annotate(total_masuk_count=Sum('pemasukan__pemasukan')).annotate(total_keluar_count=Sum('pengeluaran__pengeluaran'))
    # print (grafik)
    template_path = 'data/pdf_template.html'
    context = {'laporan': siswa}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf(request):
    siswa = Ortu.objects.all()
    
    
    # grafik = Transaksi.objects.filter(periode=periode).annotate(total_masuk_count=Sum('pemasukan__pemasukan')).annotate(total_keluar_count=Sum('pengeluaran__pengeluaran'))
    # print (grafik)
    template_path = 'data/pdf_temp.html'
    context = {'laporan': siswa}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="DataOrtu.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
@pilihan_login
def beranda(request):
    context = {
        'judul': 'Halaman Beranda',
    }
    return render(request, 'data/beranda.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def formsiswa(request):
    data = Siswa.objects.all()
    context ={
        "menu" : 'Form Karyawan',
        'siswa' : data
    }
    return render(request, 'data/formsiswa.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def formortu(request):
    data = Ortu.objects.all()
    context ={
        "menu" : 'Form Karyawan',
        'ortu' : data
    }
    return render(request, 'data/formortu.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def formdoku(request):
    data = Dokumen.objects.all()
    context ={
        "menu" : 'Form Karyawan',
        'doku' : data
    }
    return render(request, 'data/formdoku.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def pengum(request):
    data = Pengumuman.objects.all()
    context ={
        "menu" : 'Form Karyawan',
        'pengum' : data
    }
    return render(request, 'data/pengum.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def bayar(request):
    data = Pengumuman.objects.all()
    context ={
        "menu" : 'Form Karyawan',
        'doku' : data
    }
    return render(request, 'data/bayar.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def inputsiswa(request):
    form = SiswaForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = SiswaForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('formsiswa')
    
    context = {
        'judul': 'Halaman Beranda',
        "formsis" : form 
    }
    return render(request, 'data/inputsiswa.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def updatesiswa(request, pk):
    siswa = Siswa.objects.get(id=pk)
    formsis = SiswaForm(instance=siswa)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = SiswaForm(request.POST, instance=siswa)
        if formedit.is_valid:
            formedit.save()
            return redirect('formsiswa')
    context = {
        'judul': 'Edit Order',
        'form' : formsis,
    } 
    return render(request, 'data/update_siswa.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def deletesiswa(request, pk):
    orderhapus = Siswa.objects.get(id=pk)
    if request.method == 'POST':
        orderhapus.delete()
        return redirect('formsiswa')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete' : orderhapus, 
    }
    return render(request, 'data/deletesiswa.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def dataortu(request):
    form = OrtuForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = OrtuForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('formortu')

    context = {
        'judul': 'Halaman Beranda',
        "form" : form,
    }
    return render(request, 'data/dataortu.html ', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def updateortu(request, pk):
    ortu = Ortu.objects.get(id=pk)
    formortu = OrtuForm(instance=ortu)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = OrtuForm(request.POST, instance=ortu)
        if formedit.is_valid:
            formedit.save()
            return redirect('formortu')
    context = {
        'judul': 'Edit Order',
        'form' : formortu,
    } 
    return render(request, 'data/updateortu.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def deleteortu(request, pk):
    hapus = Ortu.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('formortu')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete' : hapus, 
    }
    return render(request, 'data/deleteortu.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def datadoku(request):
    form = DokuForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = DokuForm(request.POST, request.FILES)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('formdoku')

    context = {
        'judul': 'Halaman Beranda',
        "form" : form,
    }
    return render(request, 'data/datadoku.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def updatedoku(request, pk):
    doku = Dokumen.objects.get(id=pk)
    formdoku = DokuForm(instance=doku)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = DokuForm(request.POST, request.FILES, instance=doku)
        if formedit.is_valid:
            formedit.save()
            return redirect('formdoku')
    context = {
        'judul': 'Edit Order',
        'form' : formdoku,
    } 
    return render(request, 'data/updatedoku.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def deletedoku(request, pk):
    hapus = Dokumen.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('formdoku')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete' : hapus, 
    }
    return render(request, 'data/deletedoku.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def inputpengumuman(request):
    form = PengForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = PengForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pengum')
    
    context = {
        'judul': 'Halaman Beranda',
        "formsis" : form 
    }
    return render(request, 'data/inputpengumuman.html', context)

login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def updatepengumuman(request, pk):
    pengum = Pengumuman.objects.get(id=pk)
    formsis = PengForm(instance=pengum)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = PengForm(request.POST, instance=pengum)
        if formedit.is_valid:
            formedit.save()
            return redirect('pengum')
    context = {
        'judul': 'Edit Order',
        'form' : formsis,
    } 
    return render(request, 'data/updatepengumuman.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def deletepengumuman(request, pk):
    hapus = Pengumuman.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('pengum')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete' : hapus, 
    }
    return render(request, 'data/deletepengumuman.html', context)

@tolakhalaman_ini
def loginPage(request): 
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')
    context = {
        'menu': 'Halaman Login',
        'tampillogin' : formlogin
    }
    return render(request, 'data/login.html', context)

@tolakhalaman_ini
def register(request):
    formregister = RegisterForm()
    if request.method == 'POST':
        formregister = RegisterForm(request.POST)
        if formregister.is_valid():
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername} ')
            group_siswa = formregister.save()
            grup = Group.objects.get(name='siswa')
            group_siswa.groups.add(grup)
            Siswa.objects.create(
                user=group_siswa,
                nama=group_siswa.first_name)
            return redirect('login')

    context = {
        'judul': 'Halaman Register',
        'menu': 'register',
        'tampilregister' : formregister
    }
    return render(request, 'data/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def homePage(request):
    context = {
        'judul': 'Halaman Beranda',
        
    }
    return render(request, 'data/siswa/home.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def isidatasiswa(request):
    datacustumer = request.user.siswa
    form = SiswaForm (instance = datacustumer)
    if request.method == 'POST':
        form = SiswaForm(request.POST, request.FILES, instance=datacustumer)
        if form.is_valid:
            form.save()
            return redirect('home') 
    context = {
        'menu': 'settings',
        'formcustumer': form
    }
    return render(request, 'data/siswa/isidatasiswa.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def inputortu(request):
    form = OrtuForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = OrtuForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('home')
    
    context = {
        'judul': 'Halaman Beranda',
        "form" : form 
    }
    return render(request, 'data/siswa/inputortu.html ', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def uploaddoku(request):
    form = DokuForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = DokuForm(request.POST, request.FILES)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('home')

    context = {
        'judul': 'Halaman Beranda',
        "form" : form,
    }
    return render(request, 'data/siswa/uploaddoku.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def data(request):
    context = {
        'judul': 'Halaman Beranda',
        
    }
    return render(request, 'data/siswa/data.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def pengumuman(request):
    # jumlah = SppItem.objects.values('spp__spp').annotate(sppsiswa__lunas_count=Sum('spp__spp', filter=Q(sppsiswa__lunas=True)), not_sppsiswa__lunas_count=Sum('spp__spp', filter=Q(sppsiswa__lunas=False)))
    siswa = request.user.siswa
    pengumuman = Pengumuman.objects.get(nama=siswa)
    context = {
        'judul': 'Halaman Beranda',
        'pengumuman': pengumuman,
        
    }
    return render(request, 'data/siswa/pengumuman.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def pembayaran(request):
    # jumlah = SppItem.objects.values('spp__spp').annotate(sppsiswa__lunas_count=Sum('spp__spp', filter=Q(sppsiswa__lunas=True)), not_sppsiswa__lunas_count=Sum('spp__spp', filter=Q(sppsiswa__lunas=False)))
    siswa = request.user.siswa
    pembayaran = Pengumuman.objects.get(nama=siswa)
    context = {
        'judul': 'Halaman Beranda',
        'pembayaran': pembayaran,
        
    }
    return render(request, 'data/siswa/pembayaran.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['siswa'])
def profile(request):
    datacustumer = request.user.siswa
    form = SiswaForm (instance = datacustumer)
    if request.method == 'POST':
        form = SiswaForm(request.POST, request.FILES, instance=datacustumer)
        if form.is_valid:
            form.save()
            return redirect('home') 
    context = {
        'menu': 'settings',
        'formcustumer': form
    }
    return render(request, 'data/siswa/profile.html', context)