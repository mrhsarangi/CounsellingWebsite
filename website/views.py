from typing import Any
from django.views.generic import TemplateView
from posts.models import Post

class Home(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context