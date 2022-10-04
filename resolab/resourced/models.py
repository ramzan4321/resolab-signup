from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from resolab.users.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from django.utils import timezone
from django.utils.timezone import now as timezone_now

# Create your models here.

class GeneralProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    citizenship = models.CharField(max_length=255, blank=False, null=False)
    location = models.CharField(max_length=255, blank=False, null=False)
    location_state = models.CharField(max_length=255, blank=False, null=False)
    location_district = models.CharField(max_length=255, blank=False, null=False)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    alternate_phone_number = models.CharField(max_length=255, blank=False, null=False)
    is_user_active = models.BooleanField(default=True)
    make_into_as_public = models.TextField(null=True, blank=True)

    # About the organization
    organization_name = models.CharField(max_length=255, blank=False, null=False)
    legal_status = models.CharField(max_length=255, blank=False, null=False)
    select_category =models.CharField(max_length=255, blank=False, null=False)
    
    #Contact Details of Person posting Requirement
    person_name = models.CharField(max_length=255, blank=False, null=False)
    person_designation = models.CharField(max_length=255, blank=False, null=False)
    person_id = models.CharField(max_length=255, blank=False, null=False)
    #person_contact = phone_number
    person_email = models.EmailField()
    #Alternate Person Contact Details
    manager_name =models.CharField(max_length=255, blank=False, null=False)
    manager_designation =models.CharField(max_length=255, blank=False, null=False)
    #manager_contact = alternate_phone_number
    manager_email = models.EmailField()

    class Meta:
       abstract = True

class ResourceProvider(GeneralProfile):
    category_role = models.CharField(max_length=255, blank=False, null=False)
    job_role = models.CharField(max_length=255, blank=False, null=False)
    education_q = models.CharField(max_length=255, blank=False, null=False)
    degree = models.CharField(max_length=255, blank=False, null=False)

    achievements = models.CharField(max_length=255, blank=False, null=False)

    microfinance_exp = models.IntegerField()
    other_exp = models.IntegerField()
    first_Org_exp = models.IntegerField()
    first_desig = models.CharField(max_length=70, blank=False, null=False)
    first_duration = models.CharField(max_length=70, blank=False, null=False)
    second_Org_exp = models.IntegerField()
    second_desig = models.CharField(max_length=70, blank=False, null=False)
    second_duration = models.CharField(max_length=70, blank=False, null=False)
    third_Org_exp = models.IntegerField()
    third_desig = models.CharField(max_length=70, blank=False, null=False)
    third_duration = models.CharField(max_length=70, blank=False, null=False)
    organization_name = None
    legal_status = None
    person_contact = None
    person_designation = None
    person_email = None
    person_name = None
    person_id = None
    manager_contact = None
    manager_designation = None
    manager_email = None
    manager_name = None
    select_category = None


class ResourceSeeker(GeneralProfile):
    #Resource Required Summary
    job_role =models.CharField(max_length=255, blank=False, null=False)
    minimum_qualification =models.CharField(max_length=255, blank=False, null=False)
    preferred_qualification_if_any =models.CharField(max_length=255, blank=False, null=False)
    is_experience_required =models.BooleanField(default=False)
    additional_requirement =models.CharField(max_length=255, blank=False, null=False)
    joining_requirements =models.CharField(max_length=255, blank=False, null=False)

class ResourceSeekerServices(GeneralProfile):
    person_id = None


class ProfessionalOverView(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, blank=False, null=False)
    years_of_experience = models.FloatField()
    industry = models.CharField(max_length=255, blank=False, null=False)
    leadership_experience = models.BooleanField(default=False)
    how_many_years = models.FloatField()
    interested_secondary_positions = models.CharField(max_length=255, blank=True, null=True)

class SkillRanking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_skills_with_experience = models.TextField()
    secondory_skills_with_experience = models.TextField()

class SocialProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.TextField(blank=True, null=True)
    linkdin = models.TextField(blank=True, null=True)
    personal = models.TextField(blank=True, null=True)

    class Meta:
       abstract = True

class AdditionalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, blank=False, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="add_profile")
    profile_pic = models.ImageField(upload_to="profile/", null=True, blank=True)
    date_joined = models.DateTimeField()
    registered_region = models.CharField(max_length=255, blank=False, null=False)
    is_verified = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_job_provider = models.BooleanField(default=False)
    industry = models.CharField(max_length=255, blank=True, null=True)