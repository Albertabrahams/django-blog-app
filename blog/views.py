from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = { "posts": posts}

    return render(request,'blog/post_list.html', context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        student = form.save()
        
        if 'image' in request.FILES:
            student.image = request.FILES.get('image')
            student.save()
        return redirect('home')

    context = {
        'form' : form
    }
    return render(request,'blog/post_create.html', context)

def post_update(request,id):
    post = Post.objects.get(id=id)
    print(post)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect("home")
    context = {
        "form":form
    }
    return render(request, "blog/post_update.html", context)

def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.POST:
        post.delete()
        return redirect("home")
    context = {"post": post}
    return render(request, "blog/post_delete.html", context)

@login_required(login_url='/users/login/')
def post_detail(request, id):        
    post = Post.objects.get(id=id)
    user = request.user
    like = Like.objects.filter(post=id, user=user.id)
    lcount = Like.objects.filter(post=id).count()
    if request.POST:
        try:
            test = Like.objects.get(post_id=id,user_id=user.id)
        except:
            test = None
        if not test:
            murat = Like.objects.create(post_id=id,user_id=user.id) 
            print("murat")
            murat.save()
            
        else:
            test.delete()
            
            

        

    context = {
        'post': post,
        'user': user,
        'like': like,
        'lcount': lcount
    }
    return render(request, 'blog/post_detail.html', context)



    

