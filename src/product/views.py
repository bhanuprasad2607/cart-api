from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from .forms import ProductForm


# restframework imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, CartSerializer

# View Products


def productPage(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product/products.html', context)

# add Products


def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')

    context = {
        'form': form
    }
    return render(request, 'product/create-product.html', context)


def updateProduct(request, id):
    obj = get_object_or_404(Product, product_id=id)
    form = ProductForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'product/create-product.html', context)

# Delete Products


def deleteProduct(request, id):
    product = Product.objects.filter(product_id=id).get()
    product.delete()
    return redirect('list_products')

# View Cart add Products


def cartPage(request):
    cart = Cart.objects.all()
    context = {
        'cart': cart,
    }
    return render(request, 'product/cart.html', context)

# Add a Product to cart


def addCart(request, id):
    product = Product.objects.get(product_id=id)
    if not Cart.objects.filter(product_id=product).exists():
        cart = Cart(product_id=product)
        cart.save()
    return redirect('list_cart')

# delete a Product from the cart


def delProductCart(request, id):
    cart = Cart.objects.filter(cart_id=id).get()
    cart.delete()
    return redirect('list_cart')


# rest Framework
@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_view(request, id):
    if Product.objects.filter(product_id=id).exists():
        product = Product.objects.filter(product_id=id)
        if request.method == 'GET':
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def cartApi(request):
    if request.method == 'GET':
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
