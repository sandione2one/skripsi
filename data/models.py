from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Siswa(models.Model):
    start = (
        ('Diterima', 'Diterima'),
        ('Ditolak', 'Ditolak'),
    )
    Kelamin = (
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    )
    bln = (
        ('Januari', 'Januari'),('Februari', 'Februari'),('Maret', 'Maret'),('April', 'April'),('Mei', 'Mei'),('Juni', 'Juni'),
        ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), 
        ('Desember', 'Desember'),
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    jenla = models.CharField(max_length=200, blank=True, null=True, choices=Kelamin)
    tanggal = models.CharField(max_length=200, blank=True, null=True)
    bulan = models.CharField(max_length=200, blank=True, null=True, choices=bln)
    tahun =  models.CharField(max_length=200, blank=True, null=True,)
    asal = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(default='fotokosong.gif', blank=True)

    def __str__(self):
        return self.nama
    
def save(self, *args, **kwargs):
    super(Siswa, self).save(*args, **kwargs)
    img = Image.open(self.profile_pic.path)
    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.profile_pic.path)

class Ortu(models.Model):
    pendapatan = (
        ('0 - 500.000', '0 - 500.000'),
        ('500.000 - 1.000.000', '500.000 - 1.000.000'),
        ('1.000.000 - 3.000.000', '1.000.000 - 3.000.000'),
        ('3.000.000 - 5.000.000', '3.000.000 - 5.000.000'),
        ('5.000.000 - 10.000.000', '5.000.000 - 10.000.000'),
        ('10.000.000 ++', '10.000.000 ++'),
    )
    pendidik = (
        ('Tidak Sekolah', 'Tidak Sekolah'),
        ('SD/MI', 'SD/MI'),
        ('SMP/MTS', 'SMP/MTS'),
        ('SMA/MA/SMK', 'SMA/MA/SMK'),
        ('Diploma', 'Diploma'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
    )
    statu = (
        ('Masih Hidup', 'Masih Hidup'),
        ('Meninggal Dunia', 'Meninggal Dunia'),
    )
    buln = (
        ('Januari', 'Januari'),('Februari', 'Februari'),('Maret', 'Maret'),('April', 'April'),('Mei', 'Mei'),('Juni', 'Juni'),
        ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), 
        ('Desember', 'Desember'),
    )
    nama = models.ForeignKey(Siswa, null=True, on_delete=models.SET_NULL)
    namaay = models.CharField(max_length=200, blank=True, null=True)
    nikay = models.CharField(max_length=200, blank=True, null=True)
    tanggalay = models.CharField(max_length=200, blank=True, null=True)
    bulanay = models.CharField(max_length=200, blank=True, null=True, choices=buln)
    tahunay =  models.CharField(max_length=200, blank=True, null=True,)
    statusay = models.CharField(max_length=200, blank=True, null=True, choices=statu)
    alamatay = models.CharField(max_length=200, blank=True, null=True)
    pendidikanay = models.CharField(max_length=200, blank=True, null=True, choices=pendidik)
    pendapatanay = models.CharField(max_length=200, blank=True, null=True, choices=pendapatan)
    nohpay = models.CharField(max_length=200, blank=True, null=True)

    namaib = models.CharField(max_length=200, blank=True, null=True)
    nikib = models.CharField(max_length=200, blank=True, null=True)
    tanggalib = models.CharField(max_length=200, blank=True, null=True)
    bulanib = models.CharField(max_length=200, blank=True, null=True, choices=buln)
    tahunib =  models.CharField(max_length=200, blank=True, null=True,)
    statusib = models.CharField(max_length=200, blank=True, null=True, choices=statu)
    alamatib = models.CharField(max_length=200, blank=True, null=True)
    pendidikanib = models.CharField(max_length=200, blank=True, null=True, choices=pendidik)
    pendapatanib = models.CharField(max_length=200, blank=True, null=True, choices=pendapatan)
    nohpib = models.CharField(max_length=200, blank=True, null=True)

    namawal = models.CharField(max_length=200, blank=True, null=True)
    nikwal = models.CharField(max_length=200, blank=True, null=True)
    tanggalwal = models.CharField(max_length=200, blank=True, null=True)
    bulanwal = models.CharField(max_length=200, blank=True, null=True, choices=buln)
    tahunwal =  models.CharField(max_length=200, blank=True, null=True,)
    statuswal = models.CharField(max_length=200, blank=True, null=True, choices=statu)
    alamatwal = models.CharField(max_length=200, blank=True, null=True)
    pendidikanwal = models.CharField(max_length=200, blank=True, null=True, choices=pendidik)
    pendapatanwal = models.CharField(max_length=200, blank=True, null=True, choices=pendapatan)
    nohpwal = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.namaay

class Dokumen(models.Model):
    
    nama = models.ForeignKey(Siswa, null=True, on_delete=models.SET_NULL)
    ijazah = models.ImageField(blank=True, null=True)
    skl = models.ImageField(blank=True, null=True)
    kk = models.ImageField(blank=True, null=True)


def save(self):
    super().save()
    img = Image.open(self.document.path)
    if img.height > 10 or img.width > 10:
        output_size = (10, 10)
        img.thumbnail(output_size)
        img.save(self.document.path)

class Pengumuman(models.Model):
    
    nama = models.ForeignKey(Siswa, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=False)
    pembayaran = models.CharField(max_length=200, default="0")
    lunas = models.BooleanField(default=False)