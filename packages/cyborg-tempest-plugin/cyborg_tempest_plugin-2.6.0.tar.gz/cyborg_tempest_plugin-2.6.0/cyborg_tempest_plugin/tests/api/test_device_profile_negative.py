# Copyright 2020 Inspur
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

import random
import string
import uuid

from cyborg_tempest_plugin.tests.api import base
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc


class DeviceProfileNegativeTest(base.BaseAPITest):

    @classmethod
    def skip_checks(cls):
        super(DeviceProfileNegativeTest, cls).skip_checks()

    credentials = ['admin']

    @decorators.attr(type=['negative', 'gate'])
    def test_get_non_existent_device_profile(self):
        # get the non-existent device_profile
        non_existent_id = str(uuid.uuid4())
        self.assertRaises(lib_exc.NotFound,
                          self.os_admin.cyborg_client.get_device_profile,
                          non_existent_id)

    @decorators.attr(type=['negative', 'gate'])
    def test_delete_non_existent_device_profile(self):
        # delete the non-existent device_profile
        non_existent_id = str(uuid.uuid4())
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.delete_device_profile_by_uuid,
            non_existent_id)

    @decorators.attr(type=['negative', 'gate'])
    def test_delete_multiple_non_existent_device_profile(self):
        # delete multiple non_existent device_profile
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.
            delete_multiple_device_profile_by_names,
            'fake_device_name1', 'fake_device_name2')

    @decorators.attr(type=['negative', 'gate'])
    def test_delete_device_profile_name_null(self):
        # delete the device_profile name is null
        name = ""
        self.assertRaises(
            lib_exc.BadRequest,
            self.os_admin.cyborg_client.delete_device_profile,
            name)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_device_profile_server_fault(self):
        # create device profile using an existing dp uuid
        dp = [{
            "name": "fpga_uuid_test",
            "groups": [
                {
                    "resources:FPGA": "1",
                    "trait:CUSTOM_FAKE_DEVICE": "required"
                }]
        }]
        # create a device profile with named "fpga_uuid_test"
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        self.assertEqual(dp[0]['name'], response['name'])
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])
        dp[0]['name'] = 'new-fpga'
        dp[0]['uuid'] = response['uuid']

        # create a same device profile with an existing dp uuid
        self.assertRaises(lib_exc.ServerFault,
                          self.os_admin.cyborg_client.create_device_profile,
                          dp)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_device_profile_conflict(self):
        # create device profile name same
        dp = [{
            "name": "fpga_same_test",
            "groups": [
                {
                    "resources:FPGA": "1",
                    "trait:CUSTOM_FAKE_DEVICE": "required"
                }],
            "description": "null"
        }]
        # create a device profile with named "fpga_same_test"
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        self.assertEqual(dp[0]['name'], response['name'])
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])

        # create a same device profile with the same name "fpga_same_test"
        self.assertRaises(lib_exc.Conflict,
                          self.os_admin.cyborg_client.create_device_profile,
                          dp)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_device_profile_name_is_null(self):
        # create device profile name is null
        dp = [{
            "name": "",
            "groups": [
                {
                    "resources:FPGA": "1",
                    "trait:CUSTOM_FAKE_DEVICE": "required"
                }],
            "description": "null"
        }]

        # create device profile with name null
        self.assertRaises(lib_exc.ServerFault,
                          self.os_admin.cyborg_client.create_device_profile,
                          dp)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_device_profile_name_to_long(self):
        # create device profile name character is too long
        name_value = "".join(random.sample(
            string.ascii_letters * 10 + string.digits * 10, 256))
        dp = [{
            "name": name_value,
            "groups": [
                {
                    "resources:FPGA": "1",
                    "trait:CUSTOM_FAKE_DEVICE": "required"
                }],
            "description": "null"
        }]

        # create device profile with character is too long
        self.assertRaises(lib_exc.ServerFault,
                          self.os_admin.cyborg_client.create_device_profile,
                          dp)
