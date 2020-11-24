"""Tests for web app."""
import os
from pathlib import Path
from unittest import TestCase

from api.app import app

os.environ["CUDA_VISIBLE_DEVICES"] = ""

REPO_DIRNAME = Path(__file__).parents[2].resolve()
SUPPORT_DIRNAME = REPO_DIRNAME / "model_core" / "tests" / "support" /


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get("/")
        assert response.get_data().decode() == "Hello, world!"

    def test_predict(self):
       """Write your own tests """ 
