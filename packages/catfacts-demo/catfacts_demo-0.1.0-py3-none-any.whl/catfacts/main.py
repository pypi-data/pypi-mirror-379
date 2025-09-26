import random
import re
import importlib

import requests

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich import box
from pydantic import BaseModel
from pydantic import field_validator
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from typing import Self
from typing import TypedDict
from typing import cast

default_url = "https://meowfacts.herokuapp.com/"
re_cat = re.compile(r"\bcats?", re.IGNORECASE)


class Settings(BaseSettings):
    url: str = default_url

    model_config = SettingsConfigDict(env_prefix="catfacts_")


class ApiResponse(TypedDict):
    data: list[str]


class Fact(BaseModel):
    fact: str

    @field_validator("fact", mode="after")
    @classmethod
    def highlight_cats(cls, v: str) -> str:
        return re_cat.sub(r"[bold gold1]\g<0>[/bold gold1]", v)

    @classmethod
    def from_api(cls, data: ApiResponse) -> Self:
        return cls(fact=data["data"][0])


settings = Settings()


def get_a_cat() -> str:
    with importlib.resources.path("catfacts", "cats") as path:
        img = random.choice(list(Path(path).glob("*.txt")))
        with img.open("r") as fd:
            return fd.read()


def main():
    cat = get_a_cat()

    res = requests.get(settings.url)
    res.raise_for_status()
    fact = Fact.from_api(cast(ApiResponse, res.json()))

    console = Console()
    panel = Panel("\n".join([cat, fact.fact]), box=box.ROUNDED, border_style="red")
    console.print(panel)


if __name__ == "__main__":
    main()
