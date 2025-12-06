from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def index(request):
    DTBanner = Image.objects.filter(ImageTypeID=1)
    DTSlideshow = Image.objects.filter(ImageTypeID = 2)
    DTSidebarleft = Image.objects.filter(ImageTypeID = 3)
    DTSidebarRight = Image.objects.filter(ImageTypeID = 4)
    DTFooter = Image.objects.filter(ImageTypeID = 5)
    DTLogo = Image.objects.filter(ImageTypeID = 6)
    
    usinget = Image.objects.get(id=1)
    UseExclude = Image.objects.exclude(ImageTypeID=5)
    UseOrderByASC = Image.objects.order_by("id")
    UseOrderByDSCE = Image.objects.order_by("-id")
    UseFirst = Image.objects.first()
    UseLast = Image.objects.last()
    Usecount = Image.objects.count()
    UseExits = Image.objects.filter(id=500).exists()
    

    UnitPrice = 5000
    Quantity = 10
    Totalprice = UnitPrice * Quantity
    AUB = "Acleda University of Business"
    Dayty = [1,2,3,4,5,6,7,8,9,10]
    Days = ["ចន្ទ","អង្គារ","ពុធ","ព្រហ","សុក្រ","សៅរ៍","អាទិត្យ"]
    Months = ["Jan","Feb","March","April","May","June","July","August","Sep","Oct","Nov","Dec"]
    Years = [2025,2026,2027,2028,2029,2030]
    Name = "Soanr"   
    context = {
        'ObjTotalprice':Totalprice,
        'ObjAUB':AUB,
        'ObjDayty':Dayty,
        'ObjDays':Days,
        'ObjMonths':Months,
        'ObjYears':Years ,
        'Objname':Name,   
        'ObjBanner':DTBanner,
        'ObjSlideshow':DTSlideshow,
        'ObjSlidebarleft':DTSidebarleft,
        'ObjSlidebarright':DTSidebarRight,
        'ObjFooter':DTFooter,
        'ObjLogo':DTLogo,
        'Objusingget':usinget,
        'ObjuseExclude':UseExclude,
        'ObjUseOrderByASC':UseOrderByASC,
        'ObjUseOrderByDSCE':UseOrderByDSCE,
        'ObjUseFirst':UseFirst,
        'ObjUseLast':UseLast,
        'ObjUsecount':Usecount,
        'ObjUseExits':UseExits


    }
    return render(request, 'accounts/index.html', context)
def Contactus(request):
    return render(request,'accounts/contactus.html')
def aboutus(request):
    return render(request,'accounts/aboutus.html')
def login(request):
    return render(request,'accounts/login.html')
# def Product(request):
#     return render(request,'accounts/Product.html')
def Promotion(request):
    return render(request,'accounts/Promotion.html')

# Ogani
def OganiIndex(request):
    DTProduct = Product.objects.all()
    DTCategory = Category.objects.all
    context = {
        'ObjDTProduct':DTProduct,
        'ObjDTCategory':DTCategory,
    }
    return render(request, 'Ogani/index.html',context)
def OganiBlogDetails(request):
    return render(request,'Ogani/blog-details.html')
def Blog(request):
    return render(request,'Ogani/blog.html')
def CheckOut(request):
    return render(request,'Ogani/checkout.html')
def Contact(request):
    return render(request,'Ogani/contact.html')

def ShopDetails(request,pk):
    DTproducts = Product.objects.get(id = pk) #Only 1 No Loop
    DTProductDetail = ProductDetail.objects.get(productID=pk)
    DTProductDetailImage = ProductDetailImage.objects.filter(productID = pk)
    context = {
    'ObjDTproducts':DTproducts,
    'ObjDTProductDetail':DTProductDetail,
    'ObjDTProductDetailImage':DTProductDetailImage
    }
    return render(request,'Ogani/shop-details.html',context)

def ShopingCart(request):
    return render(request,'Ogani/shoping-cart.html')
def OganiShopGrid(request):
    return render(request, 'Ogani/shop-grid.html')


#==========================================
def create_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'Ogani/create_book.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Ogani/book_list.html', {'books': books})

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('book_list')
    return render(request, 'Ogani/update_book.html', {'book': book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'Ogani/delete_book.html', {'book': book})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the list view
    else:
        form = ItemForm()
    return render(request, 'Ogani/create_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'Ogani/item_list.html', {'items': items})



def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('item_list')  # Redirect to the list view
    else:
        form = ItemForm()
    return render(request, 'Ogani/create_item.html', {'ProductForm': ProductForm})


def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the list view
    else:
        form = ItemForm(instance=item)
    return render(request, 'Ogani/update_item.html', {'form': form, 'item': item})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')  # Redirect to the list view after deletion
    return render(request, 'Ogani/delete_item.html', {'item': item})


# Continue Ongani
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        cart[str(product_id)]['total'] = cart[str(product_id)]['quantity'] * cart[str(product_id)]['price']
    else:
        product = Product.objects.get(id=product_id)
        cart[str(product_id)] = {
            'productName': product.productName,
            'price': float(product.price),
            'quantity': 1,
            'total': float(product.price) * 1,
            'image': product.productImage.url if product.productImage else ''
        }

    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'Ogani/shoping-cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

def checkout_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())

    return render(request, 'Ogani/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })



def billing_add(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())

    if request.method == "POST":
        data = request.POST
        qr_image = request.FILES.get('qr_code_image')

        billing = BillingDetail(
            first_name=data['first_name'],
            last_name=data['last_name'],
            country=data['country'],
            address=data['address'],
            town=data['town'],
            postcode=data['postcode'],
            phone=data['phone'],
            email=data['email'],
            qr_code_image=qr_image,
            total=data['total']
        )
        billing.save()
        return redirect('billing_list')
    
    return render(request, 'Ogani/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })

def billing_list(request):
    billings = BillingDetail.objects.all()
    return render(request, 'Ogani/BillingList.html', {'billings': billings})




