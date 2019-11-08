
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from habit_tracker.models import User, Habit, Journal
from habit_tracker.forms import HabitForm, JournalForm
# Create your views here.


@login_required
def home_habits(request): 
  user = request.user
  all_habits = Habit.objects.all()
  return render(request, "habit_tracker/home.html", {"all_habits": all_habits, "user": user })


@login_required
def create_habit(request):
 if request.method == 'POST':
   form = HabitForm(request.POST)
   if form.is_valid():
     habit = form.save()
     return redirect(to=home_habits)
 else:
   form = HabitForm()
 return render(request, "habit_tracker/create_habit.html", {"form": form })

@login_required
def create_a_journal(request, pk): 
  habit = Habit.objects.get(pk=pk)
  if request.method =="POST":
    form = JournalForm(request.POST)
    if form.is_valid():
      journal = form.save(commit=False)
      journal.author = request.user
      journal.habit = habit
      journal.save()
      return redirect(to='create_a_journal', pk=pk)
  else:
    form = JournalForm()
    return render(request, "habit_tracker/journal.html", {"habit": habit, "form": form})


