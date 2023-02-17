from django.db.models.signals import post_delete
from .models import Document
import os

def deleteProjectDocumentFromStorage(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'Document' object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
            
post_delete.connect(deleteProjectDocumentFromStorage, sender=Document)