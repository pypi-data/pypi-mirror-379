import togura.jpcoar as jpcoar
import pytest

def test_resource_type_uri():
  assert jpcoar.resource_type_uri("test") is None
  assert jpcoar.resource_type_uri("article") == "http://purl.org/coar/resource_type/c_6501"
