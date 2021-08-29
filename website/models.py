from django.db import models

# Create your models here.

class Student(models.Model):
    COMING_FROM = (
        ('Adamsu','Adamsu'),
        ('Mpuasu','Mpuasu'),
        ('Bodaa','Bodaa'),
        ('Kofitia','Kofitia'),
        ('Adiokor1','Adiokor1'),
        ('Adiokor2','Adiokor2'),
        ('Zezera','Zezera'),
    )
    INCLASS = (
        ('Nursery','Nursery'),
        ('Pre','Pre'),
        ('KSA','KSA'),
        ('KSB','KSB'),
        ('KSC','KSC'),
    )
    BOOKS = (
        ('one','one'),
        ('four','four')
    )
    full_name = models.CharField(max_length=45, null=True)
    date_of_birth = models.DateField(null=True)
    grade = models.CharField(max_length=20, null=True, choices=INCLASS)
    residence = models.CharField(max_length=45, null=True, choices=COMING_FROM)
    name_of_mother = models.CharField(max_length=45, null=True)
    name_of_father = models.CharField(max_length=45, null=True)
    parents_contact = models.CharField(max_length=10,null=True)
    amount_to_pay = models.FloatField(null=True)
    how_many_books_to_buy = models.CharField(max_length=10,null=True, choices=BOOKS)
    completed_paying_books = models.BooleanField(default=False)
    troll = models.BooleanField(default=False)
    soap = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    student = models.ForeignKey(Student,null=True, on_delete=models.SET_NULL)
    make_payment = models.FloatField(null=True, blank=True)
    book_payment = models.FloatField(null=True, blank=True)
    when_made = models.DateField(auto_now_add=True, null=True)