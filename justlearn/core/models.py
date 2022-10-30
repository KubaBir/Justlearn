from email.policy import default

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from pyexpat import model


# Create your models here.
class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and  return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.is_staff:
            return self.email
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    PROFICIENCY_CHOICES = [
        ('JR', 'Junior'),
        ('MD', 'Mid'),
        ('SR', 'Senior')
    ]
    proficiency = models.CharField(
        choices=PROFICIENCY_CHOICES, default='JR', max_length=2)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    github_link = models.URLField(Null = True)
    linkedin_link = models.URLField(Null = True)
    description = models.TextField(max_length = 510)

    def __str__(self):
        return self.user


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Skills connected with proficiency at which they are
    skills = models.ManyToManyField(Skill)
    github_link = models.URLField(Null = True)
    linkedin_link = models.URLField(Null = True)
    description = models.TextField(max_length = 510)
    #jak najlepiej zrobic zeby rating sie updatowal po tym jak ktos wydaje opinie
    rating = models.FloatField(default = 0) 

    def __str__(self):
        return self.user

class Advertisement(models.Model):
    #przy pomocy nested serializera zrobimy zeby w ogloszeniach pojawial sie tez rating, skillset, opis, link do githuba nauczyciela(?).
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    description = models.TextField(max_length = 510)

class Problem(models.Model):
    # tak samo jak wyzej wyswietlimy cos wiecej przy pomocy nested serializera
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    description = models.TextField(max_length = 510)

# Na bazie ofert mozna robic chaty, tak samo na bazie korepetycji
# oferty jak student odpowiada na ogloszenie i jak nauczyciel odpowiada na problem studenta z oferta wspolpracy
class Offer(models.Model):
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, Null = True)
    teacher = models.ForeignKey(Teacher,on_delete = models.DO_NOTHING, Null = True)
    advertisement = models.ForeignKey(Advertisement, on_delete = models.CASCADE, Null = True)
    problem  = models.ForeignKey(Problem, on_delete = models.CASCADE, Null = True )



class Lessons(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.DurationField()
    date = models.DateTimeField()
    meeting_link = models.URLField(Null = True)

class Message(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add = True)

class Chat(models.Model):
    participants = models.ManyToManyField(User)
    messages = models.ManyToManyField(Message, blank = True)