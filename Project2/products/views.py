 
from django.contrib import messages
from django.shortcuts import redirect, render ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from products.forms import CategoryForm,ProductForm
from .models import Cart,  Product , Category
from django.views.generic import ListView , DetailView ,CreateView,UpdateView

def Home_page(request):
    if request.user.is_active:
        return render (request ,  'home.html')
    return render (request,'home.html')
#class based view
class AllProductsView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context["products"]:
            context["error_message"] = "No products"
        return context


class HomePageView(ListView):
    
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_info.html"
    context_object_name = "product"
       


class AllCategoriesView(ListView):
    model = Category
    template_name = "products/category.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context["categories"]:
            context["error_message"] = "No Categories"
        return context


class CategoryProductsView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        category = get_object_or_404(Category, id=category_id)
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = get_object_or_404(Category, id=category_id)
        return context
 

class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "products/forms/form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("all_categ")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Add New Category"
        return context

    def form_valid(self, form):
        return super().form_valid(form)
class EditCategoryView(LoginRequiredMixin,UpdateView):
    model = Category
    template_name = "products/forms/form.html"
    extra_context = {"form_title": "EditCategory"}
    form_class =CategoryForm
    def get_success_url(self):
        return reverse("edit_category", kwargs={"pk": self.object.pk})

class AddProductView(LoginRequiredMixin,CreateView):
    model = Product
    template_name="products/forms/form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")  
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["form_title"] = "Add New Product"
        return context
    def form_valid(self, form):
        return super().form_valid(form)   
    
class EditProductView(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = "products/forms/form.html"
    extra_context={"form_title": "EditProduct"}
    form_class = ProductForm
    success_url = reverse_lazy ("all_products")

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs["pk"])

    def get_success_url(self):
        return reverse("one_product", kwargs={"pk": self.object.pk})

class DeleteProductView(DetailView):
    model= Product
    success_url = reverse_lazy("all_products")
    def post(self, request, *args, **kwargs):
        """Override post method to allow deletion"""
        product = get_object_or_404(Product, pk=self.kwargs["pk"])
        product.delete()
        return HttpResponseRedirect(self.success_url)

 
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
 
  
    return redirect("cart_detail")
 

def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)
    cart_item.delete()
    return redirect('cart_detail')


def cart_detail(request):
    if request.user.is_authenticated:
        # Fetch cart items for the logged-in user
        cart_items = Cart.objects.filter(user=request.user).select_related('product')
    else:
        # If the user is not authenticated, return an empty list
        cart_items = []
    return render(request, 'cart.html', {'cart_items': cart_items})