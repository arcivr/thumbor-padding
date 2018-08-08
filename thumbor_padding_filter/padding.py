#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
# import math

from thumbor.filters import BaseFilter, filter_method

class Filter(BaseFilter):
    """
        Pads the image with optional color.

        Usage: /filters:padding(<left>, <top>, <right>, <bottom> [, <color>])
        Examples of use:
            /filters:padding(10, 10, 20, 20)/
            /filters:padding(10, 10, 20, 20, eee)/
    """

    @filter_method(
        BaseFilter.PositiveNumber,
        BaseFilter.PositiveNumber,
        BaseFilter.PositiveNumber,
        BaseFilter.PositiveNumber,
        BaseFilter.String
    )
    def padding(self, left, top, right, bottom, color='fff'):
        offset_x = left
        offset_y = top

        new_width = self.engine.size[0] + left + right
        new_height = self.engine.size[1] + top + bottom

        new_engine = self.context.modules.engine.__class__(self.context)
        new_engine.image = new_engine.gen_image((new_width, new_height), "#" + color)
        new_engine.enable_alpha()
        new_engine.paste(self.engine, (offset_x, offset_y))
        self.engine.image = new_engine.image
