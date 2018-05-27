from django.db import models

# Create your models here.


class GroupExtend(models.Model):
    group = models.OneToOneField(Group)

    def __str__(self):
        return self.group

    def create_group(self):
        self.save

    def delete_group(self):
        self.delete
