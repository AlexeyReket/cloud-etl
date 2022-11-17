import requests
from src.constants import DATE_FORMAT, REQUEST_URL
from src.parser import parse_schema_from_xml
from src.repository import Repository, get_connection
from src.validator import validate


def handler(event, context):
    repository = Repository(get_connection())
    date = validate(event)
    # requesting to API
    response = requests.get(REQUEST_URL.format(date=date.strftime(DATE_FORMAT)))
    if response.status_code != 200:
        return {
            "statusCode": response.status_code,
            "headers": {"content-type": "application/json"},
            "body": {"result": "error", "detail": response.text},
        }
    # parse and validate data
    parsed_data = parse_schema_from_xml(response.text)
    existing_data = repository.get_rates(date)
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
    for_save and repository.save_rates(for_save, date)
    repository.connection.commit()
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": {
            "result": "success",
            "saved": len(for_save),
            "updated": len(not_actual_ids),
        },
    }
