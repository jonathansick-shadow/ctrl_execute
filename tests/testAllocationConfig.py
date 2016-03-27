#!/usr/bin/env python
#
# LSST Data Management System
# Copyright 2008-2012 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#
import unittest
import os.path
from lsst.ctrl.execute.allocationConfig import AllocationConfig


class test1(unittest.TestCase):

    def setUp(self):
        self.config = AllocationConfig()

    def test_config1(self):

        self.assertTrue(self.config.platform.queue == None)
        self.assertTrue(self.config.platform.email == None)
        self.assertTrue(self.config.platform.scratchDirectory == None)
        self.assertTrue(self.config.platform.loginHostName == None)
        self.assertTrue(self.config.platform.utilityPath == None)

    def test_config2(self):
        path = os.path.join("tests", "testfiles", "config_allocation.py")
        self.config.load(path)

        self.assertTrue(self.config.platform.queue == "normal")
        self.assertTrue(self.config.platform.email == "#PBS mail -be")
        self.assertTrue(self.config.platform.scratchDirectory == "/tmp")
        self.assertTrue(self.config.platform.loginHostName == "bighost.lsstcorp.org")
        self.assertTrue(self.config.platform.utilityPath == "/bin")

if __name__ == "__main__":
    unittest.main()
