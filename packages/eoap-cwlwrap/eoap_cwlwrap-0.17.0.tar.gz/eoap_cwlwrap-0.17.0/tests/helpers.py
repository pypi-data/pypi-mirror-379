"""
EOAP CWLWrap (c) 2025

EOAP CWLWrap is licensed under
Creative Commons Attribution-ShareAlike 4.0 International.

You should have received a copy of the license along with this work.
If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.
"""

import os
import sys
import unittest
from cwltool.main import main as cwlmain
from cwltool.context import LoadingContext, RuntimeContext
from cwltool.executors import NoopJobExecutor
from cwl_loader import dump_cwl
from io import StringIO
from click.testing import CliRunner
from eoap_cwlwrap import wrap_locations
from pathlib import Path

class TestCWL(unittest.TestCase):

    def validate_cwl_file(self, cwl_file) -> int:
        args = ["--enable-ext", "--validate", cwl_file]

        stream_err = StringIO()
        stream_out = StringIO()

        result = cwlmain(
            args,
            stdout=stream_out,
            stderr=stream_err,
            executor=NoopJobExecutor(),
            loadingContext=LoadingContext(),
            runtimeContext=RuntimeContext(),
        )
        if result != 0:
            print(stream_out.getvalue(), file=sys.stderr)
            raise RuntimeError(f"Validation failed with exit code {result}")
        return result

    def setUp(self):
        self.output = '.wrapped.cwl'
        self.base_url = 'https://raw.githubusercontent.com/eoap/application-package-patterns/refs/heads/main'
        self.entrypoint = None

    def tearDown(self):
        if os.path.exists(self.output):
            os.remove(self.output)

    def _cwl_validation(self, app_cwl_file):
        return self.validate_cwl_file(app_cwl_file)

    def _wrapped_cwl_validation(self):
        directory_stage_in = f"{self.base_url}/templates/stage-in.cwl"
        file_stage_in = f"{self.base_url}/templates/stage-in-file.cwl"
        workflows_cwl = f"{self.base_url}/cwl-workflow/{self.entrypoint}.cwl"
        stage_out_cwl = f"{self.base_url}/templates/stage-out.cwl"

        main_workflow = wrap_locations(
            directory_stage_in=directory_stage_in,
            file_stage_in=file_stage_in,
            workflows=workflows_cwl,
            workflow_id=self.entrypoint, # type: ignore
            stage_out=stage_out_cwl
        )

        output_path = Path(self.output)
        with output_path.open("w") as f:
            dump_cwl(main_workflow, f)

        self.assertEqual(self._cwl_validation(self.output), 0)
