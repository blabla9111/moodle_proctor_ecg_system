from django.db import models

class MdlProctorBadResultInfo(models.Model):
    id_transaction = models.CharField(max_length=50)
    curr_time = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'mdl_proctor_bad_result_info'


class MdlProctorEcg(models.Model):
    id_transaction = models.CharField(primary_key=True, max_length=50)
    ecg_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mdl_proctor_ecg'


class MdlProctorEcgCourse(models.Model):
    quiz_id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    proctor_ecg_flag = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'mdl_proctor_ecg_course'


class MdlProctorUser(models.Model):
    user_id = models.BigIntegerField()
    quiz_id = models.BigIntegerField()
    gen_code = models.CharField(primary_key=True, max_length=50)
    id_transaction = models.CharField(max_length=50, blank=True, null=True)
    proctor_flag = models.IntegerField(default=0)
    proctor_result = models.IntegerField(default=0)
    proctor_start_flag = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'mdl_proctor_user'

