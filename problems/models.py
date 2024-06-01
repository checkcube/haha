from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('지원하지 않는 파일 형식입니다.')

class File(models.Model):
    file = models.FileField(upload_to='problems/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Problem(models.Model):
    subject = models.CharField(max_length=255, default='기타')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    difficulty = models.CharField(max_length=10, choices=[
        ('최하', '최하'),
        ('하', '하'),
        ('중', '중'),
        ('상', '상'),
        ('최상', '최상'),
    ], default='중')
    problem_file = models.ForeignKey(File, related_name='problem_files', on_delete=models.CASCADE, null=True, blank=True)
    answer_file = models.ForeignKey(File, related_name='answer_files', on_delete=models.CASCADE, null=True, blank=True)
    answer = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title
