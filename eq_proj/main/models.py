from django.db import models
from django.contrib.auth.models import User

from .utilities import get_timestamp_path

# Create your models here.


class Vendor(models.Model):
    vendor              = models.SlugField()
    vendor_name         = models.CharField(max_length=50)
    vendor_description  = models.TextField()

    def __str__(self):
        return self.vendor_name

class Exam(models.Model):
    vendor              = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE, related_name='entries_exam')
    exam                = models.SlugField()
    exam_name           = models.CharField(max_length=100)
    exam_description    = models.TextField()
    exam_count_show     = models.IntegerField() # Выявляем наиболее популярные экзамены

class Question(models.Model):
    TYPE_VIEW = ( #Необходим если будем делать реализацию прохождения тестирования
        (None, 'Установить тип ответа на вопрос'),
        ('r', 'Выбор одного ответа'),
        ('c', 'Выбор нескольких ответов'),
    )

    exam                        = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE,
                                                    related_name='entries_question')
    # question_id                 = models.IntegerField()
    question_text               = models.TextField()
    type_question = models.CharField(max_length=1, choices=TYPE_VIEW, default='r') #Необходим если будем делать реализацию прохождения тестирования
    question_image              = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')
    question_comments           = models.TextField()
    # question_answer_options     = models.TextField()
    # question_correct_answer     = models.TextField()

class Answer(models.Model):
    question                    = models.ForeignKey(Question, null=True, on_delete=models.CASCADE,
                                                    related_name='entries_answer')
    answer                      = models.TextField()
    is_true                     = models.BooleanField(default=False)


#Для чего эти ордеры нужны?
class Order(models.Model):
    user_link                   = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    exam_link                   = models.ForeignKey(Exam,null=True, on_delete=models.SET_NULL)
    date_created                = models.DateTimeField(auto_now_add=True, null=True)


# Так же если будем yделать реализацию прохождения тестов нужно будет добавить таблицы результатов ответа пользователей.