from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import Wallet, Operation
from .serializers import OperationSerializer


class WalletOperationView(APIView):
    def post(self, request, wallet_id):
        serializer = OperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(id=wallet_id)
            amount = serializer.validated_data["amount"]
            operation_type = serializer.validated_data["operation_type"]

            if operation_type == Operation.DEPOSIT:
                wallet.balance += amount
            elif operation_type == Operation.WITHDRAW:
                if wallet.balance < amount:
                    return Response({"detail": "Insufficient funds"},
                                    status=400)
                wallet.balance -= amount

            wallet.save()
            Operation.objects.create(wallet=wallet,
                                     **serializer.validated_data)

        return Response({"balance": wallet.balance}, status=200)


class WalletBalanceView(APIView):
    def get(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        return Response({"wallet_id": str(wallet.id),
                         "balance": wallet.balance})
