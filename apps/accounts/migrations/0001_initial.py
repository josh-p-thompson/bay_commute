# Generated by Django 3.0 on 2019-12-27 19:14

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
            name='FavoriteStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(choices=[('12TH', '12th St. Oakland City Center'), ('16TH', '16th St. Mission'), ('19TH', '19th St. Oakland'), ('24TH', '24th St. Mission'), ('ANTC', 'Antioch'), ('ASHB', 'Ashby'), ('BALB', 'Balboa Park'), ('BAYF', 'Bay Fair'), ('CAST', 'Castro Valley'), ('CIVC', 'Civic Center/UN Plaza'), ('COLS', 'Coliseum'), ('COLM', 'Colma'), ('CONC', 'Concord'), ('DALY', 'Daly City'), ('DBRK', 'Downtown Berkeley'), ('DUBL', 'Dublin/Pleasanton'), ('PLZA', 'El Cerrito Plaza'), ('DELN', 'El Cerrito del Norte'), ('EMBR', 'Embarcadero'), ('FRMT', 'Fremont'), ('FTVL', 'Fruitvale'), ('GLEN', 'Glen Park'), ('HAYW', 'Hayward'), ('LAFY', 'Lafayette'), ('LAKE', 'Lake Merritt'), ('MCAR', 'MacArthur'), ('MLBR', 'Millbrae'), ('MONT', 'Montgomery St.'), ('NBRK', 'North Berkeley'), ('NCON', 'North Concord/Martinez'), ('ORIN', 'Orinda'), ('PCTR', 'Pittsburg Center'), ('PITT', 'Pittsburg/Bay Point'), ('PHIL', 'Pleasant Hill/Contra Costa Centre'), ('POWL', 'Powell St.'), ('RICH', 'Richmond'), ('ROCK', 'Rockridge'), ('SBRN', 'San Bruno'), ('SFIA', "San Francisco Int'l Airport"), ('SANL', 'San Leandro'), ('SHAY', 'South Hayward'), ('SSAN', 'South San Francisco'), ('UCTY', 'Union City'), ('WCRK', 'Walnut Creek'), ('WARM', 'Warm Springs/South Fremont'), ('WDUB', 'West Dublin/Pleasanton'), ('WOAK', 'West Oakland')], max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'station')},
            },
        ),
    ]
