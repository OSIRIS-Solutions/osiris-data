from pydantic import BaseModel
import yaml
import json
import os

from osirisdata.osiris_io import OsirisIO



def dump_json_schema(validators: dict[str, BaseModel]):
    for key, validator in validators.items():
        print(f"Dumping JSON schema for {key}")
        os.makedirs("schemas", exist_ok=True)
        with open(f"schemas/{key.replace('#', '_')}.json", "w") as f:
            model_schema = validator.model_json_schema()
            f.write(json.dumps(model_schema, indent=4))


if __name__ == "__main__":
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    osiris = OsirisIO(
        connection=config["connection_string"],
        database=config["database"],
        validation=True,
        validation_extra="ignore"
    )

    dump_json_schema(osiris.validators)
