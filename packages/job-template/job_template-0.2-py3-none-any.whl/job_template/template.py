import uuid

from django.utils import timezone

from .apps import JOB_STATUS_PK_MAP
from .constants import JobStatusEnum
from .models import PeriodicJobRunLog
from .utils import _process_task


class JobTemplate:

    def __init__(self, *, job_config:dict, partner_id_list:list[int]=None, **kwargs:dict):
        self.config = job_config.pop('config')
        self.config['partner_config_map'] = job_config.pop('partner_config_map')
        self.job_metadata = job_config
        self.job_metadata['parameters'] = kwargs
        self.job_metadata['partner_id_list'] = partner_id_list
        self.job_parameters = {
            'parameters': kwargs,
            'partner_id_list': partner_id_list,
            'active_partner_id_list': list(self.config['partner_config_map'].keys())
        }

    def execute_job(self):
        self.job_metadata['job_run_log_id'] = uuid.uuid4().hex
        is_scheduled_run = not self.job_metadata['trigger_source']

        # We won't be able to handle job invocation using API, since in that scenario is_scheduled_run will evaluate
        # to True and both setup & context function will be invoked. But by looking at PJRL, we won't be able to
        # decide how the job executed before its schedule. Hence for API invocation, trigger_source and pk_list needs
        # to be passed all the time.
        if is_scheduled_run:
            periodic_job_run_log_obj = PeriodicJobRunLog(
                created_dtm=timezone.now(),
                job_id=self.job_metadata['job_id'],
                job_run_log_id=self.job_metadata['job_run_log_id'],
                status=JOB_STATUS_PK_MAP[JobStatusEnum.SUCCESS.value]
            )

        records_count, error_info = _process_task(self.job_metadata, self.config)

        if is_scheduled_run:
            self.job_metadata['eligible_records_count'] = records_count
            if error_info:
                status = JOB_STATUS_PK_MAP[JobStatusEnum.FAILED.value]
            else:
                status = JOB_STATUS_PK_MAP[JobStatusEnum.SUCCESS.value]

            periodic_job_run_log_obj.status = status
            periodic_job_run_log_obj.parameters = self.job_parameters
            periodic_job_run_log_obj.error_info = error_info
            periodic_job_run_log_obj.updated_dtm = timezone.now()
            periodic_job_run_log_obj.save()
