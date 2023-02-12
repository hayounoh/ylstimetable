from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
import datetime

from django.core.paginator import Paginator

#from .forms import PostForm, ResponseForm
from .models import Post, Response


@login_required(login_url='common:login')
def index(request):
    user = request.user

    if user.student_auth == False:
        return render(request, 'unauth.html')

    page = request.GET.get('page', '1')

    post_list = Post.objects.order_by('-create_date')

    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)

    context = {'survey_list': page_obj}
    return render(request, 'survey_list.html', context)
  
  
