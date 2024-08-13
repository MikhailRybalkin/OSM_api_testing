# File contains necessary helpers functions

import json
import helpers.logger as log


def get_json_value(value):
    """Function gets specific item (by value input) fom json file"""
    res_value = ''
    try:
        # Open and read file
        with open('parameters.json') as f:
            json_data = json.load(f)

        # Get necessary item
        res_value = json_data[value]
    except Exception as ex:
        error_message = f"Can not open file: {ex}"
        print(error_message)
        log.Logger.write_log_to_file(error_message)

    return res_value
