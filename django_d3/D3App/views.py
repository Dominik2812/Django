from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import  DeleteView

from . import models
import json

def welcome(request):
    return render(request, 'D3App/bubbles/welcome.html')

###############################################################################################
######################################create Bubble########################################
# ###############################################################################################
def createBubble(request):
    form=request.POST
    if len(form):
        form=dict(form)
        topic=form['topic'][0]
        bubble=models.Bubble(topic=topic)
        bubble.save()                          
    else:
        topic=0
    return HttpResponseRedirect(reverse("D3App:bubbles"))
# ###############################################################################################
# ###################################### List All bubbles in a tree like manner  ########################################
# ###############################################################################################

def bubbles(request):
    context=buildTree()
    return render(request, 'D3App/bubbles/reservoir_link.html', context)

def buildTree():
    family = []
    allData=models.Bubble.objects.all()
    if allData:
        for item in allData:
            if item.motherBubble!= None: 
                x=item.motherBubble.id
            else:
                x=0
            family.append({'name':item.topic,'id':item.id,'children': [], 'parent': x, 'size':1})
            recFam=listRecursive(family)

        context={'family':recFam}
    else:
        context={}
    return context

def listRecursive(family):
    for item in family:
        print(item['parent'])
    if item['parent'] > 0: 
        for item2 in family: 
            if item2['id'] == item['parent']:
                item2['children'].append(item)
                break;
    redFamily=[]
    for item in family:
        if item['parent']==0:
            redFamily.append(item)
    return json.dumps(redFamily)


# ###############################################################################################
# #####consider an individual Bubble with children, related Bubbles ########################################
# ###############################################################################################
def changeBubble(request):
    id=request.POST['id']
    topic= request.POST['topic']
    child=request.POST['child']
    relate=request.POST['relate']
    decouple=request.POST['decouple']
    outOfTheHouse=request.POST['outOfTheHouse']
    bubble=models.Bubble.objects.get(id=id)
    if len(topic)>0:
        bubble.topic=topic
        bubble.save()
    if len(child)>0:
        child=models.Bubble.objects.get_or_create(topic=child)
        if not child[0].motherBubble:
            bubble.subBubbles.add(child[0])
            bubble.save()
    if len(relate)>0:
        relate=models.Bubble.objects.get_or_create(topic=relate)
        bubble.bubbs.add(relate[0])
        bubble.save()
    if len(decouple)>0:
        decouple=models.Bubble.objects.get(topic=decouple)
        bubble.bubbs.remove(decouple)
        bubble.save()
    if len(outOfTheHouse)>0:
        outOfTheHouse=models.Bubble.objects.get(topic=outOfTheHouse)
        bubble.subBubbles.remove(outOfTheHouse)
        bubble.save()
    
    return HttpResponseRedirect('/app/singleBubble/'+str(id))



def singleBubble(request,pk):
    bubble_children = []
    bubble_related = []
    bubble=models.Bubble.objects.get(id=pk)
    children=bubble.subBubbles.all()
    
    for child in children:
        bubble_children.append({'name':child.topic , 'id':child.id, 'children': [], 'parent': bubble.topic , 'size':1})
    related=bubble.bubbs.all()
    for partner in related:
        if partner.motherBubble: 
            print('hello')
            parent=partner.motherBubble.topic
        else:
            parent=0
        bubble_related.append({'name':partner.topic , 'id':partner.id, 'children': [], 'parent': parent , 'size':1})

    if bubble.motherBubble: 
        parent=bubble.motherBubble.topic
    else:
        parent=0
    
    bubble_children=[{'name':bubble.topic,'id':bubble.id,'children': bubble_children, 'parent': parent, 'size':1}]
    bubble_related=[{'name':bubble.topic,'id':bubble.id,'children': bubble_related, 'parent': parent, 'size':1}]
    id=bubble.id
    topic=bubble.topic

    bubble_children=json.dumps(bubble_children)
    bubble_related=json.dumps(bubble_related)
    family=buildTree()['family']
    

    context={'bubble_children': bubble_children, 'bubble_related': bubble_related, 'id':id, 'topic':topic, 'family':family}
    return render(request, 'D3App/bubbles/reservoir_link.html', context)


# ###############################################################################################
# ###################################### delete Bubble ########################################
# ###############################################################################################

class DeleteBubbleView(DeleteView): 
    model = models.Bubble
    success_url =  '/app/bubbles' 
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

