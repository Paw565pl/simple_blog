# Simple Blog

This is an imaginary blog built in Django entirely for educational purposes.

### Live demo

[https://simpleblog-iv6t.onrender.com](https://simpleblog-iv6t.onrender.com)

### How to run it locally?

It is fairly simple thanks to docker. Simply run this command after **cloning the repository**.

```bash
docker compose -f docker-compose.dev.yml up -d --build
```

If you want to seed the database with sample data you can also run this command.

```bash
docker exec -t simple_blog-app-1 python manage.py seed_db
```

That's all! Now simply hit [http://localhost:8000](http://localhost:8000) and explore.
