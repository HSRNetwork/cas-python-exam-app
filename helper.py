import os
import yaml
import napalm
import requests

USER = os.environ.get('cisco_user', 'python')
PASSWORD = os.environ.get('cisco_pw', 'cisco')


def read_yaml(filename):
    # ToDo: read and return yaml file
    pass


def napalm_get_facts(ip):
    driver = napalm.get_network_driver('ios')
    # ToDo: get napalm facts

    return facts

def rest_native_interface(ip):
    headers= {'Accept': 'application/yang-data+json'}
    # ToDo: get cisco native interface information

    return interfaces['Cisco-IOS-XE-native:interface']

def convert_interface_data(data):
    new_interfaces = {}
    # ToDo: create new dic for interfaces with description and IPs
    """
    {
        'GigabitEthernet1': {
            'description': 'RESTful API Interface', 
            'ipv4': '10.3.255.101'}, 
        'Loopback0': {
            'description': 'no description set', 
            'ipv4': '10.10.10.10'}, 
        'Loopback11': {
            'description': 'no description set', 
            'ipv4': '11.11.11.11; 111.111.111.111'}, 
        'Loopback666': {
            'description': 'no description set', 
            'ipv4': 'no ip'}
    }
    """

    return new_interfaces
