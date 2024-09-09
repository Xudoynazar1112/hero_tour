from modeltranslation.translator import register, TranslationOptions
from .models import Travel, Booking


@register(Travel)
class TravelTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Booking)
class BookingTranslationOptions(TranslationOptions):
    fields = ('name', 'tour')
