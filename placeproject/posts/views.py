from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post  # Post 테이블

# Create your views here.
def home(request) :
    return render(request, 'post_index.html')

def createpost(request) :
    if request.method == 'POST' :
        form = PostModelForm(request.POST)
        image = request.FILES.get('image')
        content = request.POST.get('content')

        Post.objects.create(
            image=image,
            content=content,
            #writer=request.user
        )

        if form.is_valid() :
            form.save()
            return redirect('posthome') # 작성 완료 하면 posthome으로 보내기 
    else : # GET 요청 
        form = PostModelForm() 
    return render(request, 'create_post.html', {'form':form})

# 작성된 post들 전부 표시 
def post_list(request): # models 에서 가져온 Post의 
    posts = Post.objects.all().order_by('-create_at') 
    # 모든 객체들(all()) 을
    # created_at(생성일 기준), - : 내림차순정렬
    return render(request, 'post_list_all.html', {'posts':posts}) 
    # 딕셔너리형태, posts라는 이름의 posts 리스트 전달, html 파일 렌더링

#def post_detail(request, id) :
#   post = Post.objects.get(id=id)
#   return render(request, 'post_detail.html', {'post':post})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context={
        'post':post
    }
    return render(request, 'post_detail.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'create_post.html', {'form':form, 'id':id})

def post_delete(reqeust, id) :
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')