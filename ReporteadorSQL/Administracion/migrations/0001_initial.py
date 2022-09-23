# Generated by Django 2.1.15 on 2022-08-31 14:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imhotep_SedesReportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codreg_sede', models.CharField(default='', max_length=30)),
                ('nom_sede', models.CharField(default='', max_length=30)),
                ('codreg_ips', models.CharField(default='', max_length=30)),
                ('direccion', models.CharField(default='', max_length=200)),
                ('telefono', models.CharField(default='', max_length=120)),
                ('departamento', models.CharField(default='', max_length=120)),
                ('municipio', models.CharField(default='', max_length=120)),
                ('zona', models.CharField(default='', max_length=120)),
                ('sede', models.CharField(default='', max_length=120)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mae_GrupoReportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_grupo', models.CharField(max_length=120, unique=True)),
                ('logo', models.CharField(default='', max_length=120)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mae_Reportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_reporte', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.CharField(default='', max_length=500)),
                ('cuerpo_sql', models.TextField(default='', max_length=15000)),
                ('encabezados', models.CharField(default='', max_length=1000)),
                ('usuario_crea', models.CharField(default='', max_length=20)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now)),
                ('excel', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='I', max_length=1)),
                ('pdf', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='I', max_length=1)),
                ('csv', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='I', max_length=1)),
                ('grilla', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='I', max_length=1)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('mae_gruporeportes', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.Mae_GrupoReportes')),
            ],
        ),
        migrations.CreateModel(
            name='Mae_RepParametros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parametro', models.IntegerField()),
                ('parametro_texto', models.CharField(max_length=100)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('mae_reportes', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.Mae_Reportes')),
            ],
        ),
        migrations.CreateModel(
            name='Mae_RepUsuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cod_usuario', models.CharField(max_length=15)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('cod_sede', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='cod_sede', to='Administracion.Imhotep_SedesReportes')),
                ('mae_reportes', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='mae_reportes', to='Administracion.Mae_Reportes')),
            ],
        ),
        migrations.CreateModel(
            name='Mae_SubGrupoReportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_subgrupo', models.CharField(max_length=120, unique=True)),
                ('logo', models.CharField(default='', max_length=120)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('mae_gruporeportes', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.Mae_GrupoReportes')),
            ],
        ),
        migrations.CreateModel(
            name='Mae_TiposCampo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='mae_repparametros',
            name='mae_tiposcampo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.Mae_TiposCampo'),
        ),
        migrations.AddField(
            model_name='mae_reportes',
            name='mae_subgruporeportes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Administracion.Mae_SubGrupoReportes'),
        ),
        migrations.AlterUniqueTogether(
            name='imhotep_sedesreportes',
            unique_together={('codreg_sede', 'nom_sede')},
        ),
        migrations.AlterUniqueTogether(
            name='mae_subgruporeportes',
            unique_together={('mae_gruporeportes', 'nom_subgrupo')},
        ),
        migrations.AlterUniqueTogether(
            name='mae_repusuarios',
            unique_together={('cod_sede', 'mae_reportes', 'cod_usuario')},
        ),
        migrations.AlterUniqueTogether(
            name='mae_repparametros',
            unique_together={('mae_reportes', 'parametro')},
        ),
    ]
