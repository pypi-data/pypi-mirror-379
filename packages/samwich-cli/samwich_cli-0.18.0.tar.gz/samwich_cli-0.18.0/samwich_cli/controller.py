from __future__ import annotations

import os
import pathlib
import shutil

import click

from samwich_cli import file_utils, model, sam_utils


def run(ctx: model.Context) -> None:
    """Run the SAMWICH CLI."""
    if ctx.debug:
        click.echo(f"Context: {ctx._asdict()}\n")

    build_resources = sam_utils.get_build_resources(ctx)
    layers = build_resources["layers"]
    functions = build_resources["functions"]

    dependencies_state = _prepare_requirements(ctx, layers, functions)

    sam_utils.sam_build(ctx.sam_args, ctx.debug)

    _cleanup_requirements(ctx, dependencies_state)
    _update_layer_structure(ctx, layers, dependencies_state.layer_path)
    _update_function_structure(ctx, functions)


def _prepare_requirements(
    ctx: model.Context,
    layers: list[model.ArtifactDetails],
    functions: list[model.ArtifactDetails],
) -> model.DependenciesState:
    """
    Prepare the requirements for the build.

    Args:
        ctx: The context for the build.
        layers: The layers to be built.
        functions: The functions to be built.

    Returns:
        DependenciesState: The dependencies state containing the layer path and managed requirements paths.
    """
    layer_path = None

    copy_candidate_dirs = []
    if len(layers) == 1:
        layer_path = pathlib.Path(layers[0].codeuri)
        copy_candidate_dirs = [layer_path]
    elif len(layers) == 0:
        copy_candidate_dirs = [pathlib.Path(fn.codeuri) for fn in functions]
    else:
        copy_candidate_dirs = []
        click.secho(
            "More than one layer found, skipping requirements copy. This may be supported in the future.",
            fg="yellow",
        )

    managed_reqs_paths = []
    for candidate in copy_candidate_dirs:
        copied_req_path = file_utils.copy_requirements(ctx, candidate)
        if copied_req_path is None:
            continue

        managed_reqs_paths.append(copied_req_path)
        if ctx.debug:
            click.echo(
                f"Copied requirements.txt to {str(os.path.relpath(start=ctx.workspace_root, path=copied_req_path))}"
            )

    click.echo()

    return model.DependenciesState(
        layer_path=layer_path, managed_requirements_paths=managed_reqs_paths
    )


def _cleanup_requirements(
    ctx: model.Context,
    dependencies_state: model.DependenciesState,
) -> None:
    """Cleanup the requirements."""
    for req_path in dependencies_state.managed_requirements_paths:
        if list(_.name for _ in req_path.parent.glob(pattern="*")) == [
            "requirements.txt"
        ]:
            if ctx.debug:
                click.echo(
                    f"Removing {os.path.relpath(start=ctx.workspace_root, path=req_path.parent)}"
                )
            shutil.rmtree(req_path.parent, ignore_errors=True)
        else:
            if ctx.debug:
                click.echo(
                    f"Removing {os.path.relpath(start=ctx.workspace_root, path=req_path)}"
                )
            req_path.unlink(missing_ok=True)
    click.echo()


def _update_layer_structure(
    ctx: model.Context,
    layers: list[model.ArtifactDetails],
    layer_path: pathlib.Path | None,
) -> None:
    """Update the layer folder structure."""
    if layer_path and layer_path.exists():
        click.echo(
            "Updating layer folder structure: "
            + click.style(layers[0].name, fg="magenta")
        )
        relative_path = file_utils.determine_relative_artifact_path(
            ctx, artifact_dir=layer_path
        )
        if ctx.debug:
            click.echo(
                f"{file_utils.INDENT}Relative path: {os.path.relpath(start=ctx.source_dir, path=relative_path)}"
            )
        file_utils.restructure_layer(
            ctx,
            ctx.sam_build_dir / layers[0].full_path,
            relative_path,
            layer_path,
        )
        click.echo("")


def _update_function_structure(
    ctx: model.Context, functions: list[model.ArtifactDetails]
) -> None:
    """Update the function folder structure."""
    for fn in functions:
        click.echo(
            "Updating lambda folder structure: " + click.style(fn.name, fg="magenta")
        )
        relative_path = file_utils.determine_relative_artifact_path(
            ctx, pathlib.Path(fn.codeuri)
        )
        if relative_path == pathlib.Path():
            click.echo(
                f"{file_utils.INDENT}Source directory is the same as the artifact directory."
            )
            continue

        if ctx.debug:
            click.echo(
                f"{file_utils.INDENT}Relative path: {os.path.relpath(start=ctx.source_dir, path=relative_path)}"
            )
        file_utils.restructure_lambda_function(
            ctx,
            ctx.sam_build_dir / fn.full_path,
            relative_path,
            pathlib.Path(fn.codeuri),
        )
        click.echo("")
