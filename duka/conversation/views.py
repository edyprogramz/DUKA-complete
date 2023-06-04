from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

# Create your views here.
@login_required
def new(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect("dashboard:index")
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        return redirect("conversation:detail", pk=conversations.first().id)
    
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect("item:detail", pk=item_pk)
    
    else:
        form = ConversationMessageForm()
    
    return render(request, "conversation/new.html", {
        "form": form
    })
    
@login_required
def inbox(request):
    # conversation = get_object_or_404(Conversation, id=conversation_id)

    conversations = Conversation.objects.filter(members__in=[request.user.id])
    # is_read = Conversation.objects.add()
    
    return render(request, "conversation/inbox.html", {
        "conversations": conversations
        # "is_read": is_read
    })

@login_required
def detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id, members=request.user)
    
    # Update the read status of the accessed conversation
    messages_from_other_users = conversation.messages.exclude(created_by=request.user)
    if messages_from_other_users.exists():
        conversation.is_read = True
        conversation.save()
        
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('.')
    else:
        form = ConversationMessageForm()
        
    return render(request, "conversation/detail.html", {
        "conversation": conversation,
        "form": form
    })