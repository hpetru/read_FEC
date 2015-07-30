import json

from celeryproj.tasks import dump_filing_sked_celery, dump_committee_sked_celery, dump_candidate_sked_celery
from celery.result import AsyncResult

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render_to_response
from shared_utils.cycle_utils import is_valid_four_digit_string_cycle
from reconciliation.utils.json_helpers import render_to_json, render_to_json_via_template

def get_filing(request, filing_number, sked):
    celery_request = dump_filing_sked_celery.apply_async([sked,filing_number], queue='fast',routing_key="fast")    
    task_id = celery_request.id
    return redirect('/download/build_file/%s/' % task_id)
    
def get_committee(request, cycle, committee_id, sked):
    if not is_valid_four_digit_string_cycle(cycle):
        return None
    celery_request = dump_committee_sked_celery.apply_async([cycle,sked,committee_id], queue='fast',routing_key="fast")
    task_id = celery_request.id
    return redirect('/download/build_file/%s/' % task_id)
    
def get_candidate(request, cycle, candidate_id, sked):
    if not is_valid_four_digit_string_cycle(cycle):
        return None
    celery_request = dump_candidate_sked_celery.apply_async([cycle,sked,candidate_id], queue='fast',routing_key="fast")
    task_id = celery_request.id
    return redirect('/download/build_file/%s/' % task_id)
        
def build_file(request, task_id):
    # this is the page that gets shown while the file is downloading. It polls the status until it's done. 
    
    return render_to_response('downloads/build_file.html',
        {
        'task_id':task_id,
        })
    
def get_task_status(request, task_id):

    result = AsyncResult(task_id)
    return_obj = {}
    if result.state == 'SUCCESS':
        return_obj = {'done':True, 'result':result.result}
    else:
        return_obj = {'done':False, 'result':None}
        
    return render_to_json(json.dumps(return_obj))

