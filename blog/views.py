from django.http import HttpResponse, Http404
from django.views import generic
from .models import Blog, Category, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogCreateForm, CommentCreateForm, PostSearchForm
from django.db.models import Q
from django.http.response import JsonResponse
from django.contrib import messages
from functools import reduce
from operator import and_


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'blog/top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blog_views'] = Blog.objects.order_by('-views')[:4]
        return ctx


class CategoriesListView(generic.ListView):
    model = Category
    template_name = 'blog/categories.html'
    paginate_by=8

    def categories(request,id):
        context = {
            'categories': Category.objects.all(),
            'blog_list': Blog.objects.filter(category_id=id),
            }
        return render(request, 'blog/categories.html',context)


class BlogCategoryList(generic.ListView):
    model = Blog
    ordering = '-created_at'
    template_name = 'blog/category_list.html'
    paginate_by=8

    def get_queryset(self):
        category = get_object_or_404(Category,pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category)


def detail(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        raise Http404

    context = {
        'blog':blog,
    }
    blog.views += 1
    blog.save()
    return render(request, 'blog/blog_detail.html', context)


def blog_create(request):
    form = BlogCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('blog:top')

    context={
        'form':form,
    }
    return render(request, 'blog/blog_create.html', context)


class CommentCreate(generic.CreateView):
    model=Comment
    form_class=CommentCreateForm

    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Blog,pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('blog:blog_detail',pk=post_pk)

class SearchListView(generic.ListView):
    model = Blog
    ordering = '-created_at'
    template_name = 'blog/search.html'
    paginate_by=8

    def blogs(request):
        context = {
            'blog_list': Blog.objects.all(),
            }
        return render(request, 'blog/search.html',context)

    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''
            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i
            query = reduce(
                and_, [Q(title__icontains=q) | Q(text__icontains=q) for q in q_list]
            )
            queryset = queryset.filter(query)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))

    # def get_queryset(self):
    #     queryset=super().get_queryset()
    #     form=PostSearchForm(self.request.GET or None)
    #     if form.is_valid():
    #         key_word=form.cleaned_data.get('key_word')
    #         if key_word:
    #             queryset=queryset.filter(Q(title__icontains=key_word)|Q(text__icontains=key_word))

            # category=form.cleaned_data.get('category')
            # if category:
            #     queryset=queryset.filter(category=category)

        return queryset

# def like(request,pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         raise Http404
#     blog.like += 1
#     blog.save()
#     return redirect('blog:blog_detail',pk)

# def api_like(request,pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         raise Http404
#     blog.like += 1
#     blog.save()
#     return JsonResponse({"like":blog.like})

class RecommendListView(generic.ListView):
    model = Blog
    template_name = 'blog/recommend.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blog_views'] = Blog.objects.order_by('-views')
        return ctx
