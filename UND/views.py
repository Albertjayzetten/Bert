from django.shortcuts import render, redirect, get_object_or_404
from .models import Clothing, ClothingImage
from .forms import ClothingForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def clothing(request):
    clothing = Clothing.objects.all()
    return render(request, 'pages/clothing.html', {'clothing': clothing})

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def admin_clothing(request):
    clothing = Clothing.objects.all()
    return render(request, 'pages/admin/clothing.html', {'clothing': clothing})


def admin_clothing_add(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            clothing = form.save()
            handle_image_uploads(request, clothing)
            return redirect('clothing_list')
    else:
        form = ClothingForm()

    return render(request, 'pages/admin/add-clothing.html', {'form': form})


def admin_clothing_edit(request, clothing_id):
    clothing = get_object_or_404(Clothing, pk=clothing_id)

    if request.method == 'POST':
        form = ClothingForm(request.POST, instance=clothing)
        if form.is_valid():
            clothing = form.save()
            handle_image_uploads(request, clothing)
            return redirect('clothing_edit', clothing_id=clothing.id)
    else:
        form = ClothingForm(instance=clothing)

    return render(request, 'pages/admin/edit-clothing.html', {'form': form, 'clothing': clothing})

def admin_clothing_delete(request, id):
    return render(request, 'pages/admin/clothing_delete.html')

def handle_image_uploads(request, clothing):
    for image_file in request.FILES.getlist('images'):
        ClothingImage.objects.create(clothing=clothing, image=image_file)

def admin_clothing_delete(request, clothing_id):
    clothing = get_object_or_404(Clothing, pk=clothing_id)
    clothing.delete()
    return redirect('clothing_list')

def admin_clothing_image_delete(request, clothing_id, image_id):
    clothing = get_object_or_404(Clothing, pk=clothing_id)
    image = get_object_or_404(ClothingImage, pk=image_id)
    image.delete()
    return redirect('clothing_edit', clothing_id=clothing_id)
