import json
try:
    from mega-header-astroml.api.app import app
    schema = app.openapi()
    with open("docs/openapi.json", "w") as f:
        json.dump(schema, f)
except Exception:
    pass
