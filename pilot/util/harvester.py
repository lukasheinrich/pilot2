#!/usr/bin/env python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Paul Nilsson, paul.nilsson@cern.ch, 2018

from os import environ
from os.path import join

from pilot.util.filehandling import write_json, touch, remove
from pilot.util.config import config
from pilot.common.exception import FileHandlingFailure

import logging
logger = logging.getLogger(__name__)


def is_harvester_mode(args):
    """
    Determine if the pilot is running in Harvester mode.
    :param args:
    :return:
    """

    if (args.harvester_workdir != '' or args.harvester_datadir != '' or args.harvester_eventstatusdump != '' or
            args.harvester_workerattributes != '') and not args.update_server:
        harvester = True
    elif 'HARVESTER_ID' in environ or 'HARVESTER_WORKER_ID' in environ:
        harvester = True
    else:
        harvester = False

    return harvester


def get_job_request_file_name():
    """
    Return the name of the job request file as defined in the pilot config file.

    :return: job request file name.
    """

    return join(environ['PILOT_HOME'], config.Harvester.job_request_file)


def remove_job_request_file():
    """
    Remove an old job request file when it is no longer needed.

    :return:
    """

    path = get_job_request_file_name()
    if remove(path) == 0:
        logger.info('removed %s' % path)


def request_new_jobs(njobs=1):
    """
    Inform Harvester that the pilot is ready to process new jobs by creating a job request file with the desired
    number of jobs.

    :param njobs: Number of jobs. Default is 1 since on grids and clouds the pilot does not know how many jobs it can
    process before it runs out of time.
    :return:
    """

    path = get_job_request_file_name()
    dictionary = {'nJobs': njobs}

    # write it to file
    try:
        write_json(path, dictionary)
    except FileHandlingFailure:
        raise FileHandlingFailure


def kill_worker():
    """
    Create (touch) a kill_worker file in the pilot launch directory.
    This file will let Harverster know that the pilot has finished.

    :return:
    """

    touch(join(environ['PILOT_HOME'], config.Harvester.kill_worker_file))
