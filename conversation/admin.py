from django.contrib import admin

# Register your models here.
from .models import Conversation, ConversationMesssage

admin.site.register(ConversationMesssage)
admin.site.register(Conversation)