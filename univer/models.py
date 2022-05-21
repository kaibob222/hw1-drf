from operator import mod
from tabnanny import verbose
from django.db import models


class Student(models.Model):
    last_name = models.CharField('фамилия', max_length=50)
    first_name = models.CharField('имя', max_length=50)
    second_name = models.CharField('отчество', max_length=50, blank=True, default='')
    id_number = models.CharField('номер студбилета', max_length=25)

    def __str__(self):
        res = self.last_name + ' ' + self.first_name[0] + '.'
        if self.second_name:
            res += self.second_name[0] + '.'
        return res

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Course(models.Model):
    code = models.CharField('код', max_length=30)
    name = models.CharField('название', max_length=50)

    def __str__(self):
        return self.code + ' ' + self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.DO_NOTHING, verbose_name='студент')
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING, verbose_name='дисциплина')
    points = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='балл БРС')

    def __str__(self):
        return str(self.course) + ': ' + str(self.student)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
