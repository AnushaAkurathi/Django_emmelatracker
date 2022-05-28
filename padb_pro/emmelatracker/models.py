from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Team(models.Model):
    # id = models.BigIntegerField(blank=True, primary_key=True)
        
    member_id = models.IntegerField(null=True)
    member = models.EmailField(max_length=255, blank=True)
    member_firstname = models.EmailField(max_length=255, blank=True)
    member_lastname = models.EmailField(max_length=255, blank=True)

    class Meta:
        db_table = 'team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return str(self.member_id)

class Attendance(models.Model):
   id_choices = (('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('None', 'None'))
   ids = models.CharField(max_length = 20, choices = id_choices, default = 'None')
   reason = models.CharField(max_length=200, default = 'None')
   details = models.CharField(max_length=200, default = 'None')
   leave_for = models.FloatField(default = 'None')
   type_choices = (('Present', 'Present'), ('WFH','WFH'), ('Leave', 'Leave'), ('Break', 'Break'), ('None', 'None'))
   typ_e = models.CharField(max_length = 20, choices = type_choices, default = 'None')
   date =  models.DateField(default=now)
   created_at = models.DateTimeField(default = now, blank=True)
   b_choices = (('1 Hrs', '1 Hrs'), ('2 Hrs', '2 Hrs'), ('None', 'None'))
   brea_k = models.CharField(max_length = 20, choices = b_choices, default = 'None')
 
   class Meta:
       db_table = 'attendance'
       unique_together = ('ids','date')
       verbose_name_plural = 'Attendence'
 
   def __str__(self):
       return self.ids



class Announcements(models.Model):
    info = models.CharField(max_length=500, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    # timestamp = models.DateTimeField(default = now, blank=True) 

    class Meta:
        # ordering = ['-created_on']
        db_table = 'announcements'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return self.info


class Bonus(models.Model):
    item_type = models.CharField(max_length=200)
    item = models.CharField(max_length=300)
    bonus = models.FloatField(default = '0')
    member_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(default = now)


    class Meta:
        db_table = 'bonus'
        verbose_name_plural = 'Bonus'

    def __str__(self):
        return self.member_id


class Tasks(models.Model):
    client_no = models.IntegerField(default='0')
    project_id = models.IntegerField(default='0')
    task = models.CharField(max_length=400)
    assigned_by = models.IntegerField(default='0')
    assigned_to = models.IntegerField(default='0')
    created_at=  models.DateTimeField(default = now)
    instructions = models.TextField(default= 'None')
    id_choi = (('0', '0'), ('1', '1'))
    is_repeat = models.CharField(max_length = 20, choices = id_choi, default = '0')
    repeat_details = models.CharField(max_length=400)
    subtask_id = models.IntegerField(default='null')
    links = models.CharField(max_length = 50, default= 'None')
    is_valid = models.CharField(max_length = 20, choices = id_choi, default = '1')

    # class Meta:
    db_table = 'tasks'
    verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task 


class Worklogs(models.Model):
    task_id = models.IntegerField(default='0')
    details_of_execution = models.TextField()
    id_choiw = (('0', '0'), ('1', '1'))
    is_done = models.CharField(max_length = 20, choices = id_choiw, default = '0')
    is_hold = models.CharField(max_length = 20, choices = id_choiw, default = '0')
    member_id = models.IntegerField(default='0')
    remarks = models.CharField(max_length=400)
    created_at = models.DateTimeField(default = now)
    git_url = models.CharField(max_length = 50, default= 'None')
    gdocs_url = models.CharField(max_length = 50, default= 'None')
    other_links = models.CharField(max_length = 50, default= 'None')
    hours_taken = models.FloatField(default = '0')
    is_valid = models.CharField(max_length = 20, choices = id_choiw, default = '1')
    date = models.DateField(default=now)
    tes_t = models.TextField(default= 'None')
    test_2 = models.TextField(default= 'None')

    class Meta:
        verbose_name_plural = 'Worklogs'
        db_table = 'worklogs'

    def __str__(self):
        return self.details_of_execution
 
 
    def get_absolute_url(self):
       return reverse('worklogswithhtml')


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_director = models.BooleanField(default = False)
    is_producer = models.BooleanField(default = False)

