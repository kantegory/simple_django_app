from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()


class Auto(models.Model):
    manufacture = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gov_number = models.CharField(max_length=30)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class OwnerLicense(models.Model):
    LICENSE_TYPES = [
        ('A', 'LICENSE_A'),
        ('B', 'LICENSE_B'),
        ('C', 'LICENSE_C')
    ]

    license_number = models.CharField(max_length=30)
    issuing_date = models.DateField()
    license_type = models.CharField(choices=LICENSE_TYPES, default='A', max_length=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

