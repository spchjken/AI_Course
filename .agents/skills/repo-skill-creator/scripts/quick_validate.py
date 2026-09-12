#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
"""

import re
import sys
from pathlib import Path

import yaml

MAX_SKILL_NAME_LENGTH = 64
MIN_SHORT_DESCRIPTION_LENGTH = 25
MAX_SHORT_DESCRIPTION_LENGTH = 64


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    allowed_properties = {"name", "description", "license", "allowed-tools", "metadata"}

    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        allowed = ", ".join(sorted(allowed_properties))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). "
                f"Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
            )
        if skill_path.name != name:
            return (
                False,
                f"Skill folder '{skill_path.name}' must match frontmatter name '{name}'",
            )

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return (
                False,
                f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
            )

    openai_yaml = skill_path / "agents" / "openai.yaml"
    if openai_yaml.exists():
        try:
            openai_config = yaml.safe_load(openai_yaml.read_text())
        except yaml.YAMLError as e:
            return False, f"Invalid agents/openai.yaml: {e}"

        if not isinstance(openai_config, dict):
            return False, "agents/openai.yaml must be a YAML dictionary"

        interface = openai_config.get("interface")
        if not isinstance(interface, dict):
            return False, "agents/openai.yaml must contain an interface mapping"

        short_description = interface.get("short_description")
        if short_description is not None:
            if not isinstance(short_description, str):
                return False, "interface.short_description must be a string"
            if not (
                MIN_SHORT_DESCRIPTION_LENGTH
                <= len(short_description)
                <= MAX_SHORT_DESCRIPTION_LENGTH
            ):
                return (
                    False,
                    "interface.short_description must be 25-64 characters "
                    f"(got {len(short_description)})",
                )

        default_prompt = interface.get("default_prompt")
        if default_prompt is not None:
            if not isinstance(default_prompt, str):
                return False, "interface.default_prompt must be a string"
            invocation = f"${name}"
            if invocation not in default_prompt:
                return (
                    False,
                    f"interface.default_prompt must mention '{invocation}'",
                )

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
