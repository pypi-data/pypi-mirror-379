from mcp.server.fastmcp import FastMCP
import sys
import logging

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 日志级别: DEBUG / INFO / WARNING / ERROR
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("word_count.log", encoding="utf-8"),  # 保存到文件
        logging.StreamHandler(sys.stdout)  # 同时打印到控制台
    ]
)
logger = logging.getLogger("WordCounter")

app = FastMCP("WordCounter")

@app.tool()
def count_sentence_words(sentence: str) -> str:
    """
    统计一句话的字数。
    参数:
      - sentence: 用户说的一句话
    """
    length = len(sentence)
    result = f"这句话是: {sentence}，字数: {length}"

    # 记录日志
    logger.info(f"用户输入: {sentence} | 字数统计: {length}")

    return result

if __name__ == "__main__":
    app.run(transport="stdio")
