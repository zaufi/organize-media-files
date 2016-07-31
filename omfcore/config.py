# -*- coding: utf-8 -*-
#
# Organize Media Files
#
# Copyright (c) 2016 Alex Turbov <i.zaufi@gmail.com>
#
# Organize Media Files is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Organize Media Files is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import configparser
import copy

class config:

    def __init__(self, filename):
        # Lets use builtin python's INI file parser and feed a fake section to it.
        with filename.open('r') as inp:
            config_string = '[dummy]\n' + inp.read()

        # Parse file content
        config = configparser.ConfigParser()
        config.read_string(config_string)

        # The result is a list of keys from the only (fake) section
        self.patterns = dict(config['dummy'])

    def merge_from(self, other):
        tmp = copy.deepcopy(other.patterns)
        tmp.update(self.patterns)
        self.patterns = tmp
