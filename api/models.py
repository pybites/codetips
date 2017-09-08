from django.db import models
from django.contrib.auth.models import User

LANGUAGES = """Java Python PHP C# Javascript C++ C R Objective-C
 Swift Matlab Ruby VBA TypeScript Visual Scala Perl Kotlin Go lua
 Rust Haskell Delphi""".split()
LANGUAGE_CHOICES = sorted([(lang.lower(), lang) for lang in LANGUAGES])
DEFAULT_LANGUAGE = "python"

class Tip(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default=DEFAULT_LANGUAGE)
    tip = models.TextField(unique=True)
    published = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='tips', on_delete=models.CASCADE)

    @property
    def twitter_handle(self):
        return self.handle if self.handle.startswith('@') else '@' + self.handle

    class Meta:
        ordering = ('-created', )
