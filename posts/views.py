from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from .models import Post
from string import punctuation

# Create your views here.
class CreatePost(CreateView):
    

    model = Post
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('homepage')
    fields = ( 'title', 'content' )

    def form_valid(self, form):
        post = form.save(commit= False)
        post.slug = post.title.translate(str.maketrans(' ', '-', punctuation)).lower()
        post.author = self.request.user
        return super().form_valid(form)
    

class UpdatePost(UpdateView):
    

    model = Post
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('homepage')
    fields = ( 'title', 'content' )

    def form_valid(self, form):
        post = form.save(commit= False)
        post.slug = post.title.translate(str.maketrans(' ', '-', punctuation)).lower()
        return super().form_valid(form)
    

class DeletePost(DeleteView):

    model = Post
    success_url = reverse_lazy('homepage')