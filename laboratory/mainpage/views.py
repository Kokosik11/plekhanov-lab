from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post, Project, Comment
from .forms import FeedbackForm, CommentForm, OrderCreateForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

def mainpage(request):
  posts = Post.objects.filter(is_head=False, status=1).order_by('-created_on')
  heading = Post.objects.filter(is_head=True, status=1)
  all_projects = Project.objects.filter(status=1)
  common_tags = Post.tags.most_common()[:4]
  if request.method == "POST":
    form = FeedbackForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      phone = form.cleaned_data.get('phone')
      feedback = form.save()
      num = feedback.uuid
      messages.add_message(request, messages.INFO, f'Спасибо за оставленную заявку, {name}!')
      send_mail(
        'Ваша заявка успешно добавлена.',
        f'Здравствуйте, {name}.\n\nВаша заявка № {num} успешно зарегистрирована. \n\nВ скором времени наша команда свяжется с вами по номеру {phone}.',
        settings.EMAIL_HOST_USER,
        [f'{email}'],
        fail_silently=False,
      )
      return redirect('blog')
  else:
    form = FeedbackForm()

  if request.method == "POST":
    order_form = OrderCreateForm(request.POST)
    if order_form.is_valid():
      name = request.user.first_name
      email = request.user.email
      order = order_form.save(commit=False)
      order.user = request.user
      order.save()
      send_mail(
        'Ваш заказ успешно создан.',
        f'Здравствуйте, {name}.\n\nВаша заявка № {order} успешно создана. \n\nВ скором времени мы обработаем и примем ваш заказ',
        settings.EMAIL_HOST_USER,
        [f'{email}'],
        fail_silently=False,
      )
      return redirect('blog')
  else:
    order_form = OrderCreateForm()

  context = {
      'posts': posts,
      'heading': heading,
      'all_projects': all_projects,
      'form': form,
      'common_tags': common_tags,
      'order_form': order_form,
  }
  
  return render(request, 'mainpage/index.html', context)

def posts(request):
  posts = Post.objects.filter(is_head=False, status=1).order_by('-created_on')

  context = {
    'posts': posts,
  }

  return render(request, 'mainpage/posts.html', context)


def tagged(request, slug):
  tag = get_object_or_404(Tag, slug=slug)
  posts = Post.objects.filter(tags=tag)
  context = {
    'tag': tag,
    'posts': posts,
  }
  return render(request, 'mainpage/posts.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
      is_liked = True
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    post_object = Post.objects.get(slug=slug)
    post_object.views = post_object.views + 1
    post_object.save()

    if request.method == 'POST':
      comment_form = CommentForm(request.POST or None)
      if comment_form.is_valid():
        content = request.POST.get('content')
        comment_qs = None
        comment = Comment.objects.create(post=post, user=request.user, content=content)
        comment.save()
        # return HttpResponseRedirect(post.get_absolute_url())
    else:
      comment_form = CommentForm()

    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }

    if request.is_ajax():
      html = render_to_string('mainpage/comments.html', context, request=request)
      return JsonResponse({'form': html})

    return render(request, 'mainpage/post-detail.html', context)


@login_required
def like_post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  is_liked = False
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
    is_liked = False
  else:
    post.likes.add(request.user)
    is_liked = True
  context = {
      'post': post,
      'is_liked': is_liked,
      'total_likes': post.total_likes(),
  }
  if request.is_ajax():
    html = render_to_string('mainpage/likes.html', context, request=request)
    return JsonResponse({'form': html})


class ProjectDetailView(DetailView):
  model = Project
  template_name = "mainpage/project-detail.html"