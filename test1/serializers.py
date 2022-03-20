from rest_framework import serializers
from test1.models import BankAccount, Document, Fund


class BankAccountField(serializers.Serializer):
    account_number = serializers.CharField()
    account_bank = serializers.CharField()


class UpdateFundSerializer(serializers.ModelSerializer):
    bank_accounts = BankAccountField(many=True)

    class Meta:
        model = Fund
        fields = ["name", "doc_fund_registration", "doc_etc", "bank_accounts"]

    def update(self, instance, validated_data):
        instance.bank_accounts.all().delete()  # fund와 관계뿐만 아니라 bank_account 자체를 없앤다.
        new_bank_accounts = validated_data.pop("bank_accounts", [])
        for i in new_bank_accounts:
            BankAccount.objects.create(
                fund=instance,
                account_number=i["account_number"],  # 이미 validation check 되었다고 가정
                account_bank=i["account_bank"],
            )

        return super().update(instance, validated_data)
