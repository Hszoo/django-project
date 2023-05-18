from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # 로그인한 사용자 !!
from django.views.generic.list import ListView # cbv 에서 listView쓰기 위해 받아옴
from django.http import HttpResponse, JsonResponse, Http404
from .forms import PostModelForm # import : 현재 파일과 동일 경로 내 forms 
from .models import Post  # Post 테이블


# 홈이동
def home(request) :
    return render(request, 'post_index.html')

# 작성된 post들 전부 표시 
def post_list(request):  
    # 모든 객체들(all()) 을 . created_at(생성일 기준), - : 내림차순정렬
    posts = Post.objects.all().order_by('-create_at') 

    # 딕셔너리형태, posts라는 이름의 posts 리스트 전달, html 파일 렌더링
    return render(request, 'post_list_all.html', {'posts':posts}) 

def post_detail(request, id):
    # 존재x 페이지 에러 처리 
    # 1) try-catch문 
    try:
        post = Post.objects.get(id=id) 
    except Post.DoesNotExist:
        return redirect('index') # 홈으로 redirect 
    
    # 2) 메소드 사용 (import 필요)
    # 존재하지 않는 페이지 id값 입력 -> 404 창 발생시킴 
    # post = get_object_or_404(Post, pk=id)

    # 예외에 걸리지 않은 post -> 딕셔너리 형태로 넘겨 렌더링 
    context = {
        'post' : post,
    }
    return render(request, 'post_detail.html', context)

@login_required
def post_create(request) :
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
        form = PostModelForm()  # form.py 
    return render(request, 'post_create.html', {'form':form})

@login_required
def post_update(request, id):
    post = Post.objects.get(id=id) #요청한 id에 맞는 post객체 불러옴 

    if request.user != post.writer :
        raise Http404('잘못된 접근입니다.\n수정 권한이 없습니다.')
    
    # if request.method == 'POST' :
    #     form = PostModelForm(request.POST, instance=post)
    
    # else : #GET 요청
    #     context = {'post' : post}
    #     return render(request, 'post_create.html', {'form':form, 'id':id})

    ###
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'post_create.html', {'form':form, 'id':id})

def post_delete(request, id) :
    post = get_object_or_404(Post, pk=id)

    if request.user != post.writer :
        raise Http404('잘못된 접근입니다. 게시글은 작성자만 삭제할 수 있습니다.') # 로그인한 사용자와 작성자가 다르면 에러 
    
    if request.method == 'GET' :
        context = {'post' : post}
        return render(request, 'post_confirm_delete.html', context)
    else : # POST 요청 
        post.delete()
    return redirect('post_list') # 삭제 처리 되면 list로 이동햇 