from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketing.models import Singup

def get_category_count():
	queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
	return queryset

def index(request):
	featured = Post.objects.filter(featured=True)
	latest = Post.objects.order_by('-timestamp')[0:3]

	if request.method == 'POST':
		email = request.POST['email']
		new_signup = Singup()
		new_signup.email = email
		new_signup.save()
		
	content = {
		'object_list':featured,
		'latest':latest
	}
	return render(request,'index.html',content)

def blog(request):
	category_count = get_category_count()
	most_recent = Post.objects.order_by('-timestamp')[:3]
	post_list  = Post.objects.all()
	paginator = Paginator(post_list,4)
	page_request_var = 'page'
	page = request.GET.get('page')
	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		'queryset':paginated_queryset,
		'page_request_var':page_request_var,
		'most_recent':most_recent,
		'category_count':category_count
	}
	return render(request,'blog.html',context)

def post(request,id):
	return render(request,'post.html',{})