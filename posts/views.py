# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return a post detail"""
    template_name = 'posts/detail.html'
    slug_field = 'pk'
    slug_url_kwarg = 'post_id'
    model = Post

    def get_context_data(self, **kwargs):
        """Add post to context"""
        context = super().get_context_data(**kwargs)
        post_id = self.get_object().pk
        context['post'] = Post.objects.get(pk=post_id)
        return context


class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context


# @login_required
# def create_post(request):
#     """Create new post view."""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')

#     else:
#         form=PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form':form,
#             'user': request.user,
#             'profile':request.user.profile
#         }
#     )
