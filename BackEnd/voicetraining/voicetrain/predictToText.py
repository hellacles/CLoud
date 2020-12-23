from .models import Deliveryinfo
from .models import Userinfo
from django.db.models import Q

intent_dict = {0:'운행을 시작합니다', 1:'가게전화', 2:'가게에 도착처리하겠습니다', \
               3:'픽업완료 처리하겠습니다', 4:'주문번호가 일치합니다', \
               5:'소요시간선택', 6:'배달완료 처리하겠습니다', 88: "오류", 99:'다시 말씀해주세요'}

def predictToText(intent, user, orderNum):
    if intent == 99:
        return int(intent), intent_dict[intent], "null", "null", "null", "null", "null", "null" "null", "null"
    elif intent == 0:
        stat = Deliveryinfo.objects.get(id=8)
        stat.username = user
        stat.status = 1
        stat.save()
        userDeliveryStatus = Userinfo.objects.get(username=user)
        userDeliveryStatus.deliverystatus = 1
        userDeliveryStatus.save()
        return int(intent), intent_dict[intent], stat.shopname, stat.destination, stat.fromaddress, float(
            stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(
            stat.deslongitude), stat.receipt
    elif intent == 1:
        stat = Deliveryinfo.objects.filter((Q(username=user)&Q(status=1)) | (Q(username=user)&Q(status=2))).get()
        return int(intent), stat.phone, stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
    elif intent == 2:
        stat = Deliveryinfo.objects.filter(Q(username=user) & Q(status=1)).get()
        userDeliveryStatus = Userinfo.objects.get(username=user)
        if userDeliveryStatus.deliverystatus != 1:
            return 88, "운행을 시작해주세요", stat.shopname, stat.destination, stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
        else:
            userDeliveryStatus.deliverystatus = 2
            userDeliveryStatus.save()
            return int(intent), intent_dict[intent], stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
    elif intent == 3:
        stat = Deliveryinfo.objects.filter(Q(username=user) & Q(status=1)).get()
        userDeliveryStatus = Userinfo.objects.get(username=user)
        if userDeliveryStatus.deliverystatus != 3:
            return 88, "영수증 번호 확인하셨나요?", stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
        else:
            userDeliveryStatus.deliverystatus = 4
            userDeliveryStatus.save()
            stat.status = 2
            stat.save()
            return int(intent), intent_dict[intent], stat.shopname, stat.destination, stat.fromaddress, float(
                stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(
                stat.deslongitude), stat.receipt
    elif intent == 4:
        userDeliveryStatus = Userinfo.objects.get(username=user)
        stat = Deliveryinfo.objects.filter(Q(username=user) & Q(status=1)).get()
        if userDeliveryStatus.deliverystatus != 2:
            return 88, "가게 도착처리해주세요", stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
        else:
            if orderNum == stat.receipt:
                userDeliveryStatus.deliverystatus = 3
                userDeliveryStatus.save()
                return int(intent), intent_dict[intent], stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
            else:
                return 88, "주문번호가 일치하지 않습니다 주문번호는" + str(stat.receipt) + "입니다", stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
    elif intent == 6:
        stat = Deliveryinfo.objects.filter(Q(username=user) & Q(status=2)).get()
        userDeliveryStatus = Userinfo.objects.get(username=user)
        if userDeliveryStatus.deliverystatus != 4:
            return 88, "픽업 완료해주세요", stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
        else:
            userDeliveryStatus.deliverystatus = 0
            userDeliveryStatus.save()
            stat.status = 3
            stat.save()
            return int(intent), intent_dict[intent], stat.shopname, stat.destination, stat.fromaddress, float(stat.fromlatitude), float(stat.fromlongitude), float(stat.deslatitude), float(stat.deslongitude), stat.receipt
