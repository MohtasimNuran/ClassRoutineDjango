from django.forms import ModelForm, DateInput
from othersApp.models import Holiday


class HolidayForm(ModelForm):
    class Meta:
        model = Holiday
        fields = ['holidayStart_date', 'holidayEnd_date', 'holidayInDays', 'holiday_description']
        widgets = {
            'holidayStart_date': DateInput(attrs={'type': 'date'}),
            'holidayEnd_date': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(HolidayForm, self).__init__(*args, **kwargs)
        self.fields['holidayStart_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['holidayEnd_date'].widget.attrs.update({'class': 'form-control'})
