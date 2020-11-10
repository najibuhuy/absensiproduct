from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product


# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == "POST": #klo dia udah klik 
# 		my_form = RawProductForm(request.POST) #periksa di class RawProductForm
# 		if my_form.is_valid(): #klo udah bener (ga kosong) klo di class RawProductForm memang required=True
# 			#ada datanya
# 			print(my_form.cleaned_data) #print data yg masuk akan berupa tipe data dict
# 			Product.objects.create(**my_form.cleaned_data) #save the data to product
# 		else:
# 			print(my_form.errors)
# 	context ={
# 	"form" : my_form
# 	}

# def product_create_view(request):
# 	#print(request.GET)
# 	#print(request.POST)
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 	#Product.objects.create(title=my_new_title)
# 	context ={}

# Create your views here.
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
	'form': form
	}

	return render(request,"product/product_create_view.html",context)

# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
	'Nama': obj.Nama,
	'NoIdentitas': obj.NoIdentitas,
	'NIK': obj.NIK
	}
	return render(request,"product/detail.html",context)


def render_initial_view(request):
	initial_data = {
	'Nama': "my awesome name"
	}
	obj = Product.objects.get(id=1) 
	form = ProductForm(request.POST or None, instance=obj) 
	if form.is_valid():
		form.save()
	context = {
	'form' : form
	}
	return render(request,"product/editproduct.html",context)

# def get_product_search(request,my_search):
#     obj=Product.objects.search(title=my_search)
# 	context = {
# 	'title': obj.title,
# 	}
# 	return render(request,"product/product_search.html", context)


def dynamic_lookup_view(request,my_id):
	#obj = Product.objects.get(id=my_id) 
	obj = get_object_or_404(Product,id=my_id)
	obj = Product.objects.get(id=my_id)
	try:
		obj = Product.objects.get(id=my_id)
	except Product.DoesNotExist:
		raise Http404
	context = {
	'Nama': obj.Nama,
	'NoIdentitas': obj.NoIdentitas,
	'NIK': obj.NIK
	}
	return render(request, "product/detail.html", context)

def product_delete(request,my_id):
	obj = get_object_or_404(Product,id=my_id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
	'object': obj
	}
	return render(request, "product/product_delete_view.html", context)

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
	"object_list":queryset
	}
	return render(request, "product/product_list.html", context)

