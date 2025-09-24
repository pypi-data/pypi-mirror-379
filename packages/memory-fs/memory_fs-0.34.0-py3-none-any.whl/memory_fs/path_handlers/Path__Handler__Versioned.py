from memory_fs.path_handlers.Path__Handler                                         import Path__Handler
from osbot_utils.type_safe.primitives.domains.identifiers.safe_str.Safe_Str__Id                  import Safe_Str__Id
from osbot_utils.type_safe.primitives.domains.files.safe_str.Safe_Str__File__Path  import Safe_Str__File__Path


class Path__Handler__Versioned(Path__Handler):                                          # Handler that stores files with version numbers
    current_version : int     = 1                                                        # Current version number
    name            : Safe_Str__Id = Safe_Str__Id("versioned")
    version_prefix  : str     = "v"                                                      # Prefix for version folder

    def generate_path(self, file_id  : Safe_Str__Id              = None,                     # not used by this path handler
                            file_key : Safe_Str__File__Path = None                      # not used by this path handler
                       ) -> Safe_Str__File__Path:                                       # Generate versioned path
        version_folder = f"{self.version_prefix}{self.current_version}"
        return self.combine_paths(version_folder)

    def increment_version(self) -> 'Path__Handler__Versioned':                           # Increment version number
        self.current_version += 1
        return self

    def set_version(self, version : int                                                  # Set specific version
                   ) -> 'Path__Handler__Versioned':
        self.current_version = version
        return self