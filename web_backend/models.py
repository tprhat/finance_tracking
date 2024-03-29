# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class Transactions(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING, db_column='username', to_field='username')
    transaction = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    transaction_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username.username + ' - ' + str(self.transaction) + ' - ' + self.transaction_name


class UserBudget(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING, db_column='username', to_field='username')
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
