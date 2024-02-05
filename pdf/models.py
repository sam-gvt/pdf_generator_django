from django.db import models




class Profile(models.Model):

    job_seek = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.TextField(max_length=200)
    school = models.TextField(max_length=200)
    university = models.TextField(max_length=200)
    previous_work = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    interests = models.TextField(max_length=1000)

    def skills_as_list(self):
        return self.skills.split(';')
    def previous_work_as_list(self):
        return self.previous_work.split(';')
    def interests_as_list(self):
        return self.interests.split(';')
