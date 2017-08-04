from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)   # pk에 해당하는 post가 없을 경우 404페이지 호출
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":                #페이지에서 form에서 POST라는 메소드 호출하여 값을 전달
        form = PostForm(request.POST)
        if form.is_valid():                         # form값 확인 이후 값 저장
            post = form.save(commit=False)         # commit=False 바로 저장하지 말고 대기
            post.author = request.user              # post에 작성자, 시간 정보 추가
            post.published_date = timezone.now()    
            post.save()                             #저장
            return redirect('post_detail', pk=post.pk)  # 작성한 글로 페이지 이동
    else:   #페이지 접속시
        form = PostForm()   #form.py에서 만든 form class
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})