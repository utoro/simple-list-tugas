from django.db import models
from django.conf import settings

class Tugas(models.Model):
    judul = models.CharField(max_length=50)
    mata_kuliah = models.CharField(max_length=50)
    deskripsi = models.TextField()

    INDIVIDU = 'IND'
    KELOMPOK = 'KLM'
    ch_jenis = (
        (INDIVIDU, 'Individu'),
        (KELOMPOK, 'Kelompok'),
    )
    jenis = models.CharField(
        max_length=3,
        choices=ch_jenis,
        default=INDIVIDU,
    )

    SUDAH = 'SDH'
    BELUM = 'BLM'
    ch_status = (
        (BELUM, 'Belum Dikerjakan'),
        (SUDAH, 'Sudah Dikerjakan'),
    )
    status = models.CharField(
        max_length=3,
        choices=ch_status,
        default=BELUM,
    )

    deadline = models.DateField(blank=False)
    pemilik = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return self.judul

    def snippet(self):
        return self.deskripsi[:50] + '...'
