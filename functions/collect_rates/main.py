import http

import requests
from src.constants import DATE_FORMAT, REQUEST_URL
from src.environment import API_KEY
from src.parser import parse_schema_from_xml
from src.repository import Repository, get_connection
from src.validator import validate_event


def handler(event, context):
    repository = Repository(get_connection())
    data = validate_event(event)
    if data.api_key != API_KEY:
        return {
            "statusCode": http.HTTPStatus.UNAUTHORIZED,
            "headers": {"content-type": "application/json"},
            "body": {"result": "wrong api key"},
        }
    # requesting to API
    response = requests.get(
        REQUEST_URL, params={"rate_date": data.date.strftime(DATE_FORMAT)}
    )
    if not response.ok:
        return {
            "statusCode": response.status_code,
            "headers": {"content-type": "application/json"},
            "body": {"result": "error", "detail": response.text},
        }
    # parse and validate data
    parsed_data = parse_schema_from_xml(response.text)
    existing_data = repository.get_rates(data.date)
    for_save = []
    not_actual_ids = []
    for volute in parsed_data:
        if previous_data := list(
            filter(lambda d: d.rate_code == volute.rate_code, existing_data)
        ):
            if previous_data[0].value != volute.value:
                for_save.append(volute)
                not_actual_ids.append(previous_data[0].id)
        else:
            for_save.append(volute)
    not_actual_ids and repository.update_old_volutes(not_actual_ids)
    for_save and repository.save_rates(for_save, data.date)
    repository.connection.commit()
    return {
        "statusCode": http.HTTPStatus.OK,
        "headers": {"content-type": "application/json"},
        "body": {
            "result": "success",
            "saved": len(for_save),
            "updated": len(not_actual_ids),
        },
    }
