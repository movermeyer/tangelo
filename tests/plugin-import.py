import fixture
import json


moduletest = {"name": "moduletest",
              "path": "tests/plugins/moduletest"}
pluginorder = {"name": "pluginorder",
               "path": "tests/plugins/pluginorder"}


def test_plugin_module():
    config = {"plugins": [{
        "name": "moduletest",
        "path": "tests/plugins/moduletest"
    }]}
    (_, _, stderr) = fixture.run_tangelo("--config", json.dumps(config), timeout=3, terminate=True)
    stderr = "\n".join(stderr)

    assert "Plugin has value server.TestConstant True" in stderr


def test_plugin_single_file():
    config = {"plugins": [{
        "name": "pythonfile",
        "path": "tests/plugins/pythonfile"
    }]}
    (_, _, stderr) = fixture.run_tangelo("--config", json.dumps(config), timeout=3, terminate=True)
    stderr = "\n".join(stderr)

    assert "Python file plugin" in stderr


def test_plugin_order_good():
    config = {"plugins": [moduletest,
                          pluginorder]}

    (_, _, stderr) = fixture.run_tangelo("--config", json.dumps(config), timeout=3, terminate=True)
    stderr = "\n".join(stderr)

    assert "Plugin can reference tangelo.plugin.moduletest True" in stderr


def test_plugin_order_bad():
    config = {"plugins": [pluginorder,
                          moduletest]}

    (_, _, stderr) = fixture.run_tangelo("--config", json.dumps(config), timeout=3, terminate=True)
    stderr = "\n".join(stderr)

    assert "Plugin pluginorder failed to load" in stderr
