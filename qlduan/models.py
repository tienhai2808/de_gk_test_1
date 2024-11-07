from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DuAn(models.Model):
  ten = models.CharField(max_length=200)
  ngay_bat_dau = models.DateField()
  ngay_ket_thuc = models.DateField()
  mo_ta = models.TextField()
  quy_mo = models.CharField(max_length=30, choices=[('Nhỏ', 'Nhỏ'), ('Vừa', 'Vừa'), ('Lớn', 'Lớn')], default='Nhỏ')
  
  def __str__(self):
    return f'{self.ten} - {self.quy_mo}'


class NhanVien(models.Model):
  ho_ten = models.CharField(max_length=250)
  ngay_sinh = models.DateField()
  so_dien_thoai = models.CharField(max_length=11)
  gioi_thieu = models.TextField(blank=True)
  tai_khoan = models.OneToOneField(User, on_delete=models.CASCADE)
  du_an = models.ManyToManyField(DuAn, through='NhanVienDuAn')
  
  def __str__(self):
    return f'{self.tai_khoan} - {self.ho_ten}'
  

class NhanVienDuAn(models.Model):
  nhan_vien = models.ForeignKey(NhanVien, on_delete=models.CASCADE, related_name='nhieuduan')  #nhanvien.nhanvienduan_set.all  #nhanvien.nhieuduan.all
  du_an = models.ForeignKey(DuAn, on_delete=models.CASCADE, related_name='nhieunhanvien') #duan.nhanvienduan_set.all  #duan.nhieuduan.all