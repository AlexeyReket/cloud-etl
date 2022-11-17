import datetime
import http
import json
from json import JSONDecodeError

from src.schema import EventData


def validate_event(event) -> EventData:
    body = event.get("body") if event else None
    if not body:
        raise Exception(
            {
                "statusCode": http.HTTPStatus.BAD_REQUEST,
                "headers": {"content-type": "application/json"},
                "body": {"result": "error", "detail": "no body"},
            }
        )
    if type(body) == str:
        try:
            body = json.loads(body)
        except JSONDecodeError:
            raise Exception(
                {
                    "statusCode": http.HTTPStatus.BAD_REQUEST,
                    "headers": {"content-type": "application/json"},
                    "body": {"result": "error", "detail": "wrong body"},
                }
            )

    # date validation
    date = body.get("date")
    if not date:
        date = datetime.date.today()
    else:
        try:
            date = datetime.date.fromisoformat(date)
        except ValueError:
            raise Exception(
                {
                    "statusCode": http.HTTPStatus.BAD_REQUEST,
                    "headers": {"content-type": "application/json"},
                    "body": {"result": "error", "detail": "invalid date"},
                }
            )

    return EventData(date=date, api_key=body.get("api_key"))
