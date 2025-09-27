import os.path
from typing import Type, cast, Optional, Any

from vertagus.core.project import Project
from vertagus.core.stage import Stage
from vertagus.core.tag_base import AliasBase
from vertagus.core.manifest_base import ManifestBase
from vertagus.core.rule_bases import (
    SingleVersionRuleProtocol,
    ConfigurableSingleVersionRule,
    VersionComparisonRule,
    is_configurable_single_version_rule
)
from vertagus.rules.comparison.library import ManifestsComparisonRule
from vertagus.core.scm_base import ScmBase

from vertagus.providers.scm.registry import get_scm_cls
from vertagus.providers.manifest.registry import get_manifest_cls
from vertagus.aliases.loader import get_aliases
from vertagus.rules.single_version.loader import get_rules as get_single_version_rules
from vertagus.rules.comparison.loader import get_rules as get_version_comparison_rules
from vertagus.bumpers.registry import get_bumper_cls, BumperBase


from .configuration import types as t


def create_project(data: t.ProjectData) -> Project:
    return Project(
        manifests=create_manifests(data.manifests, data.root),
        current_version_rules=create_single_version_rules(data.rules.current),
        version_increment_rules=create_version_comparison_rules(data.rules.increment, {}),
        manifest_versions_comparison_rules=create_manifest_comparison_rules(
            ["manifests_comparison"], {"manifests": data.rules.manifest_comparisons}
        )
        if data.rules.manifest_comparisons
        else [],
        stages=create_stages(data.stages, data.root) if data.stages else None,
        aliases=create_aliases((data.aliases or [])),
        bumper=create_bumper(data.bumper) if data.bumper else None,
    )


def create_manifests(manifest_data: list[t.ManifestData], root: Optional[str] = None) -> list[ManifestBase]:
    manifests = []
    for each in manifest_data:
        if root:
            each.path = os.path.join(root, each.path)
        manifest_cls = get_manifest_cls(each.type)
        manifests.append(manifest_cls(**each.config()))
    return manifests


def create_single_version_rules(rule_items: list[str]) -> list[SingleVersionRuleProtocol]:
    rule_names = []
    rule_configurations = {}
    for item in rule_items:
        if isinstance(item, str):
            rule_names.append(item)
        elif isinstance(item, dict):
            rule_names.append(item["type"])
            rule_configurations[item["type"]] = item.get("config", {})
        else:
            raise ValueError(f"Invalid rule item: {item}")

    rules = get_single_version_rules(rule_names)
    final_rules = []
    for rule in rules:
        if is_configurable_single_version_rule(rule):
            rule = cast(Type[ConfigurableSingleVersionRule], rule)
            final_rules.append(rule(rule_configurations.get(rule.name, {})))
        else:
            final_rules.append(rule)
    return final_rules


def create_version_comparison_rules(rule_names: list[str], config) -> list[VersionComparisonRule]:
    rule_classes = get_version_comparison_rules(rule_names)
    return [rule_cls(config=config) for rule_cls in rule_classes]


def create_manifest_comparison_rules(rule_names: list[str], config) -> list[ManifestsComparisonRule]:
    def _cast(cls: Type[VersionComparisonRule]) -> Type[ManifestsComparisonRule]:
        return cast(Type[ManifestsComparisonRule], cls)

    rule_classes = get_version_comparison_rules(rule_names)
    rule_classes = [_cast(rule_cls) for rule_cls in rule_classes]
    return [rule_cls(config=config) for rule_cls in rule_classes]


def create_aliases(alias_names: list[str]) -> list[Type[AliasBase]]:
    return get_aliases(alias_names)


def create_stages(stage_data: list[t.StageData], project_root: Optional[str] = None) -> list[Stage]:
    stages = []
    for data in stage_data:
        stages.append(
            Stage(
                name=data.name,
                manifests=create_manifests(data.manifests, project_root),
                current_version_rules=create_single_version_rules(data.rules.current),
                version_increment_rules=create_version_comparison_rules(data.rules.increment, {}),
                manifest_versions_comparison_rules=create_manifest_comparison_rules(
                    ["manifests_comparison"], {"manifests": data.rules.manifest_comparisons}
                )
                if data.rules.manifest_comparisons
                else [],
                aliases=create_aliases((data.aliases or [])),
                bumper=create_bumper(data.bumper) if data.bumper else None,
            )
        )
    return stages


def create_scm(data: t.ScmData) -> ScmBase:
    scm_cls = get_scm_cls(data.scm_type)
    return scm_cls(**data.config())


def create_bumper(data: t.BumperData) -> BumperBase:
    """
    Create a bumper instance based on the provided data.
    """
    bumper_cls = get_bumper_cls(data.type)
    return bumper_cls(**data.kwargs())
