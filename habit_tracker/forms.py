from django import forms
from habit_tracker.models import User, Habit, Journal
from django.forms import ModelForm
from datetime import datetime

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ['habit', 'goal', 'note']
        labels = {
            'habit': 'NAME YOUR HABIT',
            'goal': 'SET YOUR GOAL',
            'note': 'ADD A NOTE',
        }
        

    def __init__(self, *args, **kwargs):
        super(HabitForm, self).__init__(*args, **kwargs)
        self.fields['habit'].widget.attrs['placeholder'] = 'Workout, Study, Do Yoga, etc...'
        self.fields['goal'].widget.attrs['placeholder'] = 'Times per day'

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['note', 'count','met_goal']        
        
    


    

