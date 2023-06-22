from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # 로그인한 사용자 !!
from django.views.generic.list import ListView # cbv 에서 listView쓰기 위해 받아옴
from django.http import HttpResponse, JsonResponse, Http404
from django.core.paginator import Paginator # 페이지 구현 
from .forms import PostModelForm, CommentModelForm # import : 현재 파일과 동일 경로 내 forms 
from .models import Post, Comment  # Post 테이블

# 홈이동
def home(request) :
    return render(request, 'post_index.html')

# 작성된 post들 전부 표시 
def post_list(request):  
    # 모든 객체들(all()) 을 . created_at(생성일 기준), - : 내림차순정렬
    posts = Post.objects.all().order_by('-create_at') 
    paginator = Paginator(posts, 5) # 페이지당 게시글 5개씩 표시
    pagnum = request.GET.get('page') # 현재페이지
    posts = paginator.get_page(pagnum) #현재 페이지에 해당하는 게시글들

    # 딕셔너리형태, posts라는 이름의 posts 리스트 전달, html 파일 렌더링
    return render(request, 'post_list_all.html', {'posts':posts}) 

def post_my(request) :
    posts = Post.objects.all().order_by('-create_at') 
    paginator = Paginator(posts, 5) # 페이지당 게시글 5개씩 표시
    pagnum = request.GET.get('page') # 현재페이지
    posts = paginator.get_page(pagnum) #현재 페이지에 해당하는 게시글들

    # 딕셔너리형태, posts라는 이름의 posts 리스트 전달, html 파일 렌더링
    return render(request, 'post_my.html', {'posts':posts})

def post_detail(request, id):
    # 존재x 페이지 에러 처리 위해 try-catch문 
    try:
        post = get_object_or_404(Post, pk=id)
    except Post.DoesNotExist:
        return redirect('posthome') 
    
    comment_form = CommentModelForm()
    # 예외에 걸리지 않은 post -> 딕셔너리 형태로 넘겨 렌더링 
    context = {
        'post' : post,
        'comment_form' : comment_form
    }
    return render(request, 'post_detail.html', context)

#@login_required
def post_create(request) :
    if request.method == 'POST' or request.method == 'FILES ':
        form = PostModelForm(request.POST, request.FILES)

        if form.is_valid() :
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('post_list') # 작성 완료 하면 posthome으로 보내기 
    
    else : # GET 요청 
        form = PostModelForm()  # form.py 
    return render(request, 'post_create.html', {'form':form})

#@login_required
def post_update(request, id):
    post = Post.objects.get(id=id) #요청한 id에 맞는 post객체 불러옴 

    if request.user != post.author :
        raise Http404('잘못된 접근입니다.수정 권한이 없습니다.')
    
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'post_create.html', {'form':form, 'id':id})

def post_delete(request, id) :
    post = get_object_or_404(Post, pk=id)

    if request.user != post.author :
        raise Http404('잘못된 접근입니다. 게시글은 작성자만 삭제할 수 있습니다.') # 로그인한 사용자와 작성자가 다르면 에러 
    
    if request.method == 'GET' :
        context = {'post' : post}
        return render(request, 'post_confirm_delete.html', context)
    else : # POST 요청 
        post.delete()
    return redirect('post_list') # 삭제 처리 되면 list로 이동햇 

def create_comment(request, id) :
    filled_form = CommentModelForm(request.POST)

    if filled_form.is_valid() :
        # 임시, 댓글 객체 생성 
        finished_form = filled_form.save(commit=False)
        # 넘겨받은 id에 맞는 post를 참조하도록 
        finished_form.article = get_object_or_404(Post, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('post_detail', id)

def update_comment(request, post_id, com_id) :
    my_com = Comment.objects.get(id=com_id) # 댓글 객체 id
    comment_form = CommentModelForm(instance=my_com) # instance로 작성했던 댓글 띄움 
    if request.method == "POST" : # POST
        update_form = CommentModelForm(request.POST, instance=my_com)
        if update_form.is_valid() : # 폼 유효,
            update_form.save() # 저장
            return redirect('post_detail', post_id) # 게시글 id 넘겨 redirect
    else : # GET
        return render(request, 'comment_update.html', {'comment_form':comment_form})

def delete_comment(request, post_id, com_id) :
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('post_detail', post_id)