from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Siswa)
admin.site.register(Ortu)
admin.site.register(Dokumen)
admin.site.register(Pengumuman)