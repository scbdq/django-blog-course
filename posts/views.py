from django.http import HttpResponse


def home_view(request):
    """Render the blog homepage with a welcome message."""
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")


def about_view(request):
    """Render the about page with basic author info."""
    return HttpResponse("<h1>Об авторе</h1><p>Добро пожаловать на страницу об авторе.</p>")
