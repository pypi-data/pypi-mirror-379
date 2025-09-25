from typing import Any, Dict, Iterator, Literal, Optional
from .placeholder import Placeholder, AttributePlaceholder

class ConfigRef(Placeholder):
    """
    This class is used to provide a default value based on an other key for configuration.
    """
    __slots__ = ("key",)
    __add__ = AttributePlaceholder("__add__")
    __sub__ = AttributePlaceholder("__sub__")
    __mul__ = AttributePlaceholder("__mul__")
    __truediv__ = AttributePlaceholder("__truediv__")
    __floordiv__ = AttributePlaceholder("__floordiv__")
    __mod__ = AttributePlaceholder("__mod__")
    __pow__ = AttributePlaceholder("__pow__")
    __and__ = AttributePlaceholder("__and__")
    __or__ = AttributePlaceholder("__or__")
    __xor__ = AttributePlaceholder("__xor__")
    __lt__ = AttributePlaceholder("__lt__")
    __le__ = AttributePlaceholder("__le__")
    __eq__ = AttributePlaceholder("__eq__") # type: ignore
    __ne__ = AttributePlaceholder("__ne__") # type: ignore
    __gt__ = AttributePlaceholder("__gt__")
    __ge__ = AttributePlaceholder("__ge__")
    __contains__ = AttributePlaceholder("__contains__")
    __getitem__ = AttributePlaceholder("__getitem__")

    def __init__(self, key: str):
        self.key = key

    def __repr__(self) -> str:
        return f"ConfigRef('{self.key}')"

    def _is_relative(self) -> bool:
        """
        Check if the reference is relative.
        """
        return self.key.startswith(".")
    
    def _value(self, config: 'ConfigDict', default: Any = None) -> Any:
        """
        Get the value of the reference.
        """
        if self._is_relative():
            return config.get(self.key, default)
        else:
            return config.root.get(self.key, default)


