# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Helpers.
"""
# Copyright ©  2015 1&1 Group <git@1and1.com>
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
from __future__ import absolute_import, unicode_literals, print_function

from tqdm import tqdm


CLEARLINE = "\r\033[2K"


def progress(*args, **kwargs):
    """Wrapper for progress bars providing consistent customizaion."""
    kwargs.setdefault('dynamic_ncols', True)
    kwargs.setdefault('position', 1)
    return tqdm(*args, **kwargs)
