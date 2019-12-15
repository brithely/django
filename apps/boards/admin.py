from django.contrib import admin
from .models import Board
from .models import Comment
from .models import Reply


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 0
)


@admin.register(Board)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'text', 'created_at', 'updated_at')
    raw_id_fields = ('user', )
    search_fields = ('user__email', 'user__name')
    inlines = [CommentInlineAdmin, ]
