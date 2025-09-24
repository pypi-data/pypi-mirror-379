from pydantic import ValidationError
from pytest import raises

from supervisor_pydantic import ProgramConfiguration


def test_inst():
    with raises(ValidationError):
        ProgramConfiguration()
    ProgramConfiguration(command="echo 'test'")


def test_dump_exitcodes():
    # ensure that converting exit codes to string does not regress
    # pydantic_core._pydantic_core.PydanticSerializationError: Error serializing to JSON:
    # PydanticSerializationError: Error calling function `_dump_exitcodes`:
    # TypeError: sequence item 0: expected str instance, int found
    ProgramConfiguration(command="echo 'test'", exitcodes=[0]).model_dump_json(exclude_unset=True)


def test_autorestart_options():
    ProgramConfiguration(command="echo 'test'", autorestart=True).model_dump_json(exclude_unset=True)
    ProgramConfiguration(command="echo 'test'", autorestart=False).model_dump_json(exclude_unset=True)
    ProgramConfiguration(command="echo 'test'", autorestart="unexpected").model_dump_json(exclude_unset=True)
    with raises(ValidationError):
        ProgramConfiguration(command="echo 'test'", autorestart="other").model_dump_json(exclude_unset=True)


def test_cfg():
    c = ProgramConfiguration(command="echo 'test'", environment={"USER": "test", "HOME": "a blerg's path"})
    assert c.to_cfg("name").strip() == "[program:name]\ncommand=echo 'test'\nenvironment=USER=test,HOME='a blerg'\"'\"'s path'"
