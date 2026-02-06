from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item, members__in=[request.user])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            con_message = form.save(commit=False)
            con_message.conversation = conversation
            con_message.created_by = request.user
            con_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])
    
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = get_object_or_404(
        Conversation,
        pk=pk,
        members__in=[request.user]
    )

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            con_message = form.save(commit=False)
            con_message.conversation = conversation
            con_message.created_by = request.user
            con_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })
