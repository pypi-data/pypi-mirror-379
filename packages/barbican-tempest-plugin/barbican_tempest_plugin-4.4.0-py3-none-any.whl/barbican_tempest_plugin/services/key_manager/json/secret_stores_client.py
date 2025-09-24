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
import json
from urllib import parse

from barbican_tempest_plugin.services.key_manager.json import base


class SecretStoresClient(base.BarbicanTempestClient):

    def list_secret_stores(self, **kwargs):
        uri = '/v1/secret-stores'
        if kwargs:
            uri += '?{}'.format(parse.urlencode(kwargs))
        resp, body = self.get(uri)
        self.expected_success(200, resp.status)
        return json.loads(body.decode('UTF-8'))

    def get_secret_store(self, secret_store_id):
        uri = '/v1/secret-stores/{}'.format(secret_store_id)
        resp, body = self.get(uri)
        self.expected_success(200, resp.status)
        return json.loads(body.decode('UTF-8'))

    def get_global_secret_store(self, **kwargs):
        uri = '/v1/secret-stores/global-default'
        if kwargs:
            uri += '?{}'.format(parse.urlencode(kwargs))
        resp, body = self.get(uri)
        self.expected_success(200, resp.status)
        return json.loads(body.decode('UTF-8'))

    def get_preferred_secret_store(self, **kwargs):
        uri = '/v1/secret-stores/preferred'
        if kwargs:
            uri += '?{}'.format(parse.urlencode(kwargs))
        resp, body = self.get(uri)
        self.expected_success(200, resp.status)
        return json.loads(body.decode('UTF-8'))

    def set_preferred_secret_store(self, secret_store_id):
        uri = '/v1/secret-stores/{}/preferred'.format(secret_store_id)
        resp, body = self.post(uri, None)
        self.expected_success(204, resp.status)

    def unset_preferred_secret_store(self, secret_store_id):
        uri = '/v1/secret-stores/{}/preferred'.format(secret_store_id)
        resp, body = self.delete(uri)
        self.expected_success(204, resp.status)
