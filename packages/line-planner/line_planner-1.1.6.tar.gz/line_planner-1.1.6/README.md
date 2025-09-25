# LinePlanner - SIF航线规划器

基于v1.1.0的简化版本，专注稳定性和性能。

## 快速开始

### 标准输入模式（推荐）

```bash
# 直接JSON配置
echo '{"kml_file":"boundary.kml","line_spacing":25,"rotation_angle":0,"save_dir":"./output"}' | uv run python interface.py

# 通过配置文件
echo "config.json" | uv run python interface.py
```

### 安装使用

```bash
# 从PyPI安装
pip install line-planner

# 使用uv安装（推荐）
uv add line-planner
```

## 主要特点

- ✅ **简化架构**: 从1896行代码简化到388行，删除复杂功能
- ✅ **稳定可靠**: 基于经过验证的v1.1.0版本
- ✅ **性能优化**: 运行速度快，内存占用低
- ✅ **URL支持**: 支持从HTTP/HTTPS链接下载KML文件
- ✅ **蛇形路径**: 自动优化的飞行路径生成
- ✅ **内置可视化**: 自动生成航线图像

## 配置示例

```json
{
  "kml_file": "boundary.kml",
  "line_spacing": 25,
  "rotation_angle": 0,
  "save_dir": "./output"
}
```

## Python API

```python
from line_planner import StandalonePlanner, StandaloneBoundaryParser

# 解析KML边界
parser = StandaloneBoundaryParser()
lats, lons = parser.parse_kml_coordinates("boundary.kml")

# 规划航线
planner = StandalonePlanner()
turn_points = planner.plan_flight_lines(
    boundary_lats=lats,
    boundary_lons=lons,
    line_spacing=25.0,
    rotation_angle=0.0
)
```

## 开发

```bash
# 克隆项目
git clone https://github.com/1034378361/WayPointPlanning3.git
cd WayPointPlanning3

# 安装依赖
uv sync --dev

# 运行测试
echo '{"kml_file":"test.kml","line_spacing":25,"rotation_angle":0,"save_dir":"./test_output"}' | uv run python interface.py
```

## 许可证

MIT License