from django.db import models
from django.core.validators import RegexValidator
import datetime
import calendar
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

YEAR_CHOICES = [(r, r) for r in range(1950, datetime.date.today().year + 1)]
MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]


class Owner(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    second_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    freelance = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    skype = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    about1 = models.TextField(max_length=5000, blank=True, null=True)
    about2 = models.TextField(max_length=5000, blank=True, null=True)
    about3 = models.TextField(max_length=5000, blank=True, null=True)
    profile_image = models.ImageField(upload_to='MainApp/static/img/owner')
    background_image = models.ImageField(upload_to='MainApp/static/img/owner')
    favicon = models.ImageField(upload_to='MainApp/static/img/owner')
    resume_summary = models.TextField(max_length=5000, blank=True, null=True)

    @property
    def age(self):
        return int((datetime.datetime.now().date() - self.birthday).days / 365.25)

    @property
    def full_name(self):
        return self.first_name + '-' + self.second_name + " " + self.last_name

    @property
    def formatted_phone(self):
        return "(" + self.phone[0:3] + ")" + " " + self.phone[3:6] + " " + self.phone[6:9] + " " + self.phone[9:12]

    def save(self, *args, **kwargs):
        try:
            if self.id is not None:
                this = Owner.objects.get(id=self.id)
                if this.profile_image != self.profile_image:
                    this.profile_image.delete(save=False)
                if this.background_image != self.background_image:
                    this.background_image.delete(save=False)
                if this.favicon != self.favicon:
                    this.favicon.delete(save=False)
        finally:
            pass
        super().save(*args, **kwargs)


class Education(models.Model):
    TYPE_CHOICES = (
        ('HIGHSCHOOL', 'High school Diploma'),
        ('BACHELOR', 'Bachelor\'s Degree'),
        ('MASTER', 'Master\'s Degree'),
        ('DOCTORAL', 'Doctoral Degree'),
    )

    university = models.CharField(max_length=200, blank=True, null=True)
    website_university = models.URLField(blank=True, null=True)
    faculty = models.CharField(max_length=200, blank=True, null=True)
    website_faculty = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=18, choices=TYPE_CHOICES, default='BACHELOR')
    program = models.CharField(max_length=200, blank=True, null=True)
    year_start = models.IntegerField(_('start year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_end = models.IntegerField(_('end year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    description = models.TextField(max_length=10000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)


class Experience(models.Model):
    position = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    year_start = models.IntegerField(_('start year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month_start = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    is_current_job = models.BooleanField()
    year_end = models.IntegerField(_('end year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month_end = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    description = models.TextField(max_length=10000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    @property
    def lines_of_description(self):
        return self.description.splitlines()


class Volunteering(models.Model):
    position = models.CharField(max_length=200, blank=True, null=True)
    organisation = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    year_start = models.IntegerField(_('year start'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month_start = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    year_end = models.IntegerField(_('year end'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month_end = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    description = models.TextField(max_length=10000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    @property
    def lines_of_description(self):
        return self.description.splitlines()


class Tool(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    is_visible = models.BooleanField(default=True)


class SoftSkill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='MainApp/static/img/softSkills')
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            if self.id is not None:
                this = SoftSkill.objects.get(id=self.id)
                if this.logo != self.logo:
                    this.logo.delete(save=False)
        finally:
            pass
        super().save(*args, **kwargs)


class MainSkill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='MainApp/static/img/mainskills')
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            if self.id is not None:
                this = MainSkill.objects.get(id=self.id)
                if this.logo != self.logo:
                    this.logo.delete(save=False)
        finally:
            pass
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)
    is_visible = models.BooleanField(default=True)


class ProgrammingSkill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='MainApp/static/img/programming_logo')
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            if self.id is not None:
                this = ProgrammingSkill.objects.get(id=self.id)
                if this.logo != self.logo:
                    this.logo.delete(save=False)
        finally:
            pass
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='MainApp/static/img/testimonials')
    position = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            if self.id is not None:
                this = Testimonial.objects.get(id=self.id)
                if this.image != self.image:
                    this.image.delete(save=False)
        finally:
            pass
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    image = models.ImageField(upload_to='MainApp/static/img/portofolio')

    def save(self, *args, **kwargs):
        try:
            if self.id is not None:
                this = Testimonial.objects.get(id=self.id)
                if this.image != self.image:
                    this.image.delete(save=False)
        finally:
            pass
        super().save(*args, **kwargs)
