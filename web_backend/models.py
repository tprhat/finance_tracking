# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Transactions(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING, db_column='username', to_field='username')
    transaction = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        db_table = 'transactions'


class UserBudget(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING, db_column='username', to_field='username')
    budget = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 'user_budget'
