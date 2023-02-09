from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_youtubevideos_thumbnail_and_more'),
    ]
    operations = [
        migrations.AlterField(
            model_name='youtubevideos',
            name='thumbnail',
            field=models.URLField(),
        ),
    ]