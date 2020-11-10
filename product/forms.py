from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	Nama 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
	email 		= forms.EmailField()
	# NoIdentitas = forms.CharField(required=False, 
	# 							  widget=forms.Textarea(
	# 							  	attrs={
	# 							  	"placeholder":"Your description",
	# 							  	"class": "new-class-name two",
	# 							  	"id":"my-id-for-textarea",
	# 							  	"rows": 5,
	# 							  	"cols": 5
	# 							  	}
	# 							  	)
	# 							  )
	NoIdentitas	 = forms.CharField(required=True,max_length=6)
	NIK 		 = forms.DecimalField(initial=999999)
	Password	 = forms.CharField(required=True,max_length=20)
	Telepon		 = forms.CharField(required=True,max_length=12)
	class Meta: 
		model = Product
		fields = [ 'Nama', 'NoIdentitas','NIK','email', 'Password', 'Telepon']

	def clean_email(self,*args,**kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			return email
		else:
			raise forms.ValidationError("Bukan Email yang valid")

	def clean_NoIdentitas(self,*args,**kwargs):
		NoIdentitas = self.cleaned_data.get("NoIdentitas")
		if not NoIdentitas.isdigit()==False:
			return NoIdentitas
		else:
			raise forms.ValidationError("Bukan ID Number yang valid")




class RawProductForm(forms.Form):
	Nama 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
	# NoIdentitas = forms.CharField(required=False, 
	# 							  widget=forms.Textarea(
	# 							  	attrs={
	# 							  	"placeholder":"Your description",
	# 							  	"class": "new-class-name two",
	# 							  	"id":"my-id-for-textarea",
	# 							  	"rows": 5,
	# 							  	"cols": 5
	# 							  	}
	# 							  	)
	# 							  )
	NoIdentitas	 = forms.CharField(max_length=120)
	NIK 		 = forms.DecimalField(initial=999999)
	Password	 = forms.CharField(max_length=20)
	Telepon		 = forms.CharField(max_length=12)