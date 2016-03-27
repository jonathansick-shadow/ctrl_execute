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

import sys
import unittest
import os.path
from lsst.ctrl.execute.allocatorParser import AllocatorParser


class TestAllocatorParser(unittest.TestCase):

    def test1(self):
        sys.argv = ["test1",
                    "test_platform",
                    "-n", "64",
                    "-s", "12",
                    "-m", "00:30:00",
                    "-N", "test_set",
                    "-q", "normal",
                    "-e",
                    "-O", "outlog",
                    "-E", "errlog",
                    "-v",
                    ]

        al = AllocatorParser(sys.argv[0])
        args = al.getArgs()

        self.assertTrue(args.nodeCount == 64)
        self.assertTrue(args.slots == 12)
        self.assertTrue(args.maximumWallClock == "00:30:00")
        self.assertTrue(args.nodeSet == "test_set")
        self.assertTrue(args.queue == "normal")
        self.assertTrue(args.email)
        self.assertTrue(args.outputLog == "outlog")
        self.assertTrue(args.errorLog == "errlog")
        self.assertTrue(args.verbose)

if __name__ == "__main__":
    unittest.main()
