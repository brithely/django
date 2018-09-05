from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
	path('', views.index, name='index'),
	path('signin/', views.signin, name='signin'),
	path('signup/', views.signup, name='signup'),
	path('signout/', views.signout, name='signout'),
	path('board/', views.board, name='board'),
	path('board/page/<pagenum>', views.board_page, name='board_page'),
	path('board/new/', views.board_new, name='board_new'),
	path('board/<numid>/', views.board_detail, name='board_detail'),
	path('board/<numid>/edit', views.board_edit, name='board_edit'),
	path('board/<numid>/delete', views.board_delete, name='board_delete'),
	path('board/<numid>/comment/<comid>/detelte', views.comment_delete, name='comment_delete')
]

