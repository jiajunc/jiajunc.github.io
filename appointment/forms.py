from datetime import date

from django import forms
from datetimewidget.widgets import DateTimeWidget

from .models import Prescription, Appointment
from users.models import CustomUser


class AppointmentForm(forms.ModelForm):

    app_doctor = forms.ModelChoiceField(queryset=CustomUser.objects.filter(is_doctor=True))

    class Meta:
        model = Appointment
        fields = ('app_doctor', 'date', 'timeslot',)
        widgets = {
            'date': DateTimeWidget(
                attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
                options={
                    'minView': 2,  # month view
                    'maxView': 3,  # year view
                    'weekStart': 1,
                    'todayHighlight': True,
                    'format': 'yyyy-mm-dd',
                    'daysOfWeekDisabled': [0, 6],
                    'startDate': date.today().strftime('%Y-%m-%d'),
                }),
        }

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
        if day.isoweekday() in (0, 6):
            raise forms.ValidationError('Date should be a workday', code='invalid')

        return day

#
# class PrescriptionForm(forms.ModelForm):
#
#     class Meta:
#         model = Prescription
#         fields = ('pre_patient', 'pre_doctor', 'drug', 'dossage', 'frequency', 'start_date', 'end_date',)
#         widgets = {
#             'start_date': DateTimeWidget(
#                 attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
#                 options={
#                     'minView': 2,  # month view
#                     'maxView': 3,  # year view
#                     'weekStart': 1,
#                     'todayHighlight': True,
#                     'format': 'yyyy-mm-dd',
#                     'daysOfWeekDisabled': [0, 6],
#                     'startDate': date.today().strftime('%Y-%m-%d'),
#                 }),
#             'end_date': DateTimeWidget(
#                 attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
#                 options={
#                     'minView': 2,  # month view
#                     'maxView': 3,  # year view
#                     'weekStart': 1,
#                     'todayHighlight': True,
#                     'format': 'yyyy-mm-dd',
#                     'daysOfWeekDisabled': [0, 6],
#                     'startDate': date.today().strftime('%Y-%m-%d'),
#                 }),
#         }
#
#     def clean_date(self):
#         day = self.cleaned_data['date']
#
#         if day <= date.today():
#             raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
#         if day.isoweekday() in (0, 6):
#             raise forms.ValidationError('Date should be a workday', code='invalid')
#
#         return day

class PrescribeForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = ('drug', 'dossage', 'frequency', 'start_date', 'end_date',)
        widgets = {
            'start_date': DateTimeWidget(
                attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
                options={
                    'minView': 2,  # month view
                    'maxView': 3,  # year view
                    'weekStart': 1,
                    'todayHighlight': True,
                    'format': 'yyyy-mm-dd',
                    'daysOfWeekDisabled': [0, 6],
                    'startDate': date.today().strftime('%Y-%m-%d'),
                }),
            'end_date': DateTimeWidget(
                attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
                options={
                    'minView': 2,  # month view
                    'maxView': 3,  # year view
                    'weekStart': 1,
                    'todayHighlight': True,
                    'format': 'yyyy-mm-dd',
                    'daysOfWeekDisabled': [0, 6],
                    'startDate': date.today().strftime('%Y-%m-%d'),
                }),
        }

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
        if day.isoweekday() in (0, 6):
            raise forms.ValidationError('Date should be a workday', code='invalid')

        return day