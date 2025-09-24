# Copyright 2015 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from collections import OrderedDict
import random
import re

from netaddr import ip
from tempest import config
from tempest.lib.common.utils import data_utils
import testtools

from manila_tempest_tests import utils

CONF = config.CONF
SHARE_NETWORK_SUBNETS_MICROVERSION = '2.51'
SHARE_REPLICA_QUOTAS_MICROVERSION = "2.53"
EXPERIMENTAL = {'X-OpenStack-Manila-API-Experimental': 'True'}


def deduplicate(items):
    """De-duplicate a list of items while preserving the order.

    It is useful when passing a list of items to ddt.data, in order
    to remove duplicated elements which may be specified as constants.
    """
    return list(OrderedDict.fromkeys(items))


def get_microversion_as_tuple(microversion_str):
    """Transforms string-like microversion to two-value tuple of integers.

    Tuple of integers useful for microversion comparisons.
    """
    regex = r"^([1-9]\d*)\.([1-9]\d*|0)$"
    match = re.match(regex, microversion_str)
    if not match:
        raise ValueError(
            "Microversion does not fit template 'x.y' - %s" % microversion_str)
    return int(match.group(1)), int(match.group(2))


def is_microversion_gt(left, right):
    """Is microversion for left is greater than the right one."""
    return get_microversion_as_tuple(left) > get_microversion_as_tuple(right)


def is_microversion_ge(left, right):
    """Is microversion for left is greater than or equal to the right one."""
    return get_microversion_as_tuple(left) >= get_microversion_as_tuple(right)


def is_microversion_eq(left, right):
    """Is microversion for left is equal to the right one."""
    return get_microversion_as_tuple(left) == get_microversion_as_tuple(right)


def is_microversion_ne(left, right):
    """Is microversion for left is not equal to the right one."""
    return get_microversion_as_tuple(left) != get_microversion_as_tuple(right)


def is_microversion_le(left, right):
    """Is microversion for left is less than or equal to the right one."""
    return get_microversion_as_tuple(left) <= get_microversion_as_tuple(right)


def is_microversion_lt(left, right):
    """Is microversion for left is less than the right one."""
    return get_microversion_as_tuple(left) < get_microversion_as_tuple(right)


def is_microversion_supported(microversion):
    bottom = get_microversion_as_tuple(CONF.share.min_api_microversion)
    microversion = get_microversion_as_tuple(microversion)
    top = get_microversion_as_tuple(CONF.share.max_api_microversion)
    return bottom <= microversion <= top


def skip_if_microversion_not_supported(microversion):
    """Decorator for tests that are microversion-specific."""
    if not is_microversion_supported(microversion):
        reason = ("Skipped. Test requires microversion '%s'." % microversion)
        return testtools.skip(reason)
    return lambda f: f


def skip_if_is_microversion_ge(left, right):
    """Skip if version for left is greater than or equal to the right one."""

    if is_microversion_ge(left, right):
        reason = ("Skipped. Test requires microversion "
                  "< than '%s'." % right)
        return testtools.skip(reason)
    return lambda f: f


def check_skip_if_microversion_not_supported(microversion):
    """Callable method for tests that are microversion-specific."""
    if not is_microversion_supported(microversion):
        reason = ("Skipped. Test requires microversion '%s'." % microversion)
        raise testtools.TestCase.skipException(reason)


def rand_ip(network=False):
    """This uses the TEST-NET-3 range of reserved IP addresses.

    Using this range, which are reserved solely for use in
    documentation and example source code, should avoid any potential
    conflicts in real-world testing.
    """
    test_net_3 = '203.0.113.'
    address = test_net_3 + str(random.randint(0, 255))
    if network:
        mask_length = str(random.randint(24, 32))
        address = '/'.join((address, mask_length))
        ip_network = ip.IPNetwork(address)
        return '/'.join((str(ip_network.network), mask_length))
    return address


def rand_ipv6_ip(network=False):
    """This uses the IPv6 documentation range of 2001:DB8::/32"""
    ran_add = ["%x" % random.randrange(0, 16 ** 4) for i in range(6)]
    address = "2001:0DB8:" + ":".join(ran_add)
    if network:
        mask_length = str(random.randint(32, 128))
        address = '/'.join((address, mask_length))
        ip_network = ip.IPNetwork(address)
        return '/'.join((str(ip_network.network), mask_length))
    return address


def generate_share_network_data():
    data = {
        "name": data_utils.rand_name("sn-name"),
        "description": data_utils.rand_name("sn-desc"),
        "neutron_net_id": data_utils.rand_name("net-id"),
        "neutron_subnet_id": data_utils.rand_name("subnet-id"),
    }
    return data


