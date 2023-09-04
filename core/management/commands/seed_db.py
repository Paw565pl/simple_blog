from pathlib import Path
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.db import connection
from core.models import User
from blog.models import Post
import json


class Command(BaseCommand):
    help = "Populates database with fake users and posts."

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Populating database...", ending="\n")

        with open("./data/users.json") as users:
            users = json.load(users)
        with open("./data/posts.json") as posts:
            posts = json.load(posts)

        users = [User(**user, is_active=False) for user in users]
        posts = [
            Post(
                title=post["title"], content=post["content"], author_id=post["user_id"]
            )
            for post in posts
        ]

        User.objects.bulk_create(users)
        Post.objects.bulk_create(posts)

        self.stdout.write("Done!", ending="")
