import math
import traceback

from celery import shared_task
from django.utils import timezone

from .apps import JOB_STATUS_PK_MAP
from .constants import JOB_NAME_FUNCTION_REGISTRY, JobStatusEnum
from .models import JobRunMetaDataV2


@shared_task
def _execute_setup_or_context_function(job_metadata:dict, partner_id:int=None):

    records_count = error_info = None

    task_metadata = {
        'job_name': job_metadata['job_name'],
        'job_id': job_metadata['job_id'],
        'job_run_log_id': job_metadata['job_run_log_id'],
        'config': job_metadata['config'],
        'parameters': job_metadata['parameters'],
        'partner_id': partner_id
    }

    # Scheduled Run
    if not job_metadata['trigger_source']:
        if setup_func := JOB_NAME_FUNCTION_REGISTRY[job_metadata['job_name']].get('setup_func'):
            # f(records_to_fetch_count=1000, config={}, **{})
            valid_id_list, error_info = setup_func(
                config=job_metadata['config'],
                records_to_fetch_count = job_metadata['records_to_fetch_count'],
                **job_metadata['parameters']
            )

            if valid_id_list:
                records_count = len(valid_id_list)
                if partner_id:
                    JobRunMetaDataV2.objects.create(
                        created_dtm=timezone.now(),
                        updated_dtm=timezone.now(),
                        job_id=job_metadata['job_id'],
                        job_run_log_id=job_metadata['job_run_log_id'],
                        metadata={
                            'partner_id': partner_id,
                            'eligible_records_count': records_count
                        },
                        status=JOB_STATUS_PK_MAP[JobStatusEnum.SUCCESS.value]
                    )

            else:
                # Error encountered in setup_func, e.g. DB connection error

                if partner_id:
                    # Create an entry in JRMD
                    JobRunMetaDataV2.objects.create(
                        created_dtm=timezone.now(),
                        updated_dtm=timezone.now(),
                        job_id=job_metadata['job_id'],
                        job_run_log_id=job_metadata['job_run_log_id'],
                        metadata={'partner_id': partner_id},
                        error_info=error_info,
                        status=JOB_STATUS_PK_MAP[JobStatusEnum.FAILED.value]
                    )

                return None, error_info

            batch_size = job_metadata['batch_size']
            if batch_size == 1:
                for unique_id in valid_id_list:
                    task_metadata['unique_id'] = unique_id
                    if job_metadata['run_async']:
                        try:
                            _execute_business_logic.apply_async(
                                kwargs={
                                    'task_metadata': task_metadata
                                },
                                queue=job_metadata['task_queue_name']
                            )
                        except:
                            # this will happen only when Redis is down, resulting in connection error
                            JobRunMetaDataV2.objects.create(
                                created_dtm=timezone.now(),
                                updated_dtm=timezone.now(),
                                job_id=job_metadata['job_id'],
                                job_run_log_id=job_metadata['job_run_log_id'],
                                metadata={
                                    'partner_id': partner_id,
                                    'unique_id': unique_id
                                },
                                error_info=traceback.format_exc(),
                                status=JOB_STATUS_PK_MAP[JobStatusEnum.FAILED.value]
                            )

                    else:
                        _execute_business_logic(task_metadata)

            else:
                for idx in range(math.ceil(records_count / batch_size)):
                    start_idx = idx * batch_size
                    end_idx = start_idx + batch_size
                    batch_id_list = valid_id_list[start_idx:end_idx]
                    task_metadata['unique_id_list'] = batch_id_list
                    if job_metadata['run_async']:
                        try:
                            _execute_business_logic.apply_async(
                                kwargs={
                                    'task_metadata': task_metadata
                                },
                                queue=job_metadata['task_queue_name']
                            )
                        except:
                            # this will happen only when Redis is down, resulting in connection error
                            JobRunMetaDataV2.objects.create(
                                created_dtm=timezone.now(),
                                updated_dtm=timezone.now(),
                                job_id=job_metadata['job_id'],
                                job_run_log_id=job_metadata['job_run_log_id'],
                                metadata={
                                    'partner_id': partner_id,
                                    'unique_id_list': batch_id_list
                                },
                                error_info=traceback.format_exc(),
                                status=JOB_STATUS_PK_MAP[JobStatusEnum.FAILED.value]
                            )

                    else:
                        _execute_business_logic(task_metadata)

        else:
            # setup_func is not defined for the job e.g. File upload
            _execute_business_logic(task_metadata)

    # API Invocation
    else:
        _execute_business_logic(task_metadata)

    return records_count, error_info


@shared_task
def _execute_business_logic(task_metadata:dict):

    # task_metadata format ::
    #   job_name
    #   job_id
    #   job_run_log_id
    #   config
    #   parameters
    #   partner_id
    #   unique_id : optional
    #   unique_id_list : optional

    job_run_meta_data_obj = JobRunMetaDataV2(
        created_dtm=timezone.now(),
        job_id=task_metadata['job_id'],
        job_run_log_id=task_metadata['job_run_log_id'],
        status=JOB_STATUS_PK_MAP[JobStatusEnum.SUCCESS.value]
    )

    parameters = {'config': task_metadata['config']}
    if partner_id := task_metadata.get('partner_id'):
        parameters['partner_id'] = partner_id

    context_func = JOB_NAME_FUNCTION_REGISTRY[task_metadata['job_name']]['context_func']
    metadata = {}

    if partner_id := task_metadata['parameters'].get('partner_id'):
        metadata['partner_id'] = partner_id
        parameters['partner_id'] = partner_id

    unique_id_or_id_list = task_metadata.get('unique_id') or task_metadata.get('unique_id_list')

    if unique_id_or_id_list:
        # setup_function is defined
        metadata['unique_id_or_id_list'] = unique_id_or_id_list
        error_info = context_func(unique_id_or_id_list, **parameters)
    else:
        # when setup_function is not defined
        error_info = context_func(**task_metadata['parameters'], **parameters)

    if error_info:
        status = JOB_STATUS_PK_MAP[JobStatusEnum.FAILED.value]
    else:
        status = JOB_STATUS_PK_MAP[JobStatusEnum.SUCCESS.value]


    job_run_meta_data_obj.status = status
    job_run_meta_data_obj.metadata = metadata
    job_run_meta_data_obj.error_info = error_info
    job_run_meta_data_obj.updated_dtm = timezone.now()
    job_run_meta_data_obj.save()
