from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']
        
        if sifre1 == sifre2:
            if User.objects.filter(username = kullanici).exists(): # böyle bir kullanıcı var ise
                messages.error(request,'Kullanıcı adı zaten alınmış')
                return redirect('register')
            elif User.objects.filter(email  = email).exists():
                messages.error(request,'Email Kullanımda')
                return redirect('register')
            elif len(sifre1) < 6:
                messages.error(request,'Şifre en az  6 karakterden oluşmalıdır')
                return redirect('register')
            elif kullanici in sifre1:
                messages.error(request,'Kullanıcı Adı Şifre Benzer Olamaz')
                return redirect ('register')
            else:
                #Hata yoksa kullanıcıyı oluşturur
                user = User.objects.create_user(username = kullanici,email = email,password = sifre1)
                subject = 'Exxen'
                message = 'Bu Exxen Projesini Kasım Doğruyol Yaptı İncelediğiniz İçin Teşekkürler'
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
                user.save()
                messages.success(request,'Kullanıcı Başarı İle Oluşturuldu')
                return redirect('login')
        else:
            messages.error(request,'Şifre Hatalı')
            return redirect('register')
    return render(request,'register.html')
def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']               
        sifre = request.POST['sifre']

        user = authenticate(request,username = kullanici,password = sifre)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Kullanıcı Girişi Yapıldı')
            return redirect('index')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request,'login.html')
def userLogout(request):
    logout(request)
    messages.success(request,'Çıkış Yapıldı')
    return redirect('index')
                