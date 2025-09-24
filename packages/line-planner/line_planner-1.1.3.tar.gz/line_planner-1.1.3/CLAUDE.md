# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

**SIF航线规划器 - 简化版**

这是一个专为SIF（Solar-Induced Fluorescence）单点光谱设备优化的简化航线规划器。项目采用独立实现架构，从KML边界文件生成蛇形航线拐点，专为无人机飞行控制设计。

## 项目特点

- **简化架构**: 删除了复杂的API层，只保留核心功能
- **独立实现**: 使用standalone模式，无外部依赖复杂性
- **标准输入**: 通过JSON配置进行航线规划
- **内置可视化**: 集成matplotlib生成航线图像
- **一键运行**: 通过`interface.py`统一入口

## 开发环境与工具

### 包管理器
- 使用 `uv` 管理Python环境和依赖
- 运行Python代码：`uv run python <script.py>`
- 安装开发依赖：`uv sync --dev`

### 核心命令

#### 构建与安装
```bash
# 开发模式安装
uv pip install -e .
# 安装开发依赖
uv pip install -e ".[dev]"
```

#### 代码质量检查
```bash
# 代码格式化
uv run black src/
uv run isort src/

# 类型检查
uv run mypy src/

# 代码检查
uv run flake8 src/
```

#### 测试
```bash
# 主要功能测试
echo '{"kml_file":"test.kml","line_spacing":25,"rotation_angle":0,"save_dir":"./output"}' | uv run python interface.py

# 通过配置文件测试
echo "test.json" | uv run python interface.py
```

## 项目架构

### 简化架构模式
项目采用简化的单一流程架构：

```
interface.py → line_planner.main → stdin_processor → standalone → 输出结果
```

**核心模块（简化后）:**

1. **入口层**
   - `interface.py` - 主要程序入口，处理标准输入

2. **控制层 (`src/line_planner/`)**
   - `main.py` - 主程序逻辑，路由到独立实现
   - `api/stdin_processor.py` - 标准输入处理和结果输出

3. **核心层 (`src/line_planner/core/`)**
   - `standalone.py` - 独立实现，包含所有核心功能
     - `StandaloneBoundaryParser` - KML解析
     - `StandalonePlanner` - 航线规划算法
     - 内置可视化功能

### 数据流架构
```
JSON配置 → 独立解析器 → 独立规划器 → 航线拐点 → 多格式输出+可视化
```

### 简化设计原则
- **独立实现**: 所有功能集成在standalone模块中
- **标准输入**: 通过JSON配置驱动
- **内置可视化**: 集成matplotlib生成图像
- **一体化输出**: 同时生成JSON、图像、日志

## 主要入口点

### 标准使用方式
```bash
# 直接JSON配置
echo '{"kml_file":"test.kml","line_spacing":25,"rotation_angle":0,"save_dir":"./output"}' | uv run python interface.py

# 通过配置文件
echo "test.json" | uv run python interface.py

# Windows下的等效命令
type test.json | python interface.py
```

### 配置文件格式
```json
{
  "kml_file": "test.kml",
  "line_spacing": 25,
  "rotation_angle": 0,
  "save_dir": "./output"
}
```

## 配置文件

### 关键配置文件
- `pyproject.toml` - 项目配置、依赖管理、开发工具配置
- `uv.lock` - 依赖锁定文件
- `test.json` - 测试配置文件示例

### 开发工具配置
项目在pyproject.toml中配置了：
- Black代码格式化（行长度100）
- isort导入排序
- mypy类型检查（严格模式）
- matplotlib, numpy等科学计算依赖

## 核心数据结构

### 规划结果格式
```json
{
  "success": true,
  "turn_points": [
    {"lat": 39.904200, "lon": 116.407400, "type": "start", "index": 0}
  ],
  "statistics": {
    "total_points": 12,
    "total_distance_km": 2.450,
    "estimated_flight_time_10ms_min": 4.1
  },
  "parameters": {
    "line_spacing": 20.0,
    "rotation_angle": 0.0
  }
}
```

## 算法核心

### 航线生成算法
1. **边界扫描**: 按指定间距生成水平扫描线
2. **交点计算**: 计算扫描线与多边形边界的交点
3. **拐点提取**: 每条航线只保留起点和终点
4. **蛇形优化**: 奇偶行交替方向

### 坐标转换
- 输入WGS84经纬度 → 局部米制坐标系 → 航线旋转 → 生成拐点 → 转换回WGS84

## 输出格式

自动生成多种输出文件：
- **coordinates.json**: 航线坐标数据
- **result.json**: 完整的规划结果和统计信息
- **flight_plan.png**: 可视化航线图像（自动生成）
- **processing.log**: 处理过程日志

### 输出目录结构
```
output/
└── sif_planning_20250922_105239/
    ├── coordinates.json    # 坐标数据
    ├── result.json        # 完整结果
    ├── flight_plan.png    # 可视化图像
    └── processing.log     # 处理日志
```

## 测试策略

### 简化测试方法
```bash
# 基本功能测试
echo '{"kml_file":"test.kml","line_spacing":25,"rotation_angle":0}' | uv run python interface.py

# 参数变化测试
echo '{"kml_file":"test.kml","line_spacing":50,"rotation_angle":45}' | uv run python interface.py

# 文件路径测试
echo "test.json" | uv run python interface.py
```

### 验证标准
- 输出JSON格式正确
- 生成可视化图像
- 航线拐点数量合理
- 蛇形路径优化正确

## 专业领域知识

### SIF设备特点
- 单点光谱测量，需要精确的拐点控制
- 适用于农业遥感、环境监测等场景
- 要求高精度的航线规划和稳定的飞行路径

### 航线优化原则
- 最小化转弯次数，提高飞行效率
- 保持航线间距一致性，确保数据质量
- 支持航线旋转，适应不同地形和风向条件

## 项目简化历史

### 简化原因
- 原项目包含复杂的API层和多个冗余模块
- 实际使用中只需要标准输入的简单模式
- 独立实现已经包含所有必要功能

### 删除的模块
- `src/line_planner/api/simple_api.py` - 复杂API接口
- `src/line_planner/core/planner.py` - 标准规划器
- `src/line_planner/core/boundary_parser.py` - 标准解析器
- `src/line_planner/utils/visualization.py` - 外部可视化工具

### 简化效果
- **代码减少**: 删除约1000+行代码
- **维护性提高**: 只需维护独立实现
- **性能优化**: 无复杂模块依赖
- **使用简化**: 一行命令完成航线规划

## 重要提醒

⚠️ **架构已简化** - 项目已删除标准API模式，只保留独立实现。
✅ **推荐使用方式** - 通过 `echo 'config' | python interface.py` 使用。
🔧 **核心模块** - 所有功能集中在 `standalone.py` 中。