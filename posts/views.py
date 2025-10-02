from django.http import HttpResponse

from .models import Post

def home_view(request):
    """Render the blog homepage with a welcome message."""
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")


def about_view(request):
    """Render the about page with basic author info."""
    return HttpResponse("<h1>Об авторе</h1><p>Добро пожаловать на страницу об авторе.</p>")


def post_list_view(request):
    """Render a simple list of posts."""
    posts = Post.objects.all()
    html = ["<h1>Все посты</h1><ul>"]
    for post in posts:
        snippet = post.content[:50]
        html.append(f"<li><strong>{post.title}</strong>: {snippet}...</li>")
    html.append('</ul>')
    return HttpResponse(''.join(html))
