# -*- coding: utf-8 -*-

"""
Setings file for the certificate agent
"""

import json
import os
from logsettings import get_logger_config
from path import path

ROOT_PATH = path(__file__).dirname()
REPO_PATH = ROOT_PATH
ENV_ROOT = REPO_PATH.dirname()
TEMPLATE_DIR = '{0}/template_data'.format(REPO_PATH)

# DEFAULTS
DEBUG = False
LOGGING = get_logger_config(ENV_ROOT / "log",
                            logging_env="dev",
                            local_loglevel="DEBUG",
                            dev_env=True,
                            debug=True)

# Default long names, these can be overridden in
# env.json
#  Full list of courses:
#            'BerkeleyX/CS169.1x/2012_Fall',
#            'BerkeleyX/CS169.2x/2012_Fall',
#            'BerkeleyX/CS188.1x/2012_Fall',
#            'BerkeleyX/CS184.1x/2012_Fall',
#            'HarvardX/CS50x/2012',
#            'HarvardX/PH207x/2012_Fall',
#            'MITx/3.091x/2012_Fall',
#            'MITx/6.002x/2012_Fall',
#            'MITx/6.00x/2012_Fall',
#            'BerkeleyX/CS169/fa12',
#            'BerkeleyX/CS188/fa12',
#            'HarvardX/CS50/2012H',
#            'MITx/3.091/MIT_2012_Fall',
#            'MITx/6.00/MIT_2012_Fall',
#            'MITx/6.002x-EE98/2012_Fall_SJSU',
#            'MITx/6.002x-NUM/2012_Fall_NUM']

# What we support:

CERT_DATA = {
  "edX/Open_DemoX/edx_demo_course" : {
    "LONG_ORG" : "Sample Org",
    "LONG_COURSE" : "Sample course",
    "ISSUED_DATE" : "Jan. 1st, 1970"
  },
  "CaltechX/CS1156x/Fall2013" : {
    "LONG_ORG" : "California Institute of Technology",
    "LONG_COURSE" : "Learning From Data",
    "ISSUED_DATE" : "December 9th, 2013",
    "COURSE": "CS1156x",
    "COURSE_ASSOCIATION_TEXT" : "a non-credit course",
    "VERSION": 2
  },
  "University_of_TorontoX/OEE101x/3T2013" : {
    "COURSE" : "OEE101x",
    "ORG" : "University of TorontoX",
    "LONG_ORG" : "University of Toronto",
    "LONG_COURSE" : "Our Energetic Earth",
    "ISSUED_DATE" : "December 16th, 2013",
    "VERSION": 2
  },
}


# Default for the gpg dir
# Specify the CERT_KEY_ID before running the test suite
CERT_GPG_DIR = '{0}/.gnupg'.format(os.environ['HOME'])
CERT_KEY_ID = 'info@edx.org'

# Specify these credentials before running the test suite
CERT_AWS_ID = 'PLEASE_PROVIDE_AN_ID'
CERT_AWS_KEY = 'PLEASE_PROVIDE_AN_AWS_BUCKET_KEY'
CERT_BUCKET = 'provide_a_bucket_name'

# load settings from env.json and auth.json
if os.path.isfile(ENV_ROOT / "env.json"):
    with open(ENV_ROOT / "env.json") as env_file:
        ENV_TOKENS = json.load(env_file)
    LOG_DIR = ENV_TOKENS.get('LOG_DIR', '/var/tmp')
    local_loglevel = ENV_TOKENS.get('LOCAL_LOGLEVEL', 'INFO')
    QUEUE_NAME = ENV_TOKENS.get('QUEUE_NAME', 'test-pull')
    QUEUE_URL = ENV_TOKENS.get('QUEUE_URL', 'https://stage-xqueue.edx.org')
    CERT_GPG_DIR = ENV_TOKENS.get('CERT_GPG_DIR', CERT_GPG_DIR)
    CERT_KEY_ID = ENV_TOKENS.get('CERT_KEY_ID', CERT_KEY_ID)
    CERT_BUCKET = ENV_TOKENS.get('CERT_BUCKET', CERT_BUCKET)
    LOGGING = get_logger_config(LOG_DIR,
                                logging_env=ENV_TOKENS['LOGGING_ENV'],
                                local_loglevel=local_loglevel,
                                debug=False,
                                service_variant=os.environ.get('SERVICE_VARIANT', None))

if os.path.isfile(ENV_ROOT / "auth.json"):
    with open(ENV_ROOT / "auth.json") as env_file:
        ENV_TOKENS = json.load(env_file)
    QUEUE_USER = ENV_TOKENS.get('QUEUE_USER', 'lms')
    QUEUE_PASS = ENV_TOKENS.get('QUEUE_PASS')
    QUEUE_AUTH_USER = ENV_TOKENS.get('QUEUE_AUTH_USER', '')
    QUEUE_AUTH_PASS = ENV_TOKENS.get('QUEUE_AUTH_PASS', '')
    CERT_AWS_KEY = ENV_TOKENS.get('CERT_AWS_KEY', CERT_AWS_KEY)
    CERT_AWS_ID = ENV_TOKENS.get('CERT_AWS_ID', CERT_AWS_ID)
