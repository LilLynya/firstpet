from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Forms
from workspace.forms import AddGroup, CreateGroup, MakeTask

# Models
from workspace.models import Teams, Tasks


@login_required
def add_group(request):
    username = f'{request.user.username}'
    user = get_user_model().objects.get(username=username)
    if request.method == 'POST':
        add_group_form = AddGroup(request.POST)
        if add_group_form.is_valid():
            username_from_request = f'{request.user.username}'
            entered_group = add_group_form.cleaned_data['group']
            user = get_user_model().objects.get(username=username_from_request)
            user.group = entered_group
            user.save()
            return reverse_lazy('workspace:mygroup')
    else:
        add_group_form = AddGroup()
    extra_context = {
        'form': add_group_form,
        'selfuser': user,
    }
    return render(request, 'add_group.html', context=extra_context)


@login_required
def create_group(request):
    username = f'{request.user.username}'
    selfuser = get_user_model().objects.get(username=username)
    if request.method == 'POST':
        create_group_form = CreateGroup(request.POST)
        if create_group_form.is_valid():
            username_from_request = f'{request.user.username}'
            entered_group = create_group_form.cleaned_data['group']
            user = get_user_model().objects.get(username=username_from_request)
            user.team = entered_group
            user.creator = True
            user.save()

            team = create_group_form.save(commit=False)
            team.group = entered_group
            team.created_by = username_from_request
            team.important = username_from_request
            team.save()
            return HttpResponseRedirect(reverse('workspace:my_group'))
    else:
        create_group_form = CreateGroup()
    extra_context = {
        'form': create_group_form,
        'selfuser': selfuser,
    }
    return render(request, 'create_group.html', context=extra_context)


@login_required
def workspace(request):
    username = f'{request.user.username}'
    group_id = f'{request.user.team}'

    user = get_user_model().objects.get(username=username)
    team = Teams.objects.get(group=group_id)
    members = get_user_model().objects.filter(team=group_id)
    count = get_user_model().objects.filter(team=group_id).count()
    tasks = Tasks.objects.filter(tasks=group_id, to= f'{request.user.role}')
    workspace_buttons = [
        {"name": "My Group", "link": "/workspace/mygroup"}
    ]
    data = {
        'workspace_buttons': workspace_buttons,
        'tasks': tasks,
        'members': members,
        'count': count,
        'selfuser': user,
        'team': team,
    }
    return render(request, 'index2.html', context=data)


@login_required
def my_group(request):
    username_from_request = f'{request.user.username}'
    group_from_request = f'{request.user.team}'
    user = get_user_model().objects.get(username=username_from_request)
    team = Teams.objects.get(group=group_from_request)
    group_members = get_user_model().objects.filter(team=group_from_request)
    extra_context = {
        'group_members': group_members,
        'user': user,
        'team': team,
    }
    return render(request, 'my_group.html', context=extra_context)


@login_required
def user_profile(request, user_id):
    profile = get_user_model().objects.get(nickname=user_id)
    if request.user.nickname == profile.nickname:
        edit_buttons = [
            {'link': '/editprofile', 'name': 'Edit Profile'}
        ]
    else:
        edit_buttons = []

    extra_context = {
        'profile': profile,
        'user_nickname': request.user.nickname,
        'edit_buttons': edit_buttons,
    }
    return render(request, 'user_profile.html', context=extra_context)

@login_required
def make_task(request):
    group_id = f'{request.user.team}'

    if request.method == 'POST':
        form = MakeTask(request.POST, group_id=group_id)
        if form.is_valid():
            query = form.save(commit=False)
            query.group_id = group_id
            query.save()
            return redirect('workspace:workspace')

    else:
        form = MakeTask(group_id=group_id)

    return render(request, 'make_task.html', context={'form': form})
