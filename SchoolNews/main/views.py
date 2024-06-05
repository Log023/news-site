from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticlesForm, CommentForm
from django.contrib.auth.decorators import login_required


def index(request):
    # Сортируем новости по дате в порядке убывания
    news = Articles.objects.order_by('-date')

    context = {
        'news': news,
    }

    return render(request, 'main/index.html', context)

@login_required
def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    comments = article.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'main/article_detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()
    return render(request, 'main/create.html', {'form': form, 'error': error})

@login_required
def delete_article(request, id):
    article = get_object_or_404(Articles, id=id)

    if not request.user.is_superuser:
        return redirect('article_detail', pk=article.id)  # Используем 'pk' вместо 'id'

    if request.method == 'POST':
        article.delete()
        return redirect('home')  # Замените 'home' на ваше представление для домашней страницы или списка статей

    return render(request, 'main/delete_article_confirm.html', {'article': article})

@login_required
def edit_article(request, id):
    article = get_object_or_404(Articles, id=id)

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.id)  # Используем 'pk' вместо 'id'
    else:
        form = ArticlesForm(instance=article)

    return render(request, 'main/edit_article.html', {'form': form, 'article': article})


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')