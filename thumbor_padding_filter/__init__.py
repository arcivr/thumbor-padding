#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '1.0.0'

try:
    from thumbor_padding_filter.padding import Filter  # NOQA
except ImportError:
    logging.exception('Could not import thumbor_padding. Probably due to setup.py installing it.')
