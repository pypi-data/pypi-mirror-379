import os
from pathlib import Path

import copier
import questionary
import typer
from rich.status import Status
from typing_extensions import Annotated

from .choices import DATABASE_CHOICES, FRONTEND_CHOICES

app = typer.Typer(no_args_is_help=True)


@app.command(name="new")
def new(
    project_name: Annotated[
        str | None, typer.Argument(help="Your project name")
    ] = None,
    database: Annotated[
        str | None,
        typer.Option(help="Database to use"),
    ] = None,
    frontend: Annotated[
        str | None, typer.Option(help="Frontend framework to use")
    ] = None,
    tailwind: Annotated[bool | None, typer.Option(help="Use Tailwind CSS")] = None,
    docker_in_dev: Annotated[
        bool | None, typer.Option(help="Use Docker in development")
    ] = None,
    docker_in_prod: Annotated[
        bool | None, typer.Option(help="Use Docker in production")
    ] = None,
    allauth: Annotated[
        bool | None, typer.Option(help="Use django-allauth for authentication")
    ] = None,
):
    """
    Create a new Django project with battery pack configured
    """
    if not project_name:
        project_name = questionary.text("Your project name").ask()
        if not project_name:  # Immediately exit if still empty
            typer.echo("Project name cannot be empty")
            raise typer.Exit(1)
    project_name = project_name.lower().replace(" ", "_").replace("-", "_")

    if not database:
        database = questionary.select(
            "Which database do you want to use?",
            default="sqlite",
            choices=DATABASE_CHOICES,
        ).ask()

    if not frontend:
        frontend = questionary.select(
            "Which frontend do you want to use?",
            choices=FRONTEND_CHOICES,
        ).ask()

    if tailwind is None:
        tailwind = questionary.confirm(
            "Do you want to use Tailwind CSS?", default=True
        ).ask()

    if docker_in_dev is None:
        docker_in_dev = questionary.confirm(
            "Do you want to use Docker in development?", default=True
        ).ask()

    if docker_in_prod is None:
        docker_in_prod = questionary.confirm(
            "Do you want to use Docker in production?", default=True
        ).ask()

    if allauth is None:
        allauth = questionary.confirm(
            "Do you want to use django-allauth for authentication?", default=True
        ).ask()

    data = {
        "project_name": project_name,
        "database": database,
        "docker_dev": docker_in_dev,
        "docker_prod": docker_in_prod,
        "allauth": allauth,
    }

    if frontend == "htmx":
        src_path = "gh:SarthakJariwala/lfp-htmx-template"
    else:
        src_path = "gh:SarthakJariwala/django-vite-inertia"
        data["frontend"] = frontend
        data["tailwind_css"] = tailwind

    # currently, react integration supports a starter_kit based on shadcn/ui
    if frontend == "react":
        data["starter_kit"] = True

    with Status(f"Creating project {project_name}..."):
        project_path = Path(project_name)
        os.makedirs(project_path, exist_ok=True)
        with copier.Worker(
            src_path=src_path, dst_path=project_path, data=data
        ) as worker:
            worker.run_copy()
