from django.contrib import admin
from .models import User, post, dailypost, viptest


admin.site.register(User)
admin.site.register(post)
admin.site.register(dailypost)
admin.site.register(viptest)