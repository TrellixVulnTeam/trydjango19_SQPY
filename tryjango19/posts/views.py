from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostForm
from .models import Post

def posts_list(request):
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = "pageno"
	page = request.GET.get('page_request_var')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"title" : "List",
		"object_list": queryset,
		"page_request_var":page_request_var,
	}
	return render(request, "post_list.html",context)

def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		messages.success(request,"Successfully Created!")
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"form" : form
	}
	return render(request, "post_form.html",context)
	
#id: link from url.py 
def posts_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance" : instance,
		"title" : instance.title,
	}
	return render(request, "post_detail.html",context)

def posts_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		messages.success(request,"Successfully Saved!")
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"instance" : instance,
		"title" : instance.title,
		"form" : form,
	}
	return render(request, "post_form.html",context)

def posts_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Successfully Deleted!")
	return redirect("posts:list")


