from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "olaMundo",
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "requiered": True, "empty": False },
            "elemento2": { "type": "string", "requiered": True, "empty": True },
            "elemento3": { "type": "string", "requiered": False, "empty": False }
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print("body OK")
