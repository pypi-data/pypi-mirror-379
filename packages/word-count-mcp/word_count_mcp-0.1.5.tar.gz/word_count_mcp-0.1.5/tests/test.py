import pytest
from word_count_mcp.server import count_sentence_words, run_server

def test_count_sentence_words():
    sentence = "你好世界"
    result = count_sentence_words(sentence)
    assert "字数: 4" in result

def test_run_server_startup(monkeypatch):
    """
    模拟启动 MCP 服务器。这里只测试函数是否能调用，不真正运行死循环。
    """
    called = {}

    def fake_run(transport):
        called["transport"] = transport

    # 替换 app.run 方法
    from word_count_mcp import server
    monkeypatch.setattr(server.app, "run", fake_run)

    server.run_server()
    assert called["transport"] == "stdio"
