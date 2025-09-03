from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class GitignoreBuildHook(BuildHookInterface):
    PLUGIN_NAME = "gitignore_handler"

    def initialize(self, _version, _build_data):
        """Temporarily modify .gitignore so data is included when the sdist is installed using pip. """

        gi = Path('.gitignore')
        if gi.exists():
            cleaned = gi.read_text().replace('geonamescache/data/', '')
            # On Windows .gitignore.tmp may already exist and cause an error, when calling rename.
            Path('.gitignore.tmp').unlink(missing_ok=True)
            gi.rename('.gitignore.tmp')
            Path('.gitignore').write_text(cleaned)


    def finalize(self, _version, _build_data, _artifact):
        gi = Path('.gitignore.tmp')
        if gi.exists():
            # On Windows .gitignore may already exist and cause an error, when calling rename.
            Path('.gitignore').unlink(missing_ok=True)
            gi.rename('.gitignore')
