from modeltranslation.translator import register, TranslationOptions
from .models import Post, Project

@register(Post)
class PostTranslationOptions(TranslationOptions):
  fields = ('title', 'content')

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
  fields = ('name', 'content')