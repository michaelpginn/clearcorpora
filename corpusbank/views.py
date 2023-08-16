from django.shortcuts import render, get_object_or_404, redirect
from .models import Corpusobject
from .forms import PostForm
import operator
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    posts = Corpusobject.objects.filter(knownloc = True).order_by('name')
    return render(request, 'corpusbank/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Corpusobject, pk=pk)
	return render(request, 'corpusbank/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'corpusbank/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Corpusobject, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'corpusbank/post_edit.html', {'form': form})


def search_form(request):
    return render(request, 'corpusbank/search_form.html')

def search(request):
	error = False
	if 'q[name]' in request.GET:
		qn = request.GET['q[name]']
		qc = request.GET['q[catid]']
		ql = request.GET['q[languages][]']
		if not (qn or qc or ql):
			error = True
		elif qn and (not qc and not ql):
			myresults = Corpusobject.objects.filter(name__icontains=qn).order_by('name')
			return render(request, 'corpusbank/search_results.html', {'myresults': myresults, 'query': qn})
		elif qc and (not qn and not ql):
			myresults = Corpusobject.objects.filter(catid__icontains=qc).order_by('name')
			return render(request, 'corpusbank/search_results.html', {'myresults': myresults, 'query': qc})
		elif ql and (not qn and not qc):
			myresults = Corpusobject.objects.filter(language__icontains=ql).order_by('name')
			return render(request, 'corpusbank/search_results.html', {'myresults': myresults, 'query': ql})
		elif (qc and qn) and not ql:
			myresults = Corpusobject.objects.filter(name__icontains=qn).filter(catid__icontains=qc).order_by('name')
			return render(request, 'corpusbank/search_results.html', {'myresults': myresults})
		elif (qc and ql) and not qn:
			myresults = Corpusobject.objects.filter(catid__icontains=qc).filter(language__icontains=ql).order_by('name')
			return render(request, 'corpusbank/search_results.html', {'myresults': myresults})
		elif (qn and ql) and not qc:
			myresults = Corpusobject.objects.filter(name__icontains=qn).filter(language__icontains=ql).order_by('name')
			return render(request, 'corpusbank/search_results.html', {'myresults': myresults})
	return render(request, 'corpusbank/search_form.html', {'error': error})


