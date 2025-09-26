import logging
from mcp.server.fastmcp import FastMCP

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("WordCounter")


app = FastMCP("WordCounter")

@app.tool()
def count_sentence_words(sentence: str) -> str:
        """统计一句话的字数"""
        length = len(sentence)
        result = f"这句话是: {sentence}，字数: {length}"
        logger.info(result)
        return result


def run_server():
    app.run(transport="stdio")
