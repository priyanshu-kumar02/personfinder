# Copyright 2019 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import config
import model
import photo
from search.searcher import Searcher
import simplejson
import utils


class FrontendApiHandler(utils.BaseHandler):
    """Base handler for frontend API handlers."""

    def _return_json(self, data):
        self.response.headers['Content-Type'] = (
            'application/json; charset=utf-8')
        self.write(simplejson.dumps(data))


class Person(FrontendApiHandler):

    repo_required = True

    def get(self):
        # TODO: implement this
        self._return_json({
          'name': 'Hard-coded placeholder',
          'sex': 'male',
          'age': '42',
          'home_city': 'Mountain View',
          'home_state': 'CA',
          'home_country': 'U.S.',
          'description': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
            enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          ''',
          'author_name': 'Hard-coded author',
          'source_date': 'Jan 1, 2019 01:01AM',
          'source_name': 'Google.org',
          'profile_pages': [
            {'site': 'facebook', 'value': 'https://www.facebook.com/hardcoded.placeholder.123'},
          ],
          'notes': [
            {
              'note_record_id': 'person1.1',
              'source_date': 'Jan 1, 2019 01:01AM',
              'author_name': 'Note Author 1',
              'author_made_contact': False,
              'status': 'information_sought',
              'text': 'Trying to find this person.',
            },
            {
              'note_record_id': 'person1.2',
              'source_date': 'Jan 2, 2019 02:02AM',
              'author_name': 'Note Author 2',
              'author_made_contact': True,
              'status': 'is_note_author',
              'last_known_location': 'Roppongi, Tokyo',
              'text': 'I am safe!',
            },
          ],
        })
