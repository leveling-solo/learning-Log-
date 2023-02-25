from django.shortcuts import render , redirect ,Http404 
from learning_logs.models import Topic , Entry
from  learning_logs.forms import TopicForm , EntryForm
from django.contrib.auth.decorators import login_required 
# Create your views here.

def index(request): 
    return render(request,'learning_logs/index.html')

@login_required
def topics(request): 
    topics = Topic.objects.filter(owner = request.user).order_by('date')
    context  = {'topics':topics}
    return render(request,'learning_logs/topic.html',context)


@login_required
def topic(request , topic_id): 
    topic = Topic.objects.get(id = topic_id)
    # Make sure the topic belongs to the current user. 
    if topic.owner !=request.user :
        raise Http404 
    entries = topic.entry_set.order_by('-date')
    context = {'topic':topic , 'entries': entries}

    return render(request, 'learning_logs/new_topic.html', context) 

@login_required
def new_topics(request):
    """Add a new topic."""
    if request.method == 'POST':
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topic.html')
    else:
        # No data submitted; create a blank form.
        form = TopicForm()
        context = {'form': form}
        return render(request, 'learning_logs/new_topics.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)  # create form with submitted data
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topics.html', topic_id=topic_id)
    else:
        form = EntryForm()
    context = {'topic': topic, 'form': form ,'topic_id':topic_id}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request , entry_id): 
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic 
    if topic.owner != request.user:
        raise Http404
    if request.method =="POST": 
        form = EntryForm(instance=entry , data=request.POST)
        if form.is_valid() : 
            form.save() 
            return redirect('topics.html',topic_id=topic.id)
    else: 
         # post data submitted ; process data 

         form = EntryForm(instance=entry)
    context ={'entry':entry , 'topic': topic, 'form':form} 
    return render(request,'learning_logs/edit_entry.html', context)