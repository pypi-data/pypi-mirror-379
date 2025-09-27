from logging import getLogger
from typing import Optional, Any

from vertagus.core.project import Project
from vertagus.core.tag_base import Tag
from vertagus.core.scm_base import ScmBase


logger = getLogger(__name__)


def validate_project_version(
    scm: ScmBase, project: Project, stage_name: Optional[str] = None, scm_branch: Optional[str] = None
) -> bool:
    # Get the previous version using SCM's strategy-aware method
    previous_version = scm.get_highest_version(branch=scm_branch)

    result = project.validate_version(previous_version, stage_name)
    current_version = project.get_version()

    if result:
        logger.info(
            f"Successfully validated current version: {current_version} against previous version: {previous_version}"
        )
    else:
        logger.error(
            f"Failed to validate current version: {current_version} against previous version: {previous_version}"
        )

    return result


def create_tags(scm: ScmBase, project: Project, stage_name: Optional[str] = None, ref: Optional[str] = None) -> None:
    tag = Tag(project.get_version())
    scm.create_tag(tag, ref=ref)
    aliases = project.get_aliases(stage_name)
    for alias in aliases:
        scm.migrate_alias(alias, ref=ref)


def create_aliases(scm: ScmBase, project: Project, stage_name: Optional[str] = None, ref: Optional[str] = None) -> None:
    aliases = project.get_aliases(stage_name)
    for alias in aliases:
        scm.migrate_alias(alias, ref=ref)


def bump_version(
    scm: ScmBase,
    project: Project,
    stage_name: Optional[str] = None,
    write: bool = True,
    bumper_kwargs: Optional[dict[str, Any]] = None,
) -> str:
    if not project.bumper:
        raise ValueError("Bumper is not set for the project.")
    if bumper_kwargs is None:
        bumper_kwargs = {}
    if project.bumper.inject_scm:
        bumper_kwargs["scm"] = scm
    return project.bump_version(stage_name, write=write, **bumper_kwargs)
