import litellm

def test_validate_environment_zai_missing_key(monkeypatch):
    monkeypatch.delenv("ZAI_API_KEY", raising=False)
    out = litellm.validate_environment(model="zai/test-model")
    assert out["keys_in_environment"] is False
    assert "ZAI_API_KEY" in out["missing_keys"]
