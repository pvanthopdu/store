# Generated by Django 2.1.2 on 2019-03-26 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50, verbose_name='Tên kho chi nhánh')),
                ('branch_address', models.TextField(verbose_name='Địa chỉ kho chi nhánh')),
                ('branch_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_admin', to=settings.AUTH_USER_MODEL, verbose_name='Nhân viên quản trị chi nhánh')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('good_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Mã hàng hóa')),
                ('good_name', models.TextField(verbose_name='Tên vật tư')),
                ('good_unit', models.TextField(choices=[('Cái', 'Cái'), ('Bộ', 'Bộ'), ('Thùng', 'Thùng'), ('Hộp', 'Hộp'), ('Gói', 'Gói'), ('kg', 'kg'), ('Mét', 'Mét')], verbose_name='Đơn vị tính')),
                ('good_manufacturing', models.CharField(max_length=50, verbose_name='Nơi sản xuất')),
                ('good_status', models.TextField(choices=[('new', 'Hàng mới'), ('old', 'Hàng đã qua sử dụng')], verbose_name='Tình trạng vật tư')),
                ('good_price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='History_deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_deal', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian giao dịch')),
                ('amount', models.PositiveSmallIntegerField(default=0, verbose_name='Số lượng')),
                ('tyles', models.PositiveSmallIntegerField(choices=[(0, 'Nhập kho'), (1, 'Xuất cấp'), (2, 'Bán')], verbose_name='Chọn loại giao dịch')),
                ('status', models.BooleanField(default=False, help_text='Nếu chọn giao dịch sẽ thực hiện, ngược lại giao dịch không thực hiện', verbose_name='Kích hoạt giao dịch')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_dien.Goods', verbose_name='Chọn vật tư')),
                ('ware_des', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ware_des', to='store_dien.Branch', verbose_name='Chọn kho đích')),
                ('ware_source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ware_source', to='store_dien.Branch', verbose_name='chọn kho nguồn')),
            ],
        ),
        migrations.CreateModel(
            name='warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1, verbose_name='Số lượng')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_dien.Goods', verbose_name='Vật tư')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_dien.Branch', verbose_name='Kho lưu trữ')),
            ],
        ),
    ]
