import os
import tempfile
import unittest
import importlib.util

from pythils.config import ConfigDict, ConfigRef


def _has_module(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def make_sample_config() -> ConfigDict:
    return ConfigDict({
        'base_key': 'base_value',
        'ref_key': ConfigRef('base_key'),
        'dot_ref': {
            'dot_key': 'dot_value'
        },
        'wild_ref': {
            'wild_key': 'wild_value',
        },
        '*': ConfigRef('wild_ref'),
        'nested': {
            '.': ConfigRef('dot_ref'),
            'nested_key': 'nested_value',
            'ref_to_parent': ConfigRef('..base_key'),
            'ref_to_self': ConfigRef('.nested_key'),
            'ref_to_root': ConfigRef('base_key')
        }
    })


class TestSaveLoadFormats(unittest.TestCase):
    def compare_walk_sets(self, a: ConfigDict, b: ConfigDict):
        sa = set(a.walk())
        sb = set(b.walk())
        if sa != sb:
            missing = sa - sb
            extra = sb - sa
            self.fail(f"Walk sets differ. Missing: {missing}\nExtra: {extra}")

    @unittest.skipUnless(_has_module('yaml'), 'pyyaml not installed')
    def test_yaml_roundtrip(self):
        cfg = make_sample_config()
        with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as f:
            path = f.name
        try:
            cfg.to_file(path)
            loaded = ConfigDict.from_file(path)
            self.compare_walk_sets(cfg, loaded)
        finally:
            os.unlink(path)

    def test_ini_roundtrip(self):
        cfg = make_sample_config()
        with tempfile.NamedTemporaryFile(suffix='.ini', delete=False) as f:
            path = f.name
        try:
            cfg.to_file(path)
            loaded = ConfigDict.from_file(path)
            self.compare_walk_sets(cfg, loaded)
        finally:
            os.unlink(path)

    @unittest.skipUnless(_has_module('dotenv'), 'python-dotenv not installed')
    def test_env_roundtrip(self):
        cfg = make_sample_config()
        with tempfile.NamedTemporaryFile(suffix='.env', delete=False) as f:
            path = f.name
        try:
            cfg.to_file(path)
            loaded = ConfigDict.from_file(path)
            self.compare_walk_sets(cfg, loaded)
        finally:
            os.unlink(path)

    @unittest.skipUnless(_has_module('toml'), 'toml not installed')
    def test_toml_roundtrip(self):
        cfg = make_sample_config()
        with tempfile.NamedTemporaryFile(suffix='.toml', delete=False) as f:
            path = f.name
        try:
            cfg.to_file(path)
            loaded = ConfigDict.from_file(path)
            self.compare_walk_sets(cfg, loaded)
        finally:
            os.unlink(path)

    def test_py_roundtrip(self):
        cfg = make_sample_config()
        with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
            path = f.name
        try:
            cfg.to_file(path)
            loaded = ConfigDict.from_file(path)
            self.compare_walk_sets(cfg, loaded)
        finally:
            os.unlink(path)


if __name__ == '__main__':
    unittest.main()
