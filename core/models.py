from django.db import models

class AccountInvoice(models.Model):
    title=models.CharField(max_length=100)
    student_name=models.CharField(max_length=50)
    s_id=models.IntegerField()
    tax=models.DecimalField(max_digits=5,decimal_places=4)
    s_tax=models.DecimalField(max_digits=5,decimal_places=4)
    ss_tax=models.DecimalField(max_digits=5,decimal_places=4)
    student_title=models.CharField(max_length=100)
    student_location=models.CharField(max_length=100)
    tax=models.DecimalField(max_digits=5,decimal_places=4)
    

    def __str__(self):
        return str(self.student_name)
