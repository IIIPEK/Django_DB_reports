from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Alert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    report = models.ForeignKey('main.Report', on_delete=models.CASCADE)
    cron = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)


    def __str__(self):
        return self.title