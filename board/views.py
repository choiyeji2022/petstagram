from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponseRedirect


# Create your views here.
def create_feed_view(request):
    #게시글 작성
    if request.method == 'GET':
        user = request.user.is_authenticated
        # 유저가 로그인 됐는지 확인
        if user:
            # 유저가 로그인 했을 때
            return render(request, 'board/post.html')
        else:
            # 유저가 로그인 하지 않았을 때
            return redirect('/login')
    elif request.method == 'POST':      # 사용자가 post 버튼을 눌러 게시를 했을지 실행됨
        user = request.user # 게시글 작성시 필요해서 추가
        post = Post()

        post.author = user # 게시글 작성시 필요해서 추가
        #작성자 입력 란
        post.title = request.POST.get('title','')
        post.content = request.POST.get('user-content','')
        post.save()

        # return HttpResponse('create_feed_view_POST')
        
        # 작성 후 main으로 이동
        return redirect('/')

#           DEAD_CODE
# def delete_feed_view(request, id):
#     #게시글 삭제
#     feed = Post.objects.get(id=id)
#     feed.delete()
#     return  HttpResponse('delete_ok')
#     # working on it
#     # pass
#
# def update_feed_view(request):
#     #게시글 수정
#     pass
# def read_feed_view(request):
#     #게시글 조회
#     pass
#           DEAD_CODE_END


# 메인페이지 게시글 피드
def mainpage_feed(request):
    if request.method == 'GET':
        post_feeds = Post.objects.all().order_by('-create_at')

        return render(request, 'board/petstagram.html', {'post_fedds': post_feeds})