# File contains tests for GET requests

import allure
from helpers.http_methods import Http_methods


@allure.epic("GET tests")
class Test_get_checks:
    """Class with GET tests"""

    @allure.description("Capabilities")
    def test_get_capabilities(self, base_url):
        """Gets capabilities info"""
        response = Http_methods.get(f"{base_url}/capabilities", False)
        assert response.status_code == 200
        assert "<osm version=" in response.text

    @allure.description("Map")
    def test_get_map(self, base_url):
        """Gets objects inside bounding box"""
        # Bounding box coordinates for a small area
        bbox = "11.54,48.14,11.543,48.145"
        response = Http_methods.get(f"{base_url}/map?bbox={bbox}", False)
        assert response.status_code == 200
        assert "osm" in response.text

    @allure.description("Invalid bbox")
    def test_invalid_bbox(self, base_url):
        """Check invalid bounding box"""
        bbox = "invalid"
        response = Http_methods.get(f"{base_url}/map?bbox={bbox}")
        assert response.status_code == 400

    @allure.description("Node")
    def test_get_node(self, base_url, node_id_example):
        """Gets node object info"""
        response = Http_methods.get(f"{base_url}/node/{node_id_example}")
        assert response.status_code in [200, 404]  # Node might not exist
        if response.status_code == 200:
            response_el = response.json().get('elements')[0]
            assert 'id' in response_el
            assert response_el.get('type') == 'node'

    @allure.description("Way")
    def test_get_way(self, base_url, way_id_example):
        """Gets way object info"""
        response = Http_methods.get(f"{base_url}/way/{way_id_example}")
        assert response.status_code in [200, 404]
        if response.status_code == 200:
            response_el = response.json().get('elements')[0]
            assert 'id' in response_el
            assert response_el.get('type') == 'way'

    @allure.description("Relation")
    def test_get_relation(self, base_url, relation_id_example):
        """Gets relation object info"""
        response = Http_methods.get(f"{base_url}/relation/{relation_id_example}")
        assert response.status_code in [200, 404]
        if response.status_code == 200:
            response_el = response.json().get('elements')[0]
            assert 'id' in response_el
            assert response_el.get('type') == 'relation'

    @allure.description("Invalid endpoint")
    def test_invalid_endpoint(self, base_url):
        """Checks invalid api endpoint"""
        response = Http_methods.get(f"{base_url}/invalid")
        assert response.status_code == 404

    @allure.description("SQL injection")
    def test_sql_injection(self, base_url, node_id_example):
        """Checks SQL injection handling"""
        injection_str = f"{node_id_example} OR 1=1"
        response = Http_methods.get(f"{base_url}/node/{injection_str}")
        assert response.status_code == 400

    @allure.description("History")
    def test_get_history(self, base_url, node_id_example):
        """Gets object history info"""
        response = Http_methods.get(f"{base_url}/node/{node_id_example}/history", False)
        assert response.status_code in [200, 404]  # Node might not exist
        if response.status_code == 200:
            assert f'node id="{node_id_example}"' in response.text

    @allure.description("Related relations")
    def test_get_related_relations(self, base_url, node_id_example, relation_id_example):
        """Gets info about related relations"""
        response = Http_methods.get(f"{base_url}/node/{node_id_example}/relations", False)
        assert response.status_code in [200, 404]  # Node might not exist
        if response.status_code == 200:
            assert str(relation_id_example) in response.text

    @allure.description("User")
    def test_get_user(self, base_url, user_id_example):
        """Gets user related info (by ID)"""
        response = Http_methods.get(f"{base_url}/user/{user_id_example}", False)
        assert response.status_code in [200, 404]  # User might not exist
        if response.status_code == 200:
            assert f'user id="{user_id_example}"' in response.text
