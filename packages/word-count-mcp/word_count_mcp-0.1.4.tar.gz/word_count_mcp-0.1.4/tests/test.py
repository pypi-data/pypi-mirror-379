import pytest
from word_count_mcp.server import count_sentence_words

def test_normal_sentence():
    s = "你好世界"
    result = count_sentence_words(s)
    print(result) 
    assert "字数: 4" in result
    assert "你好世界" in result
