from django.http import HttpResponse


def home_view(request):
    """Render the blog homepage with a welcome message."""
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")
