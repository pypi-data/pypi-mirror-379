from jupyter_ai_debugger import AIDebugger

def test_import():
    dbg = AIDebugger(api_key="dummy_key", models=["x-ai/grok-4-fast:free"])
    assert dbg.models[0] == "x-ai/grok-4-fast:free"
