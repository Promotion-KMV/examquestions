from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    vendor_name         = models.CharField(unique=True, max_length=50)
    vendor_slug         = models.SlugField(unique=True,)
    vendor_description  = models.TextField()

    def __str__(self):
        return self.vendor_name

    def get_absolute_url(self):
        return f'exams/{self.vendor_slug}'

class Exam(models.Model):
    vendor              = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL, related_name='entries_exam')
    exam_name           = models.CharField(max_length=100)
    exam_slug           = models.SlugField(unique=True)
    exam_description    = models.TextField(null=True, blank=True)
    exam_comments       = models.TextField(null=True, blank=True)
    exam_count_show     = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.exam_name

    def get_absolute_url(self):
        return f'/{self.vendor_slug}'


class Question(models.Model):
    exam                        = models.ForeignKey(Exam, null=True, on_delete=models.SET_NULL,
                                                    related_name='entries_question')

    question                    = models.TextField(null=True, blank=True)
    question_comments           = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question                    = models.ForeignKey(Question, null=True, on_delete=models.CASCADE,
                                                    related_name='entries_answer')
    answer                      = models.TextField()
    is_true                     = models.BooleanField(default=False)

    def __str__(self):
        return self.answer



class Order(models.Model):
    user_link                   = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    exam_link                   = models.ForeignKey(Exam,null=True, on_delete=models.SET_NULL)
    date_created                = models.DateTimeField(auto_now_add=True, null=True)


