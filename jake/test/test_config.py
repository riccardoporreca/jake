"""test_config.py audits the Config class"""
# Copyright 2019 Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from jake.config.config import Config


class TestConfig(unittest.TestCase):
  """testConfig audits the Config class"""
  def setUp(self):
    self.func = Config(save_location='/tmp/')

  def test_config_object_saves_config_file(self):
    """test_config_object_saves_config_file ensures config objs are being written to file"""
    self.func.set_password("password")
    self.func.set_username("test@me.com")
    result = self.func.save_config_to_file()
    self.assertEqual(result, True)

  def test_get_config_from_file(self):
    """test_config_object_saves_config_file ensures config objs are being written to file"""
    self.func.set_password("password")
    self.func.set_username("test@me.com")
    self.func.save_config_to_file()

    (username, password) = self.func.get_config_from_file()
    self.assertEqual(username, "test@me.com")
    self.assertEqual(password, "password")

  def test_return_true_when_config_exists(self):
    """test_config_object_saves_config_file ensures config objs are being written to file"""
    self.func.set_password("password")
    self.func.set_username("test@me.com")
    self.func.save_config_to_file()
    self.assertEqual(self.func.check_if_config_exists(), True)
