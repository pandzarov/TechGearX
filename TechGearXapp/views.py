from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

# Create your views here.
from TechGearXapp.form import UserRegistrationForm, PostForm
from TechGearXapp.models import Post, Cart


def launch(request):
    return render(request, "launch.html")


def logout(request):
    auth_logout(request)
    messages.success(request, "You were successfully logged out!")
    return redirect('home')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, "There Was An Error Logging In, Try Again...")
            return redirect('login')


    else:
        return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")

    return redirect(login)


def register(request):
    if request.user.is_authenticated:
        return redirect(home)

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="registration.html",
        context={"form": form}
    )


def shop(request):
    queryset = Post.objects.all()
    context = {"posts": queryset, "form": PostForm}
    return render(request, "shop.html", context=context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('shop')  # Redirect to post detail page
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def add_to_cart(request, post_id):
    post = Post.objects.get(pk=post_id)
    cart_item, created = Cart.objects.get_or_create(author=request.user, item=post)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, author=request.user)
    cart_item.delete()
    return redirect('cart')


def cart(request):
    cart_items = Cart.objects.filter(author=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})


def profile(request):
    return render(request, 'profile.html')


def products(request):
    queryset = Post.objects.filter(author=request.user)
    context = {"products": queryset}
    return render(request, "products.html", context=context)


def remove_post(request, post_id):
    product = get_object_or_404(Post, id=post_id, author=request.user)
    product.delete()
    return redirect('products')
