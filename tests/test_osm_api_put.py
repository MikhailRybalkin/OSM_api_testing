# File contains tests for PUT requests

import pytest
import allure
from helpers.http_methods import Http_methods


@allure.epic("PUT tests")
class Test_put_checks:
    """Class with PUT tests"""

    @allure.description("CREATE test")
    @pytest.mark.skipif(lambda moderator_access: not moderator_access, reason="Moderator access required")
    def test_create_node(self, base_url, moderator_access):
        """Creates node object"""
        data = """
        <osm>
          <node id="-1" lat="48.8566" lon="2.3522" version="1"/>
        </osm>
        """
        response = Http_methods.put(f"{base_url}/node/create", data)
        assert response.status_code == 200

    @allure.description("UPDATE test")
    @pytest.mark.skipif(lambda moderator_access: not moderator_access, reason="Moderator access required")
    def test_update_node(self, base_url):
        """Updates node object"""
        node_id = -1
        data = """
        <osm>
          <node id="{node_id}" lat="48.8566" lon="2.3522" version="2"/>
        </osm>
        """
        response = Http_methods.put(f"{base_url}/node/{node_id}", data)
        assert response.status_code == 200
        if response.status_code == 200:
            assert "<osm" in response.text
