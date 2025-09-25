import sys

import pytest
from click.testing import CliRunner

from mio.cli.config import config, _list
from mio.cli.stream import capture
from mio import Config
from mio.utils import hash_video
from mio.models import config as _config_mod
from .conftest import CONFIG_DIR

from .conftest import DATA_DIR


@pytest.mark.skip("Needs to be implemented")
def test_cli_stream():
    """should be able to invoke streamdaq, using various capture options"""
    pass


def test_cli_config_show():
    """
    `mio config` should show current config
    """
    runner = CliRunner()
    result = runner.invoke(config)
    cfg_yaml = Config().to_yaml()
    assert cfg_yaml in result.output


def test_cli_config_show_global():
    """
    `mio config global` should show contents of the global config file
    """
    runner = CliRunner()
    result = runner.invoke(config, ["global"])
    cfg_yaml = _config_mod._global_config_path.read_text()
    assert str(_config_mod._global_config_path) in result.output
    assert cfg_yaml in result.output


def test_cli_config_global_path():
    """
    `mio global path` should show the path to the global config file
    """
    runner = CliRunner()
    result = runner.invoke(config, ["global", "path"])
    assert str(_config_mod._global_config_path) in result.output


def test_cli_config_user_show(set_user_yaml):
    """
    `mio config user` should show contents of the user config file
    """
    user_yaml_path = set_user_yaml({"logs": {"level": "WARNING"}})
    runner = CliRunner()
    result = runner.invoke(config, ["user"])
    user_config = user_yaml_path.read_text()
    assert "level: WARNING" in user_config
    assert user_config in result.output


@pytest.mark.parametrize("clean", [True, False])
@pytest.mark.parametrize("dry_run", [True, False])
def test_cli_config_user_create(clean, dry_run, tmp_path):
    """
    `mio config user create` creates a new user config file,
    optionally with clean/dirty mode or dry_run or not
    """
    dry_run_cmd = "--dry-run" if dry_run else "--no-dry-run"
    clean_cmd = "--clean" if clean else "--dirty"

    config_path = tmp_path / "mio_config.yaml"

    runner = CliRunner()
    result = runner.invoke(config, ["user", "create", dry_run_cmd, clean_cmd, str(config_path)])

    if dry_run:
        assert "DRY RUN" in result.output
        assert not config_path.exists()
    else:
        assert "DRY RUN" not in result.output
        assert config_path.exists()

    if clean:
        assert "level" not in result.output
    else:
        assert "level" in result.output

    assert f"user_dir: {str(config_path.parent)}" in result.output


def test_cli_config_user_path(set_env, set_user_yaml):
    """
    `mio config user path` should show the path to the user config file
    """
    user_config_path = set_user_yaml({"logs": {"level": "WARNING"}})

    runner = CliRunner()
    result = runner.invoke(config, ["user", "path"])
    assert str(user_config_path) in result.output


def test_cli_config_list():
    """
    mio config list should list all the configs in the user directory and provided by mio
    """
    runner = CliRunner()
    result = runner.invoke(_list, color=False)

    # not testing for the literal table structure, but we should have headers and some table characters
    for header_substr in ("id", "mio_model", "path"):
        assert header_substr in result.output

    if sys.platform == "win32":
        assert "\u2500" in result.output
    else:
        assert "━━" in result.output

    # configs from the temporarily configured test config directory should be included
    assert "test-wireless-200px" in result.output

    # and configs provided by mio
    assert "wirefree-sd-layout" in result.output

    # by default paths and mio models should be truncated
    if sys.platform == "win32":
        assert "\u2502 .sdcard.SDLayout" in result.output
        assert "\u2502 wirefree" in result.output
    else:
        assert "│ .sdcard.SDLayout" in result.output
        assert "│ wirefree/" in result.output

    # verbose should display the full values (though truncated in testing because console width is 80)
    result = runner.invoke(_list, ["-v"], color=False)
    assert "mio.models." in result.output
    assert str(CONFIG_DIR)[0:5] in result.output


@pytest.mark.timeout(30)
@pytest.mark.parametrize(
    "freq_mask_config, video_hash",
    [
        (None, "f7ca12006595f18922380937bf6fc28376ed48976b050dbbd5529c1803dcda2f"),
    ],
)
def test_cli_capture(
    freq_mask_config,
    video_hash: str,
    tmp_path,
    set_okdev_input,
):
    """
    Basic regression test to ensure that we can in fact call the capture cli method,
    even though it's just a wrapper of the capture method.
    """
    runner = CliRunner()
    path_stem = tmp_path / "data"
    data_file = DATA_DIR / "stream_daq_test_fpga_raw_input_200px.bin"
    set_okdev_input(data_file)
    args = ["--device_config", "test-wireless-200px", "--output", str(path_stem), "--no-display"]

    # bit of a ghost parameterization -
    # left as placeholder in case we want to test freq mask display
    if freq_mask_config:
        args.append("--freq_mask_config")
        args.append(freq_mask_config)

    result = runner.invoke(capture, args)
    assert result.exit_code == 0
    output_hash = hash_video(path_stem.with_suffix(".avi"))
    assert output_hash == video_hash
