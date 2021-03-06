from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class SessionLog(models.Model):
    session_id = models.CharField(max_length=255)
    users = ArrayField(models.CharField(max_length=255), default=list)
    admin = models.CharField(max_length=255, null=True)


class ActivityLog(models.Model):
    session_id = models.ForeignKey(SessionLog, on_delete=models.CASCADE)

    answered_right = ArrayField(models.CharField(max_length=255), default=list)
    no_answer = ArrayField(models.CharField(max_length=255), default=list)
    answered_wrong = ArrayField(models.CharField(max_length=255), default=list)

    question = models.ForeignKey("Question", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("activitylog")
        verbose_name_plural = _("activitylogs")

    def __str__(self):
        return self.session_id.session_id + "_" + self.question.content

    def get_absolute_url(self):
        return reverse("activitylog_detail", kwargs={"pk": self.pk})


class Question(models.Model):
    content = models.CharField(max_length=255)
    right_answer = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})


class CustomQuestion(models.Model):
    session_id = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)


class CustomQuestionLog(models.Model):
    session_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)

    custom_question = models.ForeignKey("CustomQuestion", on_delete=models.CASCADE)


class Log(models.Model):
    """Log in teacher's log view"""

    session_id = models.ForeignKey(SessionLog, on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    student = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("log")
        verbose_name_plural = _("logs")

    def __str__(self):
        return f"{self.action}-{self.text}"

    def get_absolute_url(self):
        return reverse("log_detail", kwargs={"pk": self.pk})
