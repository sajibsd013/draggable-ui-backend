from django.db import models
from django.utils.timezone import now
from users.models import MyUser

class CV(models.Model):
    cv = models.TextField()
    user = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, related_name='cv')
    created_date = models.DateTimeField(default=now, editable=False)
    class Meta:
        verbose_name_plural = "CV"
        db_table = "cv"


