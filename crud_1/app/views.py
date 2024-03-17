from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages

# Create your views here.

def create(request):
    cpo = ProductForm()
    if request.method == 'POST':
        cpdo = ProductForm(request.POST,request.FILES)
        
        if cpdo.is_valid():
            cpdo.save()
    d = {'cpo':cpo}
    return render(request, 'create.html',d)

def retrive(request):
    pro = Product.objects.all()
    d = {'pro' : pro}
    return render(request, 'retrive.html', d)

def update(request, id):
    puo = Product.objects.get(pro_id = id)
    ufo = ProductForm(instance = puo)
    if request.method == 'POST':
        puo.pro_id = request.POST['pro_id']
        puo.pro_name = request.POST['pro_name']
        puo.pro_price = request.POST['pro_price']
        puo.pro_desc = request.POST['pro_desc']
        if request.FILES :
            puo.pro_img = request.FILES['pro_img']
        puo.save()
        messages.info(request, 'product edited successfully !!')
        return redirect('/retrive')

    d = {'ufo' : ufo}
    return render(request, 'update.html',d)

def delete(request,id):
    Product.objects.filter(pro_id = id).delete()
    messages.info(request, 'product deleted successfully !!')
    return redirect('/retrive')


#  Product.objects.all() 
# QuerySet [<Product: pencil>, <Product: neon pen>, <Product: pen>, <Product: pen>, <Product: pens>]>
#  Product.objects.values('pro_id')
# QuerySet [{'pro_id': 101}, {'pro_id': 102}, {'pro_id': 103}, {'pro_id': 104}, {'pro_id': 105}]>
#  Product.objects.values('pro_id','pro_name')
# QuerySet [{'pro_id': 101, 'pro_name': 'pencil'}, {'pro_id': 102, 'pro_name': 'neon pen'}, {'pro_id': 103, 'pro_name': 'pen'}, {'pro_id': 104, 'pro_name': 'pen'}, {'pro_id': 105, 'pro_name': 'pens'}]>
#  Product.objects.values_list('pro_id','pro_name')
# QuerySet [(101, 'pencil'), (102, 'neon pen'), (103, 'pen'), (104, 'pen'), (105, 'pens')]>


def product(request):
    obj=Product(pro_id = 500, pro_name = 'pensil', pro_price = 20, pro_desc = 'nuchjsi mjzwe',pro_img)