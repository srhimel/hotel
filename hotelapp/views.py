from django.shortcuts import render

# Create your views here.
def gethome(request):
    return render(request, "home.html")
def getabout(request):
    return render(request, "about-us.html")
def getbestroom(request):
    return render(request, "best-rooms.html")
def getbestroomdetails(request):
    return render(request, "best-rooms-detail.html")
def getblog(request):
    return render(request, "blog.html")
def getblogdetails(request):
    return render(request, "blog-detail.html")
def getcontact(request):
    return render(request, "contacts.html")
def getfaq(request):
    return render(request, "faq.html")
def getgallery(request):
    return render(request, "gallery.html")
def getwizzars1(request):
    return render(request, "wizzard-step1.html")
def getwizzars2(request):
    return render(request, "wizzard-step2.html")
def getwizzars3(request):
    return render(request, "wizzard-step3.html")
def get404(request):
    return render(request, "404.html")
