import os
import shutil
from unittest.mock import patch, MagicMock
from pathlib import Path

from techlens_agent.agent import Agent
from techlens_agent.config import Config
from techlens_agent.utils.utils import DebugLog

file_path = Path(__file__)
test_folder = file_path.parent.absolute()
results_dir = test_folder.joinpath("results").absolute()
str_path = str(test_folder.joinpath("str_conf.yaml").absolute())


@patch("techlens_agent.agent.requestx.get")
@patch("techlens_agent.agent.requestx.post")
@patch("techlens_agent.upload.Uploader.make_upload_path")
@patch("techlens_agent.user.__get_input__", return_value="y")
def test_no_config_with_mocks(mock_input, mock_make_upload, mock_post, mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = "mocked_scan_id"
    mock_resp.json.return_value = {}
    mock_get.return_value = mock_resp
    mock_post.return_value = mock_resp
    mock_make_upload.side_effect = (
        lambda path_type, report, code=None, repo_name=None: f"/mocked/path/{path_type}"
    )

    shutil.rmtree(results_dir, ignore_errors=True)
    os.makedirs(results_dir, exist_ok=True)

    agent = Agent()
    config = Config(str_path)
    config.output_dir = results_dir
    config.dry = False
    config.shouldUpload = True
    config.modules.code = ["mock_repo"]
    agent.config = config
    agent.debug = DebugLog(path=agent.config.output_dir, debug=False)
    agent.log = agent.debug.log
    agent.uploader.config = config.upload_conf

    agent.scan()

    assert Path(results_dir).exists()
    assert results_dir.joinpath("log.txt").exists()
    assert Path(results_dir, "results.html").exists()

    mock_get.assert_called_once()
    mock_make_upload.assert_called_with("scan_id", report=config.reportId)

    with open(results_dir.joinpath("log.txt"), "r") as f:
        log_content = f.read()
    assert "Report Run Id Fetch" in log_content
    assert "Report Run Id" in log_content
    assert "Finished" in log_content
