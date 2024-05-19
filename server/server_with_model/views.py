from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server_with_model.requstParserJson import *
from server_with_model.services import *
from server_with_model.models import *
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def take_code(request):
    requestParser = RequestParserJson(request=request, json_start_flag=True)
    user_id = requestParser.get_user_id()
    quiz_id = requestParser.get_quiz_id()
    proctor_user = create_proctor_user(
        MdlProctorUser.objects, user_id, quiz_id)
    answer = None
    if (proctor_user):
        answer = proctor_user.gen_code
    return HttpResponse("gen_code: "+str(answer))


@csrf_exempt
def find_code(request):
    requestParser = RequestParserJson(request=request)
    code = requestParser.get_code()
    proctor_ecg = create_proctor_ecg(MdlProctorUser.objects, MdlProctorEcg.objects, code)
    answer = None
    if (proctor_ecg):
        answer = proctor_ecg.id_transaction
    return HttpResponse(answer)


@csrf_exempt
def send_init_ecg(request):
    requestParser = RequestParserJson(request=request)
    id_transaction = requestParser.get_transaction_id()
    ecg_data = requestParser.get_ecg_data()
    proctor_ecg = save_ecg_data(MdlProctorEcg.objects, MdlProctorUser.objects,id_transaction, ecg_data)
    answer = False
    if (proctor_ecg):
        answer = True
    return HttpResponse(answer)


@csrf_exempt
def check_ecg(request):
    requestParser = RequestParserJson(request=request)
    id_transaction = requestParser.get_transaction_id()
    ecg_data = requestParser.get_ecg_data()
    is_same = identify_ecg(MdlProctorEcg.objects, MdlProctorUser.objects,
                           MdlProctorBadResultInfo.objects, id_transaction, ecg_data)
    if is_same==None:
        is_same = "602"
    return HttpResponse(is_same)


@csrf_exempt
def close_check_ecg(request):
    requestParser = RequestParserJson(request=request, json_start_flag=True)
    user_id = requestParser.get_user_id()
    quiz_id = requestParser.get_quiz_id()
    proctor_user = close_proctoring(MdlProctorUser.objects,MdlProctorEcg.objects,user_id, quiz_id)
    answer = False
    if proctor_user:
        answer = True
    return HttpResponse(answer)


@csrf_exempt
def close_desktop(request):
    requestParser = RequestParserJson(request=request)
    id_transaction = requestParser.get_transaction_id()
    proctor_user_close_desktop(
        MdlProctorEcg.objects, MdlProctorUser.objects, MdlProctorBadResultInfo.objects, id_transaction)
    answer = False
    return HttpResponse(answer)