def generate_subnet_data():
    data = {
        "neutron_net_id": data_utils.rand_name("net-id"),
        "neutron_subnet_id": data_utils.rand_name("subnet-id"),
    }
    return data


def generate_security_service_data(set_ou=False):
    data = {
        "name": data_utils.rand_name("ss-name"),
        "description": data_utils.rand_name("ss-desc"),
        "dns_ip": utils.rand_ip(),
        "server": utils.rand_ip(),
        "domain": data_utils.rand_name("ss-domain"),
        "user": data_utils.rand_name("ss-user"),
        "password": data_utils.rand_name("ss-password"),
    }
    if set_ou:
        data["ou"] = data_utils.rand_name("ss-ou")

    return data


def choose_matching_backend(share, pools, share_type):
    extra_specs = {}
    # fix extra specs with string values instead of boolean
    for k, v in share_type['extra_specs'].items():
        extra_specs[k] = (True if str(v).lower() == 'true'
                          else False if str(v).lower() == 'false'
                          else v)
    selected_pool = next(
        (x for x in pools if (x['name'] != share['host'] and all(
            y in x['capabilities'].items() for y in extra_specs.items()))),
        None)

    return selected_pool


def get_configured_extra_specs(variation=None):
    """Retrieve essential extra specs according to configuration in tempest.

    :param variation: can assume possible values: None to be as configured in
        tempest; 'opposite_driver_modes' for as configured in tempest but
        inverse driver mode; 'invalid' for inverse as configured in tempest,
        ideal for negative tests.
    :return: dict containing essential extra specs.
    """

    extra_specs = {'storage_protocol': CONF.share.capability_storage_protocol}

    if variation == 'invalid':
        extra_specs['driver_handles_share_servers'] = (
            not CONF.share.multitenancy_enabled)
        extra_specs['snapshot_support'] = (
            not CONF.share.capability_snapshot_support)

    elif variation == 'opposite_driver_modes':
        extra_specs['driver_handles_share_servers'] = (
            not CONF.share.multitenancy_enabled)
        extra_specs['snapshot_support'] = (
            CONF.share.capability_snapshot_support)

    else:
        extra_specs['driver_handles_share_servers'] = (
            CONF.share.multitenancy_enabled)
        extra_specs['snapshot_support'] = (
            CONF.share.capability_snapshot_support)
        extra_specs['create_share_from_snapshot_support'] = (
            CONF.share.capability_create_share_from_snapshot_support)

    return extra_specs


def get_access_rule_data_from_config(protocol):
    """Get the first available access type/to combination from config.

    This method opportunistically picks the first configured protocol
    to create the share. Do not use this method in tests where you need
    to test depth and breadth in the access types and access recipients.
    """

    if protocol in CONF.share.enable_ip_rules_for_protocols:
        access_type = "ip"
        access_to = rand_ip()
    elif protocol in CONF.share.enable_user_rules_for_protocols:
        access_type = "user"
        access_to = CONF.share.username_for_user_rules
    elif protocol in CONF.share.enable_cert_rules_for_protocols:
        access_type = "cert"
        access_to = "client3.com"
    elif protocol in CONF.share.enable_cephx_rules_for_protocols:
        access_type = "cephx"
        access_to = data_utils.rand_name("cephx-id")
    else:
        message = "Unrecognized protocol and access rules configuration."
        raise testtools.TestCase.skipException(message)

    return access_type, access_to


def replication_with_multitenancy_support():
    return (share_network_subnets_are_supported() and
            CONF.share.multitenancy_enabled)


def skip_if_manage_not_supported_for_version(
        version=CONF.share.max_api_microversion):
    if (is_microversion_lt(version, "2.49")
            and CONF.share.multitenancy_enabled):
        raise testtools.TestCase.skipException(
            "Share manage tests with multitenancy are disabled for "
            "microversion < 2.49")


def share_network_subnets_are_supported():
    return is_microversion_supported(SHARE_NETWORK_SUBNETS_MICROVERSION)


def share_replica_quotas_are_supported():
    return is_microversion_supported(SHARE_REPLICA_QUOTAS_MICROVERSION)


def share_network_get_default_subnet(share_network):
    return next((
        subnet for subnet in share_network.get('share_network_subnets', [])
        if subnet['availability_zone'] is None), None)


def get_extra_headers(request_version, graduation_version):
    headers = None
    extra_headers = False
    if is_microversion_lt(request_version, graduation_version):
        headers = EXPERIMENTAL
        extra_headers = True
    return headers, extra_headers
