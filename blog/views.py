from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import CommentForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='login')


class PostList(ListView):
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return queryset


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('created_date')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            form = CommentForm(request.POST)
            post = self.get_object()
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()

                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','text']
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk })


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk })


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post_list')

def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.like()
    return redirect('post_detail', pk=comment.post.pk) 

def comment_dislike(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.dislike()
    return redirect('post_detail', pk=comment.post.pk)

