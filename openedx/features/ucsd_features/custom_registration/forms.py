from .models import ExtendedProfile
from django.forms import ModelForm


class ExtendedProfileForm(ModelForm):
    """
    The fields on this form are derived from the ExtendedProfile model
    """
    def __init__(self, *args, **kwargs):
        super(ExtendedProfileForm, self).__init__(*args, **kwargs)

        self.fields['ethnicity'].error_messages = {
            "required": u"Enter your ethnicity.",
        }

        self.fields['age'].error_messages = {
            "required": u"Enter your age.",
        }

        self.fields['gender'].error_messages = {
            "required": u"Enter your gender.",
        }

        self.fields['highest_level_of_education'].error_messages = {
            "required": u"Select your highest level of education.",
        }

        self.fields['resource'].error_messages = {
            "required": u"Please select related option",
        }

    class Meta(object):
        model = ExtendedProfile
        fields = ('gender', 'age', 'ethnicity', 'highest_level_of_education', 'resource')
