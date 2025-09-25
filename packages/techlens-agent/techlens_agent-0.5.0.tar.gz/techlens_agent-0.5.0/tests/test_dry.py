from unittest.mock import patch
from techlens_agent.agent import Agent
from techlens_agent.config import Config
from techlens_agent.utils.utils import DebugLog
from pathlib import Path
import shutil, os

file_path = Path(__file__)
test_folder = file_path.parent.absolute()
results_dir = test_folder.joinpath("results").absolute()
str_path = str(test_folder.joinpath("str_conf.yaml").absolute())


@patch("techlens_agent.agent.requestx.get")
@patch("techlens_agent.agent.requestx.post")
@patch("techlens_agent.upload.Uploader.make_upload_path")
@patch("techlens_agent.user.__get_input__", return_value="y")
def test_no_config(mock_input, mock_make_upload, mock_post, mock_get):
    mock_make_upload.side_effect = (
        lambda path_type, report, code=None, repo_name=None: f"/mocked/path/{path_type}"
    )
    mock_resp = type(
        "MockResponse",
        (),
        {"status_code": 200, "text": "mocked_text", "json": lambda: {}},
    )()
    mock_get.return_value = mock_resp
    mock_post.return_value = mock_resp

    shutil.rmtree(results_dir, ignore_errors=True)
    os.makedirs(results_dir, exist_ok=True)

    agent = Agent()
    config = Config(str_path)
    config.output_dir = results_dir
    agent.config = config
    agent.config.dry = True
    agent.config.shouldUpload = True
    agent.debug = DebugLog(path=agent.config.output_dir, debug=False)
    agent.log = agent.debug.log
    agent.uploader.config = config.upload_conf

    get_url = agent.uploader.make_upload_path("scan_id", report=agent.config.reportId)
    assert get_url == "/mocked/path/scan_id"

    agent.scan()

    assert "/log.txt" in agent.debug.file
    with open(agent.debug.file) as f:
        logText = f.read()
    assert "Error" not in logText
    assert "File does not exist:" in logText

    upload_fail_prefix = "File does not exist: " + str(results_dir) + "/"
    expected_files = [
        "small-test-repo.git.git.log.json",
        "small-test-repo.git.sizes.json",
        "small-test-repo.git.stats.json",
        "small-test-repo.git.findings.json",
        "small-test-repo.git.dependencies.json",
    ]
    for fname in expected_files:
        assert upload_fail_prefix + fname in logText
