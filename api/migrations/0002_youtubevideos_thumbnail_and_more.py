from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='youtubevideos',
            name='thumbnail',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='youtubevideos',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='youtubevideos',
            name='title',
            field=models.TextField(),
        ),
    ]