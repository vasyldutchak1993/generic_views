from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker
from permitions_task.models import Article

class Command(BaseCommand):
    help = "Naplní databázu testovacími používateľmi a článkami"

    def handle(self, *args, **kwargs):
        fake = Faker()
        content_type = ContentType.objects.get_for_model(Article)

        perm_edit = Permission.objects.get(codename='can_edit_article', content_type=content_type)
        perm_delete = Permission.objects.get(codename='can_delete_article', content_type=content_type)

        # Admini
        for i in range(1, 4):
            user = User.objects.create_user(username=f"admin{i}", password="adminpass",is_staff=True,is_superuser=True)
            user.user_permissions.add(perm_edit, perm_delete)
            self.stdout.write(self.style.SUCCESS(f"Admin {user.username} vytvorený."))

        # Bežní používatelia
        for i in range(1, 4):
            user = User.objects.create_user(username=f"user{i}", password="userpass")
            self.stdout.write(self.style.SUCCESS(f"Používateľ {user.username} vytvorený."))

        # Články
        for _ in range(5):
            Article.objects.create(title=fake.sentence(), content=fake.paragraph(nb_sentences=5))
        self.stdout.write(self.style.SUCCESS("5 článkov bolo vytvorených."))
