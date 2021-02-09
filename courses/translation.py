from modeltranslation.translator import register, TranslationOptions
from .models import Courses

@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
