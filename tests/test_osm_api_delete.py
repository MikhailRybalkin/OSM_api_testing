# File contains tests for DELETE requests

import pytest
import allure
from helpers.http_methods import Http_methods


@allure.epic("DELETE tests")
class Test_delete_checks:
    """Class with DELETE tests"""

    @allure.description("DELETE test")
    @pytest.mark.skipif(lambda moderator_access: not moderator_access, reason="Moderator access required")
    def test_delete_node(self, base_url):
        """Deletes node with example ID"""
        node_id = -1  # sample ID
        response = Http_methods.delete(f"{base_url}/node/{node_id}")
        assert response.status_code == 200
