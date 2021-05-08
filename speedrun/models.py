from django.db import models
import uuid
import datetime


"""
represents a user:
they just have a name for now
"""
class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

"""
This here represents a speedrun entry in the database

elements:
rid = run id, unique id associate with each run
    note: its generated through uuid4, its something I found online
uid = id of the user that did the run
artifacts = artifacts/vanilla, bool, true for artifacts used, false for vanilla
mithrix = bool whether or not did mithrix or didnt(obliterate)
Difficulty = drizzle, rainstorm, monsoon
"""
class Run(models.Model):
    rid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artifacts = models.BooleanField()
    mithrix = models.BooleanField()
    time = models.TimeField(default=datetime.time(0,0,0))

    class the_difficulties(models.TextChoices):
        drizzle = "drizzle"
        rainstorm = "rainstorm"
        monsoon = "monsoon"

    difficulty = models.CharField(
        max_length=30,
        choices=the_difficulties.choices,
        default=the_difficulties.monsoon,
    )

    class the_characters(models.TextChoices):
        commando = 'commando'
        huntress = 'huntress'
        bandit = 'bandit'
        mult = 'mult'
        engineer = 'engineer'
        artificer = 'artificer'
        mercenary = 'mercenary'
        rex = 'rex'
        loader = 'loader'
        acrid = 'acrid'
        captain = 'captain'

    character = models.CharField(
        max_length=30,
        choices=the_characters.choices,
        default=the_characters.engineer,
    )



    def __str__(self):
        return "Speedrun instance; " + \
               "User=" + str(self.user.name) + "; " + \
               "Time=" + str(self.time)+ "; " + \
               "Character=" + self.character