class ConfigDict:
    """
    Configuration management for the application.
    This module provides functions to get, set, and update configuration values,
    to load from a file, and to save to a file.
    """
    def __init__(self, config_dict: Optional[Dict[str, Any]] = None, parent: Optional['ConfigDict'] = None, copy: bool = True) -> None:
        if copy and config_dict:
            self.config_dict = config_dict.copy()
        else:
            self.config_dict = config_dict or {}

        if parent:
            self.parent = parent
            self.root = parent.root
        else:
            self.parent = self.root = self
        
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get the value of a configuration key.
        If the key does not exist, return the default.
        """
        config = self

        while key.startswith(".."):
            config = config.parent
            key = key[1:]
        if key.startswith("."):
            key = key[1:]
        value = default
        parts = key.lower().replace("__dot__", ".").replace("__wildcard__", "*").replace("__", ".").split(".")
        not_found = object()
        for i, part in enumerate(parts):
            value = config.config_dict.get(part, not_found)

            if isinstance(value, Placeholder):
                value = value._value(config, not_found)
            
            if value is not_found:
                if "." in config.config_dict:
                    wildcard = config.config_dict["."]
                    if isinstance(wildcard, Placeholder):
                        wildcard = wildcard._value(config, {})
                    elif isinstance(wildcard, dict):
                        wildcard = ConfigDict(wildcard, config.parent, copy=False)

                    assert isinstance(wildcard, ConfigDict)
                    value = wildcard.get(part, not_found)
                    if isinstance(value, Placeholder):
                        value = value._value(config, not_found)
                elif self.parent is not self and "*" in config.parent.config_dict:
                    wildcard = config.parent.config_dict["*"]
                    if isinstance(wildcard, Placeholder):
                        wildcard = wildcard._value(config, {})
                    assert isinstance(wildcard, dict) or isinstance(wildcard, ConfigDict)
                    value = wildcard.get(part, not_found)

                    if isinstance(value, Placeholder):
                        value = value._value(config, not_found)
            
            if value is not_found:
                if "*" in self.config_dict:
                    value = self.config_dict["*"]
                    if isinstance(value, Placeholder):
                        value = value._value(config, value)
                    if isinstance(value, dict):
                        value = ConfigDict(value, config, copy=True)
                else:
                    return default

            if isinstance(value, dict):
                value = ConfigDict(value, config, copy=False)
            if isinstance(value, ConfigDict):
                config = value
            elif i < len(parts) - 1:
                # si la valeur n'est pas un dict, on ne peut pas descendre plus bas
                return default
        
        return value
    
    def set(self, key:str, value:Any) -> None:
        """
        Set the value of a configuration key.
        If the key already exists, update its value.
        """
        while key.startswith(".."):
            self = self.parent
            key = key[1:]
        if key.startswith("."):
            key = key[1:]

        # Normalize the flat key into dotted parts while preserving special tokens
        # Use placeholders to avoid creating accidental consecutive dots
        SENT_DOT = "\x00DOT\x00"
        SENT_WILD = "\x00WILD\x00"
        tmp = key.lower()
        tmp = tmp.replace("__dot__", SENT_DOT).replace("__wildcard__", SENT_WILD)
        tmp = tmp.replace("__", ".")
        parts = [p.replace(SENT_DOT, ".").replace(SENT_WILD, "*") for p in tmp.split(".") if p != ""]

        _config = self.config_dict
        for part in parts[:-1]:
            if part not in _config or not isinstance(_config[part], dict):
                _config[part] = {}
            _config = _config[part]
        _config[parts[-1]] = value

    def __contains__(self, key: str) -> bool:
        """
        Check if the configuration contains a key.
        """
        not_found = object()
        return self.get(key, not_found) is not not_found
    
    def __getitem__(self, key: str) -> Any:
        """
        Get the value of a configuration key.
        """
        not_found = object()
        result = self.get(key, not_found)
        if result is not not_found:
            return result
        raise KeyError(f"Key '{key}' not found in configuration.")
    
    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value of a configuration key.
        """
        self.set(key, value)
    
    def clear(self) -> None:
        """
        Clear the configuration.
        """
        self.config_dict.clear()
    
    def copy(self) -> 'ConfigDict':
        """
        Create a copy of the configuration.
        """
        return ConfigDict(self.config_dict, self.parent)
    
    def walk(self, prefix: str = ""):
        """
        Walk through the configuration dictionary and yield key-value pairs.
        """
        stack: list[tuple[dict[str, Any], str, 'ConfigDict']] = [(self.config_dict, prefix, self)]
        while stack:
            current_dict, current_prefix, current_config = stack.pop()
            for key, value in current_dict.items():
                if key == ".":
                    key = "__dot__"
                elif key == "*":
                    key = "__wildcard__"
                if isinstance(value, Placeholder):
                    value = value._value(current_config, None)
                if isinstance(value, dict):
                    stack.append((value, current_prefix + key + ".", ConfigDict(value, current_config, copy=False))) # type: ignore
                elif isinstance(value, ConfigDict):
                    stack.append((value.config_dict, current_prefix + key + ".", value))
                else:
                    yield current_prefix + key, value

    def to_dict(self):
        """
        Convert the configuration to a dictionary.
        """
        output_dict: dict[str, Any] = {}
        stack: list[tuple[dict[str, Any], dict[str, Any], 'ConfigDict']] = [(self.config_dict, output_dict, self)]
        while stack:
            current_dict, current_output_dict, current_config = stack.pop()
            for key, value in current_dict.items():
                if isinstance(value, Placeholder):
                    value = value._value(current_config, None)
                if isinstance(value, dict):
                    stack.append((value, current_output_dict.setdefault(key, {}), ConfigDict(value, current_config, copy=False))) # type: ignore
                elif isinstance(value, ConfigDict):
                    stack.append((value.config_dict, current_output_dict.setdefault(key, {}), value))
                else:
                    current_output_dict[key] = value
        return output_dict

    def keys(self, recursive: bool = False) -> list[str]:
        """
        Get the keys of the configuration.
        """
        if recursive:
            return [key for key, _ in self.walk()]
        return list(self.config_dict.keys())
    
    def items(self, recursive: bool = False) -> list[tuple[str, Any]]:
        """
        Get the items of the configuration.
        """
        if recursive:
            return list(self.walk())
        return list(self.config_dict.items())
    
    def values(self, recursive: bool = False) -> list[Any]:
        """
        Get the values of the configuration.
        """
        if recursive:
            return [value for _, value in self.walk()]
        return list(self.config_dict.values())
    
    def __iter__(self) -> Iterator[str]:
        """
        Iterate over the configuration dictionary.
        """
        return iter(self.config_dict)
    
    def __len__(self) -> int:
        """
        Get the length of the configuration dictionary.
        """
        return len(self.config_dict)
    
    def __repr__(self) -> str:
        """
        Get the string representation of the configuration dictionary.
        """
        return f"ConfigDict({self.config_dict})"
    

    def update(self, config_dict: Dict[str, Any], mode: Literal['simple', 'flat', 'recursive'] = 'simple') -> None:
        """
        Update the configuration.
        """
        if mode == 'flat':
            for key, value in config_dict.items():
                self.set(key, value)
        elif mode == 'recursive':
            stack = [(self.config_dict, config_dict)]
            while stack:
                current_dict, config_dict = stack.pop()
                for key, value in config_dict.items():
                    if isinstance(value, dict):
                        if key not in current_dict or not isinstance(current_dict[key], dict):
                            current_dict[key] = {}
                        stack.append((current_dict[key], value))
                    else:
                        current_dict[key] = value
        else:
            self.config_dict.update(config_dict)

    @staticmethod
    def from_env(prefix: str = "") -> 'ConfigDict':
        """
        Create a configuration from environment variables.
        """
        import os
        config_dict = ConfigDict()
        prefix = prefix.upper()
        config_dict.update({key.removeprefix(prefix): value for key, value in os.environ.items() if key.startswith(prefix)}, mode='flat')
        return config_dict
    
    @staticmethod
    def from_file(file_path: str) -> 'ConfigDict':
        """
        Create a configuration from a file.
        """
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            try:
                import yaml
            except ImportError:
                raise RuntimeError("Please install pyyaml (pythils[yaml]) to load yaml files.")
            with open(file_path, 'r') as f:
                config_dict = yaml.safe_load(f)
        elif file_path.endswith('.json'):
            import json
            with open(file_path, 'r') as f:
                config_dict = json.load(f)
        elif file_path.endswith('.py'):
            import importlib.util
            spec = importlib.util.spec_from_file_location("config", file_path)
            if spec is None or spec.loader is None:
                raise ImportError(f"Cannot import config from {file_path}")
            config_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config_module)
            if hasattr(config_module, 'config') and isinstance(config_module.config, dict):
                config_dict = config_module.config
            elif hasattr(config_module, 'config') and isinstance(config_module.config, ConfigDict):
                return config_module.config
            else:
                config_dict = {k: getattr(config_module, k) for k in dir(config_module) if not k.startswith("_")}
        elif file_path.endswith('.ini'):
            import configparser
            parser = configparser.ConfigParser()
            parser.read(file_path)
            # Build config using flat updates similar to .env
            cfg = ConfigDict()
            # Defaults -> top-level keys (flat)
            if parser.defaults():
                cfg.update(dict(parser.defaults()), mode='flat')
            # Sections -> nested dicts; we encode as section.<key>
            for section in parser.sections():
                if hasattr(parser, "_sections") and section in parser._sections:  # type: ignore[attr-defined]
                    items = dict(parser._sections[section])  # type: ignore[attr-defined]
                    items.pop('__name__', None)
                else:
                    # Remove default-derived items
                    defaults = parser.defaults()
                    items = {k: v for k, v in parser.items(section) if k not in defaults}
                for k, v in items.items():
                    # Reconstruct the key string with '.' separators, preserving tokens for set()
                    SENT_DOT = "\x00DOT\x00"
                    SENT_WILD = "\x00WILD\x00"
                    tmp = k.replace("__dot__", SENT_DOT).replace("__wildcard__", SENT_WILD)
                    tmp = tmp.replace("__", ".")
                    encoded = tmp.replace(SENT_DOT, "__dot__").replace(SENT_WILD, "__wildcard__")
                    cfg.set(f"{section}.{encoded}", v)
            return cfg
        elif file_path.endswith('.env'):
            try:
                from dotenv import dotenv_values
                flat = dotenv_values(file_path)
                cfg = ConfigDict()
                cfg.update(flat, mode='flat')
                return cfg
            except ImportError:
               raise RuntimeError("Please install dotenv (pythils[dotenv]) to load .env files.")
        elif file_path.endswith('.toml'):
            try:
                import toml
                with open(file_path, 'r') as f:
                    config_dict = toml.load(f)
            except ImportError:
                raise RuntimeError("Please install toml (pythils[toml]) to load .toml files.")
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
        return ConfigDict(config_dict)

    def to_file(self: 'ConfigDict', file_path: str, format: Optional[Literal['yaml', 'json', 'ini', 'env', 'toml', 'py']] = None) -> None:
        """
        Save the configuration to a file.
        """
        data = self.to_dict()
        if format == 'yaml' or (format is None and (file_path.endswith('.yaml') or file_path.endswith('.yml'))):
            try:
                import yaml
            except ImportError:
                raise RuntimeError("Please install pyyaml (pythils[yaml]) to save yaml files.")
            with open(file_path, 'w') as f:
                yaml.safe_dump(data, f)
        elif format == 'json' or (format is None and file_path.endswith('.json')):
            import json
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        elif format == 'ini' or (format is None and file_path.endswith('.ini')):
            import configparser
            parser = configparser.ConfigParser()
            def encode_segment(seg: str) -> str:
                if seg == '.':
                    return '__dot__'
                if seg == '*':
                    return '__wildcard__'
                return seg
            for section, values in data.items():
                if isinstance(values, dict):
                    # Flatten nested dicts into __-joined keys using tokens for special keys
                    flat: Dict[str, str] = {}
                    stack: list[tuple[Dict[str, Any], list[str]]] = [(values, [])]
                    while stack:
                        current, path = stack.pop()
                        for k, v in current.items():
                            seg = encode_segment(k)
                            if isinstance(v, dict):
                                stack.append((v, path + [seg]))
                            else:
                                key_name = '__'.join(path + [seg]) if path or seg else seg
                                flat[key_name] = str(v)
                    parser[section] = flat
                else:
                    parser['DEFAULT'][section] = str(values)
            with open(file_path, 'w') as f:
                parser.write(f)
        elif format == 'env' or (format is None and file_path.endswith('.env')):
            with open(file_path, 'w') as f:
                for k, v in self.walk():
                    f.write(f"{k.upper().replace('.', '__')}={v}\n")
        elif format == 'toml' or (format is None and file_path.endswith('.toml')):
            try:
                import toml
            except ImportError:
                raise RuntimeError("Please install toml (pythils[toml]) to save .toml files.")
            with open(file_path, 'w') as f:
                toml.dump(data, f)
        elif format == 'py' or (format is None and file_path.endswith('.py')):
            with open(file_path, 'w') as f:
                f.write("config = ")
                import pprint
                pprint.pprint(data, stream=f)
        else:
            raise ValueError(f"Unsupported file format: {format or file_path}")