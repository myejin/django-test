from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)


class Fund(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    doc_fund_registration = models.ManyToManyField(
        "Document", blank=True, related_name="registration_funds"
    )
    doc_etc = models.ManyToManyField("Document", blank=True, related_name="etc_funds")


class BankAccount(models.Model):
    fund = models.ForeignKey(
        "fund", on_delete=models.CASCADE, related_name="bank_accounts"
    )
    account_number = models.CharField(max_length=255, blank=False, null=False)
    account_bank = models.CharField(max_length=1, choices=[("H", "Hana"), ("K", "KB")])
