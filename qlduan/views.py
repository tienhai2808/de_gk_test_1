from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import DuAnForm
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')

def dsnhanvien(request):
  nhieunhanvien = NhanVien.objects.all()
  return render(request, 'dsnhanvien.html', {'nhieunhanvien': nhieunhanvien})

def ctduan(request, idduan):
  du_an = get_object_or_404(DuAn, id=idduan)
  return render(request, 'ctduan.html', {'du_an': du_an})

def duan(request, idduan=None):
  if idduan:
    duan = get_object_or_404(DuAn, id=idduan)
    title = f'SỬA DỰ ÁN {duan.ten.upper()}'
    button = 'Sửa'
  else:
    duan = None
    title = 'TẠO DỰ ÁN'
    button = 'Tạo'
  form = DuAnForm(request.POST or None, instance=duan)
  if request.POST:
    if form.is_valid():
      duan_update = form.save()
      if idduan:
        messages.success(request, f'Chỉnh sửa {duan_update.ten} thành công')
      else:
        messages.success(request, f'Tạo mới dự án {duan_update.ten} thành công')
      return redirect('ctduan', duan_update.id)
  return render(request, 'duan.html', {'form': form, 'title': title, 'button': button})