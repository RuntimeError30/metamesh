from django.db import models

# Create your models here.
class students(models.Model):
    stu_id = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=260)
    password = models.CharField(max_length=300)
    batch = models.CharField(max_length=10)
    dept = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12, default="")
    active= models.CharField(max_length=20, default="false")
    profpic = models.ImageField(upload_to='images', null=True)
    class Meta:
        db_table = "students"

class posts(models.Model):
    text = models.CharField(max_length=10000)
    student = models.ForeignKey(students, on_delete=models.CASCADE) 
    upvote = models.CharField(max_length=100, null=True, default="0")
    category = models.CharField(max_length=100)
    iid = models.CharField(primary_key=True, max_length=100)
    pictures = models.ImageField(upload_to="posts", null=True)
    class Meta:
        db_table = "posts" 

class likes(models.Model):
    counter = models.CharField(max_length=100, default="0", null=True)
    post = models.ForeignKey(posts, on_delete=models.CASCADE)
    user = models.ForeignKey(students, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, null=True)
    class Meta:
        db_table = 'like'
        unique_together = ('post', 'user')

class notification(models.Model):
    message = models.CharField(max_length=200, default="")
    to = models.ForeignKey(students, on_delete=models.CASCADE)

    class Meta:
        db_table = "notification"

class clubs(models.Model):   
    clubname = models.CharField(max_length=100, primary_key=True)
    clubtype = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200, null=True)
    rules = models.CharField(max_length=200)
    adminname = models.CharField(max_length=100)
    adminid = models.ForeignKey(students, on_delete=models.CASCADE)
    imagee = models.ImageField(upload_to='fimage', null=True)
    class Meta:
        db_table = 'club'

class clubApproval(models.Model):
    clubid = models.ForeignKey(clubs, on_delete=models.CASCADE)
    studentss = models.ForeignKey(students, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="not")
    admin = models.CharField(max_length=100, default="")

    class Meta:
        db_table = "approval"
        unique_together = ('clubid', 'studentss')

class clubpost(models.Model):
    clubidd = models.ForeignKey(clubs, on_delete=models.CASCADE)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    texts = models.CharField(max_length=300, default="")
    iid = models.CharField(max_length=100, primary_key=True)
    upvote = models.CharField(max_length=200, null=True, default="0")
    cimage = models.ImageField(upload_to='cposts', null=True)
    class Meta:
        db_table = "clubpost"

class clublikes(models.Model):
    counter = models.CharField(max_length=100, default="0", null=True)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    club = models.ForeignKey(clubs, on_delete=models.CASCADE)
    post = models.ForeignKey(clubpost, on_delete=models.CASCADE)

    class Meta:
        db_table = "clublikes"

class eevent(models.Model):
    bannerImg = models.ImageField(upload_to='banner', blank=True, default="")
    name = models.CharField(max_length=100, primary_key=True)
    cat = models.CharField(max_length=100)
    club = models.ForeignKey(clubs, on_delete=models.CASCADE)
    admin = models.ForeignKey(students, on_delete=models.CASCADE)
    stime = models.CharField(max_length=20)
    etime = models.CharField(max_length=30)
    details = models.CharField(max_length=400)

    class Meta:
        db_table = "event"

class conversations(models.Model):
    userss = models.ManyToManyField(students)
    created_at = models.DateTimeField(auto_now_add=True)
    pkk = models.CharField(max_length=200, primary_key=True)
    class Meta:
        db_table = "conversations"

class messages(models.Model):
    convs = models.ForeignKey(conversations, on_delete=models.CASCADE)
    sender = models.ForeignKey(students, on_delete=models.CASCADE)
    msg = models.CharField(max_length=300, default="", null=True)

    class Meta:
        db_table = "message"

