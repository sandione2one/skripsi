from django import forms
from django.forms import ModelForm
from django.forms.widgets import Select
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SiswaForm(ModelForm):
    class Meta:
        model = Siswa
        fields= '__all__'

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'npm': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'jenla': forms.Select(attrs={'class': 'form-control'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control'}),
            'bulan': forms.Select(attrs={'class': 'form-control'}),
            'tahun': forms.TextInput(attrs={'class': 'form-control'}),
            'asal': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'})

            }
        labels = {
            'user': 'NISN',
            'npm': 'Nomor Pendaftaran',
            'alamat': 'Tempat Tinggal',
            'jenla' : 'Jenis Kelamin',
            'tanggal' : 'Tanggal Lahir',
            'bulan' : 'Bulan ',
            'tahun' : 'Tahun  ',
            'asal': 'Asal Sekolah',
            'profile_pic': 'Foto',
        }

class OrtuForm(ModelForm):
    class Meta:
        model = Ortu
        fields= '__all__'

        widgets = {
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'namaay': forms.TextInput(attrs={'class': 'form-control'}),
            'nikay': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggalay': forms.TextInput(attrs={'class': 'form-control'}),
            'bulanay': forms.Select(attrs={'class': 'form-control'}),
            'tahunay': forms.TextInput(attrs={'class': 'form-control'}),
            'statusay': forms.Select(attrs={'class': 'form-control'}),
            'alamatay': forms.TextInput(attrs={'class': 'form-control'}),
            'pendidikanay': forms.Select(attrs={'class': 'form-control'}),
            'pendapatanay': forms.Select(attrs={'class': 'form-control'}),
            'nohpay': forms.TextInput(attrs={'class': 'form-control'}),

            'namaib': forms.TextInput(attrs={'class': 'form-control'}),
            'nikib': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggalib': forms.TextInput(attrs={'class': 'form-control'}),
            'bulanib': forms.Select(attrs={'class': 'form-control'}),
            'tahunib': forms.TextInput(attrs={'class': 'form-control'}),
            'statusib': forms.Select(attrs={'class': 'form-control'}),
            'alamatib': forms.TextInput(attrs={'class': 'form-control'}),
            'pendidikanib': forms.Select(attrs={'class': 'form-control'}),
            'pendapatanib': forms.Select(attrs={'class': 'form-control'}),
            'nohpib': forms.TextInput(attrs={'class': 'form-control'}),

            'namawal': forms.TextInput(attrs={'class': 'form-control'}),
            'nikwal': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggalwal': forms.TextInput(attrs={'class': 'form-control'}),
            'bulanwal': forms.Select(attrs={'class': 'form-control'}),
            'tahunwal': forms.TextInput(attrs={'class': 'form-control'}),
            'statuswal': forms.Select(attrs={'class': 'form-control'}),
            'alamatwal': forms.TextInput(attrs={'class': 'form-control'}),
            'pendidikanwal': forms.Select(attrs={'class': 'form-control'}),
            'pendapatanwal': forms.Select(attrs={'class': 'form-control'}),
            'nohpwal': forms.TextInput(attrs={'class': 'form-control'}),
            }
        labels = {
            'npm': 'Nomor Pendaftaran',
            'namaay': 'Nama',
            'nikay' : 'NIK',
            'tanggalay' : 'Tanggal Lahir',
            'bulanay' : 'Bulan ',
            'tahunay' : 'Tahun  ',
            'statusay' : 'Status',
            'alamatay' : 'Alamat ',
            'pendidikanay' : 'Pendidikan Terakhir  ',
            'pendapatanay': 'Pendapatan Perbulan',
            'nohpay': 'No. HP',

            'namaib': 'Nama',
            'nikib' : 'NIK',
            'tanggalib' : 'Tanggal Lahir',
            'bulanib' : 'Bulan ',
            'tahunib' : 'Tahun  ',
            'statusib' : 'Status',
            'alamatib' : 'Alamat ',
            'pendidikanib' : 'Pendidikan Terakhir  ',
            'pendapatanib': 'Pendapatan Perbulan',
            'nohpib': 'No. HP',

            'namawal': 'Nama',
            'nikwal' : 'NIK',
            'tanggalwal' : 'Tanggal Lahir',
            'bulanwal' : 'Bulan ',
            'tahunwal' : 'Tahun  ',
            'statuswal' : 'Status',
            'alamatwal' : 'Alamat ',
            'pendidikanwal' : 'Pendidikan Terakhir  ',
            'pendapatanwal': 'Pendapatan Perbulan',
            'nohpwal': 'No. HP',

        }
        
class DokuForm(ModelForm):
    class Meta:
        model = Dokumen
        fields= '__all__'

        widgets = {
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'ijazah': forms.FileInput(attrs={'class': 'form-control'}),
            'skl': forms.FileInput(attrs={'class': 'form-control'}),
            'kk': forms.FileInput(attrs={'class': 'form-control'})
            }
        labels = {
            'nama': 'Nama Lengkap',
            'ijazah': 'Tempat Tinggal',
            'skl' : 'Jenis Kelamin',
            'kk': 'Asal Sekolah',
        }
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'first_name', 'password1', 'password2']
        labels = {
            'username': 'NISN',
            'first_name': 'Nama Lengkap',
            'password1' : 'Password',
            'password2': 'Confirm Password',
        }

class PengForm(ModelForm):
    class Meta:
        model = Pengumuman
        fields= '__all__'

        widgets = {
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'pembayaran': forms.TextInput(attrs={'class': 'form-control'}),
            
            }
        labels = {
            'nama': 'Nama Lengkap',
            'status': 'Pengumuman',
            'pembayaran': 'Total Pembayaran',

            'lunas': 'Lunas',
        }
