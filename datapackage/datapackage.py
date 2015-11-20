from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from .schema import Schema


class DataPackage(object):
    SCHEMAS_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'schemas'
    )
    BASE_SCHEMA_PATH = os.path.join(SCHEMAS_PATH, 'base.json')

    def __init__(self, descriptor, schema=BASE_SCHEMA_PATH):
        self.__descriptor = descriptor
        self.__schema = Schema(schema)

    @property
    def descriptor(self):
        return self.__descriptor

    @property
    def schema(self):
        return self.__schema

    @property
    def properties(self):
        private_prefix = '_{cls}__'.format(cls=self.__class__.__name__)
        is_private = lambda k: k.startswith(private_prefix)

        return {k: v for (k, v) in self.__dict__.items()
                if not is_private(k) and v is not None}

    def validate(self):
        self.schema.validate(self.descriptor)