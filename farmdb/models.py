from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm = models.CharField(max_length=80)


class Animal_Group(models.Model):
    animal_group = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Breed(models.Model):
    breed = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    animal_group = models.ForeignKey(Animal_Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = (Animal_Group, Breed)


class Sub_Group(models.Model):
    sub_group = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    animal_group = models.ForeignKey(Animal_Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = (Animal_Group, Sub_Group)


class Origin(models.Model):
    origin = models.CharField(max_length=200)
    active = models.BooleanField


class Animal(models.Model):
    animal_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1)
    birthdate = models.DateField
    mother = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    markings = models.CharField(max_length=200)
    filename = models.FileField
    alive = models.BooleanField
    comments = models.TextField
    animal_group = models.ForeignKey(Animal_Group, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(Sub_Group, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)


class Reason(models.Model):
    reason = models.CharField(max_length=50)
    active = models.BooleanField


class Vet(models.Model):
    care_date = models.DateField(blank=True)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    symptoms = models.TextField(blank=True)
    temperature = models.SmallIntegerField(blank=True)
    care = models.TextField(blank=True)
    weight = models.SmallIntegerField(blank=True)
    vet = models.CharField(max_length=100, blank=True)
    contact = models.IntegerField(blank=True)
    assistants = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)


# Did not add the user stated in the original model. If problems arise, add it

class Medication(models.Model):
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)
    active = models.BooleanField


class meds_given(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    units = models.SmallIntegerField
    units_given = models.FloatField
    vet_id = models.ForeignKey(Vet.pk)


class Egg_Log(models.Model):
    collection_date = models.DateField
    number = models.IntegerField
    comments = models.TextField


class Wormer(models.Model):
    wormer = models.CharField(max_length=100)
    active = models.BooleanField


class Sheep_care(models.Model):
    care_date = models.DateField
    animal_id = models.ForeignKey(Animal.animal_id, on_delete=models.CASCADE)
    eye = models.SmallIntegerField
    body = models.SmallIntegerField
    tail = models.CharField(max_length=6)
    nose = models.CharField(max_length=100)
    coat = models.CharField(max_length=100)
    jaw = models.SmallIntegerField
    wormer = models.CharField(max_length=100)
    wormer_quantity = models.IntegerField
    hoof = models.CharField(max_length=3)
    weight = models.IntegerField
    estimated = models.CharField(max_length=9)
    comments = models.TextField


class Forage(models.Model):
    forage = models.CharField(max_length=100)
    density = models.FloatField
    active = models.BooleanField


class Paddock(models.Model):
    size = models.FloatField
    forage = models.ForeignKey(Forage, on_delete=models.CASCADE)
    active = models.BooleanField


# The move table has been omitted

class Notes(models.Model):
    note_date = models.DateField
    note = models.TextField
    filename = models.FileField(blank=True)
    created_by = models.CharField(max_length=50)


class Destination(models.Model):
    destination = models.CharField(max_length=200)
    active = models.BooleanField


class Sale(models.Model):
    animal_id = models.ForeignKey(Animal.animal_id, unique=True)
    sale_tag = models.CharField(max_length=50)
    destination = models.ForeignKey(Destination.destination, on_delete=models.CASCADE)
    weight = models.SmallIntegerField
    estimated = models.CharField(max_length=9)
    price_lb = models.DecimalField(max_digits=8, decimal_places=2)
    fees = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField


class Slay_House(models.Model):
    slay_house = models.CharField(max_length=200)
    active = models.BooleanField


class Slaughter(models.Model):
    animal_id = models.ForeignKey(Animal.animal_id, unique=True, on_delete=models.CASCADE)
    sale_tag = models.CharField(max_length=50)  # I suspect this should be a foreign key with the table sale
    slay_house = models.ForeignKey(Slay_House, on_delete=models.CASCADE)
    hauler = models.CharField(max_length=200)
    haul_equip = models.CharField(max_length=200)
    slay_date = models.DateField
    weight = models.PositiveSmallIntegerField
    estimated = models.CharField(max_length=9)
    fees = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField


class Other_Dest(models.Model):
    reason = models.CharField(max_length=50)
    active = models.BooleanField


class Other_Reason(models.Model):
    reason = models.CharField(max_length=50)
    active = models.BooleanField


class Other_Remove(models.Model):
    animal_id = models.ForeignKey(Animal.animal_id, on_delete=models.CASCADE, unique=True)
    remove_date = models.DateField
    reason = models.ForeignKey(Other_Reason, on_delete=models.CASCADE)
    destination = models.ForeignKey(Other_Dest, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField
    comments = models.TextField


class Feed_Type(models.Model):
    type = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Feed_Subtype(models.Model):
    type = models.ForeignKey(Feed_Type, on_delete=models.CASCADE)
    subtype = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Feed_Units(models.Model):
    unit = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Vendor(models.Model):
    vendor = models.CharField(max_length=200)
    active = models.BooleanField(default=True)


class Feed_Purchase(models.Model):
    purchase_date = models.DateField
    type = models.ForeignKey(Feed_Type, on_delete=models.CASCADE)
    subtype = models.ForeignKey(Feed_Subtype, on_delete=models.CASCADE)
    animal_group = models.ForeignKey()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    units = models.ForeignKey(Feed_Units, on_delete=models.CASCADE)
    price_unit = models.DecimalField(max_digits=8, decimal_places=2)
    weight_unit = models.DecimalField(max_digits=8, decimal_places=2)


class Task(models.Model):
    task = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Task_Master(models.Model):
    m_id = models.IntegerField
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comments = models.TextField
    animal_group = models.ForeignKey(Animal_Group, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(Sub_Group, on_delete=models.CASCADE)
    workers = models.IntegerField
    minutes = models.IntegerField
    complete = models.BooleanField(default=False)


class Task_Recurring(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField
    comments = models.TextField
    animal_group = models.ForeignKey(Animal_Group, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(Sub_Group, on_delete=models.CASCADE)
    workers = models.IntegerField
    minutes = models.IntegerField
    recur = models.CharField(max_length=15)
