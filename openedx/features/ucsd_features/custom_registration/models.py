from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtendedProfile(models.Model):
    """
    This model contains extra user profile fields that will be saved when a user registers.
    """

    user = models.OneToOneField(USER_MODEL, null=True)
    DECLINE_TO_STATE_OPTION = ('decline_to_state', 'Decline To State')

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-Binary'),
        DECLINE_TO_STATE_OPTION,
    )
    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_CHOICES,
        max_length=200,
    )

    AGE_CHOICES = (
        ('13_to_17_years', '13-17 years old'),
        ('18_to_22_years', '18 - 22 years old'),
        ('23_to_29_years', '23 - 29 years old'),
        ('30_to_49_years', '30 - 49 years old'),
        ('50_above_years old', '50 + years old'),
        DECLINE_TO_STATE_OPTION,
    )
    age = models.CharField(
        verbose_name="Age",
        choices=AGE_CHOICES,
        max_length=200,
    )

    ETHNICITY_CHOICES = (
        ('african_american_and_black', 'African American and black'),
        ('american_indian_or_alaska_native', 'American Indian / Alaska Native'),
        ('asian', 'Asian'),
        ('hispanic_or_latinx', 'Hispanic / Latinx'),
        ('native_hawaiian_and_pacific_islander', 'Native Hawaiian and Pacific Islander'),
        ('south_asian_or_north_african', 'Southwest Asia / North African'),
        ('white', 'White'),
        DECLINE_TO_STATE_OPTION,
    )
    ethnicity = models.CharField(
        verbose_name="Ethncity",
        choices=ETHNICITY_CHOICES,
        max_length=200,
    )

    EDUCATION_LEVEL_CHOICES = (
        ('graduate', 'Graduate'),
        ('un_graduate', 'Undergraduate'),
        ('high_school', 'Up to High School'),
        DECLINE_TO_STATE_OPTION,
    )
    highest_level_of_education = models.CharField(
        verbose_name="Highest level of education completed",
        choices=EDUCATION_LEVEL_CHOICES,
        max_length=200,
    )

    RESOURCE_CHOICES = (
        ('13_to_17_years', 'Social Media'),
        ('18_to_22_years', 'Email'),
        ('23_to_29_years', 'Word-of-Mouth'),
        ('30_to_49_years', 'Print Advertisemen'),
        ('50_above_years old', 'Other'),
    )
    resource = models.CharField(
        verbose_name="How did you hear about UC San Diego _Online_?",
        choices=RESOURCE_CHOICES,
        max_length=200,
        blank=True,
        null=True
    )
