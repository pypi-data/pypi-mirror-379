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

import uuid

from cyborg_tempest_plugin.tests.api import base
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc


class AcceleratorRequestNegativeTest(base.BaseAPITest):

    @classmethod
    def skip_checks(cls):
        super(AcceleratorRequestNegativeTest, cls).skip_checks()

    credentials = ['admin']

    @decorators.attr(type=['negative', 'gate'])
    def test_get_non_existent_accelerator_request(self):
        # get the non-existent accelerator request
        non_existent_id = str(uuid.uuid4())
        self.assertRaises(lib_exc.NotFound,
                          self.os_admin.cyborg_client.get_accelerator_request,
                          non_existent_id)

    @decorators.attr(type=['negative', 'gate'])
    def test_delete_non_existent_accelerator_request(self):
        # delete the non-existent accelerator request
        non_existent_id = str(uuid.uuid4())
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.delete_accelerator_request,
            non_existent_id)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_accelerator_request_device_profile_name_is_null(self):
        # create the accelerator request with device profile name null
        dp_mame = {"device_profile_name": ""}
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.create_accelerator_request,
            dp_mame)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_accelerator_request_device_profile_name_non_exist(self):
        # create the accelerator request with device profile name non_exist
        dp_mame = {"device_profile_name": "fake_dp"}
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.create_accelerator_request,
            dp_mame)

    @decorators.attr(type=['negative', 'gate'])
    def test_create_accelerator_request_with_special_characters(self):
        # create the accelerator request with special characters
        dp_mame = {"device_profile_name": "!@#$%^&*()=-[]"}
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.create_accelerator_request,
            dp_mame)
