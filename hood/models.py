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


class Hood(models.Model):
    name = models.CharField(max_length=90)
    location = models.CharField(max_length=90)
    count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save

    def delete_hood(self):
        self.delete

    @classmethod
    def get_hood(cls):
        hood = cls.objects.all()
        return hood

    @classmethod
    def find_hood(cls, hood_id):
        query = cls.objects.filter(user__name__icontains=hood_id)
        return query

    @classmethod
    def update_hood(cls):
        hoody = cls.objects.all()
        return hoody

    @classmethod
    def update_count(cls):
        count = cls.objects.all()
        return count


class Business(models.Model):
    name = models.CharField(max_length=90)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save

    def delete_business(self):
        self.delete

    @classmethod
    def get_business(self):
        business = Business.objects.all()
        return business

    @classmethod
    def searched_business(cls, search_term):
        biz = cls.objects.filter(user__username__icontains=search_term)
        return biz

    @classmethod
    def update_business(cls):
        update = cls.objects.all()
        return update
