from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class Tag(models.Model):
    name = models.CharField(max_length=128)


class Language(models.Model):
    name = CharField(max_length=128)


class Category(models.Model):
    name = CharField(max_length=128)


class Parody(models.Model):
    name = models.CharField(max_length=256)


class Character(models.Model):
    name = models.CharField(max_length=256)


class Artist(models.Model):
    name = models.CharField(max_length=256)


class Group(models.Model):
    name = models.CharField(max_length=256)


class Doujinshi(models.Model):
    nhentai_id = models.IntegerField()
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    upload_date = models.DateTimeField()
    Pages = models.IntegerField()
    is_translated = models.BooleanField(default=False)
    dir_path = models.CharField(max_length=512)
    language = ForeignKey(Language, on_delete=models.PROTECT)
    category = ForeignKey(Category, on_delete=models.PROTECT)


class Parodys(models.Model):
    doujinshi = ForeignKey(Doujinshi, on_delete=models.CASCADE)
    parody = ForeignKey(Parody, on_delete=models.PROTECT)


class Characters(models.Model):
    doujinshi = ForeignKey(Doujinshi, on_delete=models.CASCADE)
    character = ForeignKey(Character, on_delete=models.PROTECT)


class Tags(models.Model):
    doujinshi = ForeignKey(Doujinshi, on_delete=models.CASCADE)
    tag = ForeignKey(Tag, on_delete=models.PROTECT)


class Artists(models.Model):
    doujinshi = ForeignKey(Doujinshi, on_delete=models.CASCADE)
    artist = ForeignKey(Artist, on_delete=models.PROTECT)


class Groups(models.Model):
    doujinshi = ForeignKey(Doujinshi, on_delete=models.CASCADE)
    group = ForeignKey(Group, on_delete=models.PROTECT)
