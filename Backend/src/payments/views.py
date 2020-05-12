from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import (
    Payment,
    BanckPayment,
    DirectPayment
    )

from .serializers import (
    
    # CRUD SERIALIZERS
    PaymentSerializer,
    UpdatePaymentSerializer,
    CreatePaymentSerializer,
    InactivatePaymentSerializer,
    DeletePaymentSerializer,

    BanckPaymentSerializer,
    CreateBanckPaymentSerializer,
    UpdateBanckPaymentSerializer,
    InactivateBanckPaymentSerializer,
    DeleteBanckPaymentSerializer,

    DirectPaymentSerializer,
    CreateDirectPaymentSerializer,
    UpdateDirectPaymentSerializer,
    InactivateDirectPaymentSerializer,
    DeleteDirectPaymentSerializer
    # QUERY SERIALIZERS
)

from .permissions import (
    AllowAdmin,
    AllowManager,
    AllowOperator
)

from rest_framework.views import APIView
from rest_framework.response import Response

# ============================================Views para el modúlo Energy Transfers==========================

#----------------------------------------------------Subestaciones-------------------------------------                                      

#                                                       CRUD


class PaymentCreate(ListCreateAPIView):
    """View para crear una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = CreatePaymentSerializer

class PaymentDetail(RetrieveAPIView):
    """View para retrive una Subestacion""" 
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentUpdate(UpdateAPIView):
    """View para update una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = UpdatePaymentSerializer

class PaymentDelete(DestroyAPIView):
    """View para delete una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = DeletePaymentSerializer

class PaymentInactivate(UpdateAPIView):
    """View para delete una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = InactivatePaymentSerializer

#                                                   QUERY

#------------------------------------------------BanckPayment-------------------------------------

#                                                   CRUD

class BanckPaymentCreate(ListCreateAPIView):
    """View para delete un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = BanckPaymentSerializer

class BanckPaymentDetail(RetrieveAPIView):
    """View para retrive un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = BanckPaymentSerializer

class BanckPaymentList(ListAPIView):
    """View para retrive todos los BanckPayments"""
    queryset = BanckPayment.objects.all()
    serializer_class = BanckPaymentSerializer

class BanckPaymentUpdate(UpdateAPIView):
    """View para update un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = UpdateBanckPaymentSerializer

class BanckPaymentDelete(DestroyAPIView):
    """View para delete un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = DeleteBanckPaymentSerializer

class BanckPaymentInactivate(UpdateAPIView):
    """View para inactivate un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = InactivateBanckPaymentSerializer

#                                               QUERY

#----------------------------------------------DirectPayment------------------------------------------------

#                                               CRUD

class DirectPaymentCreate(ListCreateAPIView):
    """View para delete un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = CreateDirectPaymentSerializer

class DirectPaymentDetail(RetrieveAPIView):
    """View para retrive un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DirectPaymentSerializer

class DirectPaymentList(ListAPIView):
    """View para retrive todos los DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DirectPaymentSerializer

class DirectPaymentUpdate(UpdateAPIView):
    """View para update un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = UpdateDirectPaymentSerializer

class DirectPaymentDelete(DestroyAPIView):
    """View para delete un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DeleteDirectPaymentSerializer

class DirectPaymentInactivate(UpdateAPIView):
    """View para inactivate un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = InactivateDirectPaymentSerializer