from django.db import models
from django.utils.timezone import now
from user.models import User

class CV(models.Model):
    cv = models.TextField()
    user = models.ForeignKey(
        User, verbose_name="User", on_delete=models.CASCADE, related_name='cv')
    created_date = models.DateTimeField(default=now, editable=False)
    class Meta:
        verbose_name_plural = "CV"
        db_table = "cv"


