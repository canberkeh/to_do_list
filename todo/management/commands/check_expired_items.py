from django.core.management.base import BaseCommand
from todo.models import ToDoListItem
from django.utils import timezone


class Command(BaseCommand): 
    """This command triggers exchane update process"""

    def handle(self, *args, **options):
        """Handle command"""

        ToDoListItem.objects.filter(deadline__lt=timezone.now()).update(
            status=ToDoListItem.ToDoListItemStatus.EXPIRED
        )
