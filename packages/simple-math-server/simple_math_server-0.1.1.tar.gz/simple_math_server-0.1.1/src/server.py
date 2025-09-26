
from mcp.server.fastmcp import FastMCP

# 初始化MCP服务实例
app = FastMCP("demo-server")

# 添加工具：加法计算
@app.tool()
def add(a: int, b: int) -> int:
    """计算两个整数的和"""
    return a + b

# 添加工具：天气查询
@app.tool()
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    weather_data = {
        "北京": "晴，25℃",
        "上海": "多云，28℃",
        "广州": "雷阵雨，30℃",
        "Beijing": "晴，25℃",
        "Shanghai": "多云，28℃",
        "Guangzhou": "雷阵雨，30℃"
    }
    return weather_data.get(city, "暂不支持该城市")

def main():
    # 启动服务（stdio模式）
    app.run(transport='stdio')

if __name__ == "__main__":
    # 启动服务（stdio模式）
    app.run(transport='stdio')
