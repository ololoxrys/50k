
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='���������')),
                ('subtitle', models.CharField(max_length=60, verbose_name='������������')),
                ('description', models.CharField(max_length=600, verbose_name='��������')),
                ('price', models.IntegerField(verbose_name='����')),
                ('genre', models.CharField(max_length=60, verbose_name='����')),
                ('author', models.CharField(max_length=40, verbose_name='�����')),
                ('year', models.DateField(verbose_name='��� ������ �����')),
                ('date', models.DateField(auto_now_add=True, verbose_name='���������� ����� �� ����')),
            ],
            options={
                'verbose_name': '������� ������',
                'verbose_name_plural': '������� �������',
            },
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]