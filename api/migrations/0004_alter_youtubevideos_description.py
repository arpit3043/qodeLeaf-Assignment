from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_alter_youtubevideos_thumbnail'),
    ]
    operations = [
        migrations.AlterField(
            model_name='youtubevideos',
            name='description',
            field=models.TextField(default='No description'),
        ),
    ]