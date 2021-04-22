from django.shortcuts import render
from django.urls.base import reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, CreateView,ListView, DetailView, DeleteView
from . import models

# Create your views here.
def start(request):
    allCats=models.Category.objects.all()
    categories=[("bucket_"+str(cat.id), cat, cat.relatedItems.all(),str(cat.id)) for cat in allCats]
    allItems=models.Item.objects.all()
    items=[("Item_"+str(item.id), item, item.categories.all(),str(item.id)) for item in allItems]


    context={'allCats': categories, 'allItems': items}
    return render(request,'index.html',context)

def createCategory(request):
    form=request.POST
    print(form)
    if len(form):
        form=dict(form)
        topic=form['topic'][0]
        category=models.Category(topic=topic)
        category.save()                           # muss zweimal gesaved werden
    return HttpResponseRedirect('/bucket/start')


class DeleteCategoryView(DeleteView):

    model = models.Category
    success_url = '/bucket/start'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def createItem(request):
    form=request.POST
    print(form)
    if len(form):
        form=dict(form)
        title=form['title'][0]
        item=models.Item(title=title)
        item.save()                           

    return HttpResponseRedirect('/bucket/start')

def link(request,pk1,pk2):

    category=models.Category.objects.get(id=pk1)
    item=models.Item.objects.get(id=pk2)
    item.categories.add(category)
    category.relatedItems.add(item)
    item.save()
    category.save()

    return HttpResponseRedirect('/bucket/start')

class DeleteItemView(DeleteView):
    
    model = models.Item
    success_url = '/bucket/start'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def uncouple(request, pk,pk2):
    category=models.Category.objects.get(id=pk2)
    outOfTheHouse=models.Item.objects.get(id=pk)
    category.relatedItems.remove(pk)
    # category.save()
    # outOfTheHouse.save()
    return HttpResponseRedirect('/bucket/start')