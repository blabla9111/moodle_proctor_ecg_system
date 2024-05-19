import uuid
from cryptography.fernet import Fernet
from server_with_model.config import *
from server_with_model.model.siames_nn import predict
import datetime


def create_proctor_user(proctor_users, user_id, quiz_id):
    proctor_user = proctor_users.filter(
        user_id=user_id, proctor_flag=0)
    random_uuid = uuid.uuid4()
    if proctor_user:
        # нельзя начинать прокторинг не завершив другой
        if proctor_user.exclude(quiz_id=quiz_id):
            return None
        else:
            proctor_user.update(gen_code=str(random_uuid))
            return proctor_user.get()
    else:
        proctor_user = proctor_users.create(
            user_id=user_id, quiz_id=quiz_id, gen_code=str(random_uuid))
        return proctor_user


def create_proctor_ecg(proctor_users, proctor_ecgs, code):
    proctor_user = proctor_users.filter(gen_code=code, proctor_flag=0)
    if proctor_user:
        transaction_id = str(uuid.uuid4())
        proctor_ecg = proctor_ecgs.create(id_transaction=transaction_id)
        proctor_user.update(id_transaction=transaction_id)
        return proctor_ecg

    else:
        return None


def save_ecg_data(proctor_ecgs, proctor_users, id_transaction, ecg_data):
    f = Fernet(CRYPTO_KEY)
    crypto_ecg_data = f.encrypt(ecg_data.encode()).decode()
    proctor_ecg = proctor_ecgs.filter(id_transaction=id_transaction)
    if proctor_ecg:
        proctor_ecg.update(ecg_data=str(crypto_ecg_data))
        proctor_user = proctor_users.filter(
            id_transaction=id_transaction)
        proctor_user.update(proctor_start_flag=1)
        proctor_user.update(start_time=str(datetime.datetime.now()))
        return proctor_ecg
    else:
        return None


def identify_ecg(proctor_ecgs, proctor_users, bad_results, id_transaction, ecg_data):
    proctor_ecg = proctor_ecgs.filter(
        id_transaction=id_transaction).first()
    proctor_user = proctor_users.filter(
        id_transaction=id_transaction).first()
    if proctor_ecg and proctor_user and proctor_user.proctor_flag == 0:
        f = Fernet(CRYPTO_KEY)
        print(33333)
        ecg_data_db = f.decrypt(proctor_ecg.ecg_data).decode()
        print(111)
        if predict(ecg_1=ecg_data, ecg_2=ecg_data_db):
            return True
        else:
            proctor_user.proctor_result = 1
            proctor_user.save()
            bad_results.create(
                id_transaction=id_transaction, curr_time=str(datetime.datetime.now()))

            return False
    else:
        return None


def close_proctoring(proctor_users, proctor_ecgs, user_id, quiz_id):
    proctor_user = proctor_users.filter(
        user_id=user_id, quiz_id=quiz_id, proctor_flag=0)
    if proctor_user:
        proctor_user = proctor_user.get()
        proctor_user.proctor_flag = 1
        proctor_user.end_time = str(datetime.datetime.now())
        proctor_user.save()
        id_transaction = proctor_user.id_transaction
        proctor_ecgs.filter(id_transaction=id_transaction).delete()
    return proctor_user


def proctor_user_close_desktop(proctor_ecgs, proctor_users, bad_results, id_transaction):
    proctor_ecg = proctor_ecgs.filter(
        id_transaction=id_transaction)
    proctor_user = proctor_users.filter(
        id_transaction=id_transaction)
    # если запись экг есть, а пользователь закрыл приложение, то это значит прокторинг прервался
    if proctor_ecg:
        proctor_user = proctor_user.get()
        proctor_user.proctor_result = 1
        proctor_user.proctor_flag = 1
        proctor_user.save()
        proctor_ecg.delete()
        bad_results.create(
            id_transaction=id_transaction, curr_time=str(datetime.datetime.now()))
        return proctor_user
    return None
