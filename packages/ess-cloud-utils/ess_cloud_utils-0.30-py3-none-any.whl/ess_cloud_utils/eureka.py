#!/usr/bin/env python
import os
import random
import time

import py_eureka_client.eureka_client as eureka_client
from .host_info_service import *


def host_retry(function, total_tries=5, initial_wait=0.5, backoff_factor=2):
    """calling the decorated function with applying an exponential backoff.

    :param function: function to retry
    :param total_tries: Total tries
    :param initial_wait: Time to first retry
    :param backoff_factor: Backoff multiplier (e.g. value of 2 will double the delay each retry).
    :returns: wrapped function in decorated manner
    """

    def wrapper(*args, **kwargs):
        tries, delay = 0, initial_wait
        while total_tries > tries:
            try:
                # logging.info(f"Got the host {function(*args, **kwargs)} with {tries} retries", extra={"serviceName": "packager"})
                # print(f"got the host {function(*args, **kwargs)}")
                return function(*args, **kwargs)
            except Exception as e:
                tries += 1
                if tries == total_tries:
                    raise
                time.sleep(delay)
                delay *= backoff_factor
                # logging.info(f"Trying to get host. Try #{tries} with delay {delay}, {e}", extra={"serviceName": "packager"})
                # print(f"{e}: trying to retry with delay {delay}")
        # logging.error(f"Can not get the host after {tries} tries", extra={"serviceName": "packager"})

    return wrapper


def get_ip_by_host(host):
    return host


class Eureka:
    def __init__(self, app_name, eureka_server, port, profile=None):

        # Get service ip depending on profile
        if profile == None:
            profile = os.getenv('DEV_PROFILE')
        if profile == 'dev':
            ip = DockerHostInfoService.get_ip()
        elif profile == 'test':
            print("App profile TEST")
            ip = AwsHostInfoService.get_ip()
        elif profile == 'prod':
            ip = AwsHostInfoService.get_ip()
        elif profile == 'localhost':
            ip = 'localhost'
        else:
            ip = LoopBackHostInfoService.get_ip()
        print("Eureka_IP : ", ip)
        # Cheating the eureka library
        eureka_client.netint.get_ip_by_host = get_ip_by_host

        # Register to Eureka server and start to send heartbeat every 30 seconds
        eureka_client.init(eureka_server=eureka_server,
                           app_name=app_name,
                           instance_host=ip,
                           instance_port=port,
                           ha_strategy=eureka_client.HA_STRATEGY_OTHER
                           )

    @staticmethod
    @host_retry
    def get_application_address(application_name: str):
        client = eureka_client.get_client()
        application = client.applications.get_application(application_name)
        random_index = random.randrange(0, len(application.up_instances))
        return application.up_instances[random_index].homePageUrl
