# File contains necessary HTTP methods for api testing (GET, PUT, DELETE)

import requests
import allure
import helpers.logger as log


class Http_methods:
    """Class with HTTP methods"""

    # Headers parameters
    json_headers = {"Accept": "application/json"}
    xml_headers = {"Content-Type": "application/xml"}
    cookie = ''

    @staticmethod
    def get(url, json=True):
        """GET method"""
        try:
            with allure.step("GET"):  # allure step
                log.Logger.add_request(url, method='GET')  # add to log
                headers = Http_methods.json_headers if json else ''
                result = requests.get(url, headers=headers, cookies=Http_methods.cookie)  # send request
                log.Logger.add_response(result)  # add to log

        except Exception as ex:
            error_message = f"Failed GET request: {ex}"
            print(error_message)
            log.Logger.write_log_to_file(error_message)

        return result

    @staticmethod
    def put(url, body):
        """PUT method"""
        try:
            with allure.step("PUT"):  # allure step
                log.Logger.add_request(url, method='PUT')  # add to log
                result = requests.put(url, json=body, headers=Http_methods.xml_headers, cookies=Http_methods.cookie)  # send request
                log.Logger.add_response(result)  # add to log

        except Exception as ex:
            error_message = f"Failed PUT request: {ex}"
            print(error_message)
            log.Logger.write_log_to_file(error_message)

        return result

    @staticmethod
    def delete(url):
        """DELETE method"""
        try:
            with allure.step("DELETE"):  # allure step
                log.Logger.add_request(url, method='DELETE')  # add to log
                result = requests.delete(url, headers=Http_methods.xml_headers, cookies=Http_methods.cookie)  # send request
                log.Logger.add_response(result)  # add to log

        except Exception as ex:
            error_message = f"Failed DELETE request: {ex}"
            print(error_message)
            log.Logger.write_log_to_file(error_message)

        return result
