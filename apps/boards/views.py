from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Board, Comment
from .forms import BoardForm, UserSignForm, CommentForm
# Create your views here.


class BoardListView(ListView):
	template_name = "board/board_list.html"
	queryset = Board.objects.all()
	context_object_name = 'board_list'


def board_page(request, pagenum):
	pageRow = 5
	maxpage = int(pagenum)*pageRow
	minpage = int(pagenum)*pageRow-5;
	boards = Board.objects.all().order_by('-created')[minpage:maxpage]
	pages = Board.objects.all()
	count = pages.count()

	if int(pagenum)%5 == 0:
		pagecount = int(int(pagenum)/pageRow)
		maxcount = int(pagecount)*pageRow
		mincount = maxcount-5+1
	else:
		pagecount = int(int(pagenum)/pageRow)+1
		maxcount = int(pagecount)*pageRow
		mincount = maxcount-5+1
	if maxcount*pageRow > int(count):
		maxcount= int(int(count)/pageRow)+1
	if int(pagecount) > int(count):
		pagecount = count

	if count >= maxpage:
		isMax = True
	else:
		isMax = False
	prepage = int(pagenum)-1
	nextpage = int(pagenum)+1

	page = range(mincount, maxcount+1)
	return render(request, 'board/board_list.html', {'boards': boards, 'page':page, 'nextpage':nextpage, 'prepage':prepage, 'isMax': isMax})

def board_detail(request, numid):
	board = Board.objects.get(pk=numid)
	try:
		user = User.objects.get(id=int(request.user.id))
	except:
		user = False
	form = CommentForm
	try:
		comments = Comment.objects.filter(num_board_id=numid)
	except Comment.DoesNotExist:
		comments = False

	if str(request.user.username) == str(board.created_user):
		isCreatedUser = True
	else:
		isCreatedUser = False

	for comment in comments:
		if str(request.user.username) == str(comment.created_user):
			comment.isCreatedUser = True
		else:
			comment.isCreatedUser = False


	return render(request, 'board/board_detail.html', {'isCreatedUser': isCreatedUser, 'board': board, 'comments':comments, 'form':form, 'user': user})


	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.num_board_id = board
			comment.created = timezone.now()
			comment.created_user = user	
			comment.save()
			return redirect('board:board_detail', numid=board.num_id)

	if request.method == "DELETE":
		print("METHOD TEST")

def board_edit(request, numid):
	board = get_object_or_404(Board, pk=numid)

	if request.method == "POST":
		form = BoardForm(request.POST, instance=board)
		if form.is_valid():
			board = form.save(commit=False)
			board.save()
			return redirect('board:board_detail', numid=board.num_id)

	else:
		form = BoardForm(instance=board)
	return render(request, 'board/board_edit.html', {'form': form})
	


def board_new(request):
	if request.method == "POST":
		form = BoardForm(request.POST)
		if form.is_valid():
			user = User.objects.get(id=int(request.user.id))
			print(user)
			post = form.save(commit=False)
			post.created = timezone.now()
			post.created_user = user
			post.save()
			boards = Board.objects.all()
			return redirect('board:board_page', pagenum=1) 
		
	else:
		form = BoardForm()
	return render(request, 'board/board_edit.html', {'form' : form })

def board_delete(request, numid):
	board = Board.objects.get(pk=numid)
	board.delete()
	return redirect('board:board_page', pagenum=1)

def comment_delete(request, numid, comid):
	try:
		comment = Comment.objects.get(num_com_id=comid)
	except Comment.DoesNotExist:
		comment = False
	if comment:
		comment.delete()
	return redirect('board:board_detail', numid=numid)

################################USER############################
def signup(request):
	if request.method == "POST":
		form = UserSignForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.date_joined = timezone.now()
			post.set_password(post.password)
			post.save()
			return redirect('board:index') 
	else:
		form = UserSignForm()
	return render(request, 'board/user_signup.html', {'form' : form})

def signin(request):
	if request.method == "POST":
		form = UserSignForm()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print(request.user.is_authenticated)
			return redirect('board:index');
		else:
			error = True
			return render(request, 'board/user_signin.html', {'form':form, 'error':error})

	else:
		form = UserSignForm()
		error = False
	return render(request, 'board/user_signin.html', {'form': form, 'error':error})

def signout(request):
	logout(request)
	return redirect('board:index')


#############################Comment##############################


############################Search###############################

def search_page(request, search, pagenum):
        pageRow = 5
        maxpage = int(pagenum)*pageRow
        minpage = int(pagenum)*pageRow-5;
        boards = Board.objects.filter(title__contains=search).order_by('-created')[minpage:maxpage]
        pages = Board.objects.filter(title__contains=search)
        count = pages.count()

        if int(pagenum)%5 == 0:
                pagecount = int(int(pagenum)/pageRow)
                maxcount = int(pagecount)*pageRow
                mincount = maxcount-5+1
        else:
                pagecount = int(int(pagenum)/pageRow)+1
                maxcount = int(pagecount)*pageRow
                mincount = maxcount-5+1
        if maxcount*pageRow > int(count):
                maxcount= int(int(count)/pageRow)+1
        if int(pagecount) > int(count):
                pagecount = count

        if count >= maxpage:
                isMax = True
        else:
                isMax = False
        prepage = int(pagenum)-1
        nextpage = int(pagenum)+1

        page = range(mincount, maxcount+1)
        return render(request, 'board/board_list.html', {'boards': boards, 'page':page, 'nextpage':nextpage, 'prepage':prepage, 'isMax': isMax})
