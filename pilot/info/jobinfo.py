"""
Job specific info provider mainly used to customize Queue, Site, etc data of Information Service
with details fetched directly from Job instance

:author: Alexey Anisenkov
:contact: anisyonk@cern.ch
:date: January 2018
"""

import logging
logger = logging.getLogger(__name__)


class JobInfoProvider(object):
    """
        Job info provider which is used to extract settings specific for given Job
        and overwrite general configuration used by Information Service
    """

    job = None  ## Job instance

    def __init__(self, job):
        self.job = job

    def resolve_schedconf_sources(self):
        """
            Resolve Job specific prioritized list of source names to be used for SchedConfig data load
            :return: prioritized list of source names
        """

        ## FIX ME LATER
        ## quick stub implementation: extract later from jobParams, e.g. from overwriteAGISData..
        ## an example of return data:
        ## return ['AGIS', 'LOCAL', 'CVMFS']
        ##

        return None  ## Not implemented yet

    def resolve_queuedata(self, pandaqueue, **kwargs):
        """
            Resolve Job specific settings for queue data (overwriteAGISData)
            :return: dict of settings for given PandaQueue as a key
        """

        ## TO BE IMPLEMENTED
        return None