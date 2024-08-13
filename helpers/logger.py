# File contains log file handling functionality

import datetime
import os

from requests import Response


class Logger:
    """Class with logging functionality"""
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"  # log name

    @classmethod
    def write_log_to_file(cls, data: str):
        """Writes text to the log file"""
        try:
            # Open and write to file
            with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
                logger_file.write(data)

        except Exception as ex:
            error_message = f"Can not write to log: {ex}"
            print(error_message)

    @classmethod
    def add_request(cls, url: str, method: str):
        """Writes request to the log file"""
        try:
            test_name = os.environ.get('PYTEST_CURRENT_TEST')  # Determine path

            data_to_add = f"\n-----\n"
            data_to_add += f"Test: {test_name}\n"
            data_to_add += f"Time: {str(datetime.datetime.now())}\n"
            data_to_add += f"Request method: {method}\n"
            data_to_add += f"Request URL: {url}\n"
            data_to_add += "\n"

            cls.write_log_to_file(data_to_add)  # update log

        except Exception as ex:
            error_message = f"Can not lod request: {ex}"
            print(error_message)

    @classmethod
    def add_response(cls, result: Response):
        """Writes response to the log file"""
        try:
            cookies_as_dict = dict(result.cookies)
            headers_as_dict = dict(result.headers)

            data_to_add = f"Response code: {result.status_code}\n"
            data_to_add += f"Response text: {result.text}\n"
            data_to_add += f"Response headers: {headers_as_dict}\n"
            data_to_add += f"Response cookies: {cookies_as_dict}\n"
            data_to_add += f"\n-----\n"

            cls.write_log_to_file(data_to_add)  # update log

        except Exception as ex:
            error_message = f"Can not log response: {ex}"
            print(error_message)
