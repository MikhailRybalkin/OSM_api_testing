# File contains main fixtures with basic api parameters

import pytest
import helpers.utils as helpers


@pytest.fixture
def base_url():
    """Base OSM api URL"""
    return helpers.get_json_value('base_url')


@pytest.fixture
def moderator_access():
    """Boolean moderator access parameter (allows to use put/delete requests)"""
    return helpers.get_json_value('moderator_access')


@pytest.fixture
def node_id_example():
    """Example ID of some existent node"""
    return helpers.get_json_value('node_id')


@pytest.fixture
def way_id_example():
    """Example ID of some existent way"""
    return helpers.get_json_value('way_id')


@pytest.fixture
def relation_id_example():
    """Example ID of some existent relation"""
    return helpers.get_json_value('relation_id')


@pytest.fixture
def user_id_example():
    """Example ID of some existent user ID"""
    return helpers.get_json_value('user_id')
