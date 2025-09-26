from deepKernel import deepline
import json

def _init():
    global _global_dict
    _global_dict={}

def set_config_path(path):
    data = {
        'func': 'SET_CONFIG_PATH',
        'paras': {
                      'path': path
                      }   
    }
    #print(json.dumps(data))
    return deepline.process(json.dumps(data))

#获取当前层feature数
def get_layer_feature_count(jobName, stepName, layerName):
    data = {
        'func': 'GET_LAYER_FEATURE_COUNT',
        'paras': {'jobName': jobName, 
                  'stepName': stepName, 
                  'layerName': layerName}
    }
    return deepline.process(json.dumps(data))

def get_opened_jobs():
    data = {
        'func': 'GET_OPENED_JOBS'
    }
    #print(json.dumps(data))
    return deepline.process(json.dumps(data))

def open_job(path, job):
    data = {
        'func': 'OPEN_JOB',
        'paras': [{'path': path},
                  {'job': job}]
    }
    # print(json.dumps(data))
    ret = deepline.process(json.dumps(data))
    return ret

def get_matrix(job):
    data = {
        'func': 'GET_MATRIX',
        'paras': {'job': job}
    }
    # print(json.dumps(data))
    return deepline.process(json.dumps(data))

def has_profile(job, step):
    data = {
        'func': 'HAS_PROFILE',
        'paras': {
                    'job': job,
                    'step': step
                      }   
    }
    #print(json.dumps(data))
    return deepline.process(json.dumps(data))

def get_profile_box(job, step):
    data = {
            'func': 'PROFILE_BOX',
            'paras': {'job': job, 
                      'step': step}
    }
    js = json.dumps(data)
    #print(js)
    ret = deepline.process(json.dumps(data))
    return ret