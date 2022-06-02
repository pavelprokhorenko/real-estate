
import pytest
from fastapi import status
from fastapi.testclient import TestClient


pytestmark = pytest.mark.usefixtures("use_postgres")

