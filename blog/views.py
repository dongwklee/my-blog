from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

from django.contrib.auth.decorators import login_required


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})
@login_required
def post_new(request):
	if request.method =='POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail',pk=post.pk)
	else:
		form = PostForm()
		return render(request, 'blog/post_edit.html',{'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('blog.views.post_detail',pk=pk)
def publish(self):
	self.published_date = timezone.now()
	self.save()
def post_remove(request, pk):
	post = get_object_or_404(Post,pk=pk)
	post.delete()
	return redirect('blog.views.post_list')


def image_input(request):
  if request.method == 'POST':
    form = post(request.POST, request.FILES)
    if form.is_valid():
      post = User.objects.get('noel').get_profile()
      post.picture = request.FILES['picture']
      post.save()
      return HttpResponseRedirect('/next/page/')
  form = PhotoForm()
  return render_to_response(
      'post_edit.html',
      {'form': form },
      RequestContext(request))
