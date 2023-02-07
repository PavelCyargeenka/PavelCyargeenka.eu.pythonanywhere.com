# Generated by Django 4.1.2 on 2022-11-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0009_member_origin_band_member_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='member_origin',
        ),
        migrations.RemoveField(
            model_name='discography',
            name='labels',
        ),
        migrations.RemoveField(
            model_name='discography',
            name='vocals',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='line_up',
        ),
        migrations.AddField(
            model_name='mark',
            name='bass',
            field=models.CharField(choices=[('RE', 'Rod Evans'), ('IG', 'Ian Gillan'), ('DC', 'David Coverdale'), ('JLT', 'Joe Lynn Turner'), ('RB', 'Ritchie Blackmore'), ('TB', 'Tommy Bolin'), ('JS', 'Joe Satriani'), ('SM', 'Steve Morse'), ('SMB', 'Simon McBride'), ('NS', 'Nick Simper'), ('RG', 'Roger Glover'), ('GH', 'Glenn Hughes'), ('JL', 'Jon Lord'), ('DA', 'Don Airey'), ('IP', 'Ian Paice')], default='RG', max_length=3),
        ),
        migrations.AddField(
            model_name='mark',
            name='drums',
            field=models.CharField(choices=[('RE', 'Rod Evans'), ('IG', 'Ian Gillan'), ('DC', 'David Coverdale'), ('JLT', 'Joe Lynn Turner'), ('RB', 'Ritchie Blackmore'), ('TB', 'Tommy Bolin'), ('JS', 'Joe Satriani'), ('SM', 'Steve Morse'), ('SMB', 'Simon McBride'), ('NS', 'Nick Simper'), ('RG', 'Roger Glover'), ('GH', 'Glenn Hughes'), ('JL', 'Jon Lord'), ('DA', 'Don Airey'), ('IP', 'Ian Paice')], default='IP', max_length=3),
        ),
        migrations.AddField(
            model_name='mark',
            name='guitar',
            field=models.CharField(choices=[('RE', 'Rod Evans'), ('IG', 'Ian Gillan'), ('DC', 'David Coverdale'), ('JLT', 'Joe Lynn Turner'), ('RB', 'Ritchie Blackmore'), ('TB', 'Tommy Bolin'), ('JS', 'Joe Satriani'), ('SM', 'Steve Morse'), ('SMB', 'Simon McBride'), ('NS', 'Nick Simper'), ('RG', 'Roger Glover'), ('GH', 'Glenn Hughes'), ('JL', 'Jon Lord'), ('DA', 'Don Airey'), ('IP', 'Ian Paice')], default='RB', max_length=3),
        ),
        migrations.AddField(
            model_name='mark',
            name='keyboards',
            field=models.CharField(choices=[('RE', 'Rod Evans'), ('IG', 'Ian Gillan'), ('DC', 'David Coverdale'), ('JLT', 'Joe Lynn Turner'), ('RB', 'Ritchie Blackmore'), ('TB', 'Tommy Bolin'), ('JS', 'Joe Satriani'), ('SM', 'Steve Morse'), ('SMB', 'Simon McBride'), ('NS', 'Nick Simper'), ('RG', 'Roger Glover'), ('GH', 'Glenn Hughes'), ('JL', 'Jon Lord'), ('DA', 'Don Airey'), ('IP', 'Ian Paice')], default='JL', max_length=3),
        ),
        migrations.AddField(
            model_name='mark',
            name='vocals',
            field=models.CharField(choices=[('RE', 'Rod Evans'), ('IG', 'Ian Gillan'), ('DC', 'David Coverdale'), ('JLT', 'Joe Lynn Turner'), ('RB', 'Ritchie Blackmore'), ('TB', 'Tommy Bolin'), ('JS', 'Joe Satriani'), ('SM', 'Steve Morse'), ('SMB', 'Simon McBride'), ('NS', 'Nick Simper'), ('RG', 'Roger Glover'), ('GH', 'Glenn Hughes'), ('JL', 'Jon Lord'), ('DA', 'Don Airey'), ('IP', 'Ian Paice')], default='IG', max_length=3),
        ),
        migrations.DeleteModel(
            name='Label',
        ),
        migrations.DeleteModel(
            name='Member_Origin',
        ),
    ]
