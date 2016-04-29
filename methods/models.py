from django.contrib.auth.models import User
from django.db import models


SHORT_TEXT_LEN = 1000


class Article(models.Model):
    name_methods = models.TextField()
    path_module = models.TextField()
    lineno = models.TextField()

    def __str__(self):
        return self.name_methods

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text