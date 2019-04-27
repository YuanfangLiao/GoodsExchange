# Generated by Django 2.1.7 on 2019-04-25 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0007_goods_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=200, null=True, verbose_name='留言')),
                ('status', models.IntegerField(choices=[(1, '交易中'), (2, '交易终止'), (3, '交易成功')], verbose_name='交易状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='购买者')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='active',
            field=models.BooleanField(default=True, verbose_name='是否活跃'),
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.Goods', verbose_name='商品'),
        ),
    ]