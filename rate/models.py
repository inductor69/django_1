
from django.db import models
from django.db.models import Manager

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=9,unique=True,primary_key=True)
    department=models.CharField(max_length=50, blank=True,null=True)
    user_photo=models.CharField(max_length=50, blank=True,null=True)
    user_rating=models.IntegerField(default=0)
    is_blocked=models.BooleanField(default=False)
    block_date=models.DateTimeField(blank=True,null=True)

    objects=Manager()


class Courses(models.Model):
    course_id=models.CharField(max_length=6)
    course_description=models.CharField(max_length=200)
    course_department=models.CharField(max_length=50)
    

    def __str__(self):
        return(self.course_id)

class Professors(models.Model):
    prof_name=models.CharField(max_length=50)
    prof_deparment=models.CharField(max_length=50)
    prof_research_interest=models.CharField(max_length=50,blank=True)
    img_src=models.CharField(max_length=100,blank=True,default='')
    website=models.CharField(max_length=100,blank=True,default="")

    def __str__(self):
        return(self.prof_name)



   



    

class CourseRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='course_urate')
    course_own=models.ForeignKey(Courses, on_delete=models.CASCADE,related_name="course_r")
    course_difficulty_own=models.IntegerField()
    course_workload_own=models.IntegerField()
    course_content_rating_own=models.IntegerField()
    

class ProfRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='prof_urate')
    prof_own=models.ForeignKey(Professors, on_delete=models.CASCADE,related_name="prof_r")
    prof_puntuality_own=models.IntegerField()
    prof_grading_own=models.IntegerField()
    prof_strictness_rating_own=models.IntegerField()
    prof_teaching_skill_own=models.IntegerField()
    prof_enthusiasm_own=models.IntegerField()
    prof_overall_own=models.IntegerField()
    
class ProfReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='prof_urev')
    prof_own=models.ForeignKey(Professors, on_delete=models.CASCADE,)
    prof_review_own=models.CharField(blank=True,max_length=200)
    prof_review_reiability=models.IntegerField(default=0)
    anonymous=models.BooleanField(default=False)

class CourseReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='course_urev')
    course_own=models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_review_own=models.CharField(blank=True,max_length=200)
    course_review_reiability=models.IntegerField(default=0)
    anonymous=models.BooleanField(default=False)

class Prof_to_subj(models.Model):
    professor=models.ForeignKey(Professors, on_delete=models.CASCADE)
    subject=models.ForeignKey(Courses, on_delete=models.CASCADE)
    rating_of_subj=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.professor.prof_name + " teaches " + self.subject.course_id 

class Complaints(models.Model):
    user = models.ForeignKey(User, related_name='sample1',on_delete=models.CASCADE)
    user_to_be_reported = models.ForeignKey(User, related_name='sample2',on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    review_id=models.CharField(max_length=12,blank=True,null=True)

class Liker(models.Model):
    post = models.ForeignKey(CourseReview,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Forum_message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_by')
    text=models.CharField(max_length=200)
    post_date=models.DateTimeField()