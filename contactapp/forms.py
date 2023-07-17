from django.forms import ModelForm
from .models import Contact, Booking

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

        def __init__(self, *args, **kwargs):
            super(ModelForm, self).__init__(*args, **kwargs)
            for key, field in self.fields.items():
                field.widget.attrs.update({'class':'form-control'})

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        def __init__(self, *args, **kwargs):
            super(ModelForm, self).__init__(*args, **kwargs)
            for key, field in self.fields.items():
                field.widget.attrs.update({'class':'form-control'})