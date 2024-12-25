from django.db import models
from django.urls import reverse

class Appointment(models.Model):
    user = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    contact_number = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.Appointment_name

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class User(models.Model):
    ROLE_CHOICES = (
        ('Student', 'Student'),
        ('Tutor', 'Tutor'),
        ('Admin', 'Admin'),
    )
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    passwordHash = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.role}"


class Subject(models.Model):
    subName = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.subName

class Session(models.Model):
    SESSION_TYPE_CHOICES = (
        ('Online', 'Online'),
        ('In-Person', 'In-Person'),
    )
    student = models.ForeignKey(User, related_name='sessions_as_student', on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, related_name='sessions_as_tutor', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sessionDate = models.DateTimeField()
    sessionType = models.CharField(max_length=10, choices=SESSION_TYPE_CHOICES)
    feedback = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def __str__(self):
        return f"Session {self.id} - {self.student} with {self.tutor}"


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for session {self.session.id}"

class Review(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='reviews_as_student', on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, related_name='reviews_as_tutor', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    review_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Review for session {self.session.id} by {self.student}"
