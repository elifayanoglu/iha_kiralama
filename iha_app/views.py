from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Iha
from django.contrib.auth.models import User
from datetime import *
from django.utils import timezone

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Kiralama



# Create your views here.

def index(request):
    ihas = Iha.objects
    return render(request, 'iha_app/index.html', {'ihas':ihas})

def profil(request):
     iha_ekle = Iha.objects
     kiralamalar = Kiralama.objects.filter(kullanici_ismi=request.user.username)
     return render(request, 'iha_app/profil.html',{"iha_ekle": iha_ekle, "kiralamalar": kiralamalar})


def kiraliste(request):
    if request.user.is_authenticated:
        ihas = Iha.objects
        kiralar= Kiralama.objects
    else:
        return render('iha_app/giris.html')

    return render(request, 'iha_app/kiraliste.html', {'ihas':ihas, 'kiralar':kiralar})




def kirala(request, iha_id):
    print("kiralanın içindeyim")
 #   if request.method == "POST":
    iha_kiralanan = get_object_or_404(Iha, pk=iha_id)
    
    if request.user.is_authenticated:
        kullanici_ismi = request.user.username
        tarih = timezone.now()
        
        kiralama = Kiralama(kullanici_ismi=kullanici_ismi, tarih=tarih, iha_kiralanan=iha_kiralanan)
        kiralama.save()
        
        return HttpResponse("Kirala işlemi tamamlandı")
    else:
        return render(request, 'iha_app/giris.html')
    
    return render(request, 'iha_app/profil.html')
 
 
def detail(request, iha_id):
    iha_detail = get_object_or_404(Iha, pk=iha_id)
    return render(request, 'iha_app/detail.html',{'iha_detail':iha_detail})

def giris(request):
    if request.method == 'POST':
        username = request.POST['kullanici']
        password = request.POST['sifre']

        user = authenticate(request, username = username , password = password)

        if user is not None:
            login(request , user)
            messages.success(request , 'Giriş Yapıldı')
            return redirect('profil')
        else:
            messages.error(request , 'Kullanıcı adınız veya şifreniz hatalı')
            return redirect('giris')
    return render(request, 'iha_app/giris.html')

def kayit(request):
    
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        isim = request.POST['isim']
        soyisim = request.POST['soyisim']
        sifre1 = request.POST['sifre1']
        sifre2=request.POST['sifre2']

        if sifre1 == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request , 'Başka bir kullanıcı adı seçiniz.')
                return redirect('kayit')
            

            elif User.objects.filter(email = email).exists():
                messages.error(request , 'Bu mail adresi sistemimizde mevcut. Lütfen başka bir mail adresi giriniz.')
                return redirect('kayit')
            
            elif len(sifre1) < 6 :
                messages.error(request , 'Şifre en az 6 karakter olmalıdır')
                return redirect('kayit')
            
            else:
                user = User.objects.create_user(
                    username= kullanici , email=email , password= sifre1
                )
                profil.objects.create(
                    kullanici = user ,
                    isim = isim ,
                    soyisim = soyisim
                )
                user.save()
                messages.success(request , 'Kayıt başarılı')
                return redirect('giris')
        else:
            messages.error(request , 'Şifreniz doğrulanamadı. Lütfen tekrar deneyiniz.')
            return redirect('kayit')
    return render(request, 'iha_app/kayit.html')



def cikis(request):
    cikis(request)
    return redirect ('index')