from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Article
from .forms import ArticleForm


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "permitions_task/article_list.html"
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "permitions_task/article_detail.html"
    context_object_name = "article"

@login_required
@permission_required('permitions_task.can_edit_article', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Článok bol upravený.")
            return redirect("article_detail", pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "permitions_task/article_form.html", {"form": form})

@login_required
@permission_required('permitions_task.can_delete_article', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        messages.success(request, "Článok bol vymazaný.")
        return redirect("article_list")
    return render(request, "permitions_task/article_confirm_delete.html", {"article": article})
