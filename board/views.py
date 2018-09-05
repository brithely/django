from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Board, Comment
from .forms import BoardForm, UserSignupForm, UserSigninForm, CommentForm
# Create your views here.

def index(request):
	boards = Board.objects.all().order_by('-created')[:3]
	return render(request, 'board/board_index.html', {'boards': boards}) 

def board(request):
	boards = Board.objects.all()
	return render(request, 'board/board_list.html', {'boards': boards})

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


	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.num_board_id = board
			comment.created = timezone.now()
			comment.created_user = user	
			comment.save()
			return redirect('board:board_detail', numid=board.num_id)


	return render(request, 'board/board_detail.html', {'isCreatedUser': isCreatedUser, 'board': board, 'comments':comments, 'form':form, 'user': user})
def board_edit(request, numid):
	board = get_object_or_404(Board, pk=numid)

	if request.method == "POST":
		form = BoardForm(request.POST, instance=board)
		if form.is_valid():
			board = form.save(commit=False)
			board.created = timezone.now()
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
			return render(request, 'board/board_list.html', {'boards': boards}) 
		
	else:
		form = BoardForm()
	return render(request, 'board/board_edit.html', {'form' : form })

def board_delete(request, numid):
	board = Board.objects.get(pk=numid)
	board.delete()
	return redirect('board:board')

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
		form = UserSignupForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.date_joined = timezone.now()
			post.set_password(post.password)
			post.save()
			return redirect('board:index') 
	else:
		form = UserSignupForm()
	return render(request, 'board/user_signup.html', {'form' : form})

def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print(request.user.is_authenticated)
			return redirect('board:index');
		else:
			return HttpResponse('Error')

	else:
		form = UserSigninForm()
	return render(request, 'board/user_signin.html', {'form': form})

def signout(request):
	logout(request)
	return redirect('board:index');


#############################Comment##############################



