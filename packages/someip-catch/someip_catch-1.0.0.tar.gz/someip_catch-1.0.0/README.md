# DiagProxy Python框架

基于DiagProxy架构的ECU诊断刷写框架的Python实现。

## 功能特性

- 完整的UDS诊断协议支持
- 模块化的诊断动作和用例架构
- VBF文件解析和处理
- 安全访问和数据传输管理
- ECU刷写流程控制

## 主要组件

- **基础接口**: IDiagAction/IDiagCase 接口定义
- **通信层**: DiagCommunication 通信管理
- **上下文管理**: DiagProxyContext 上下文控制
- **诊断动作**: 各种具体的诊断操作实现
- **诊断用例**: 完整的诊断场景实现
- **主控制器**: DiagProxy 核心控制逻辑

## 安装

```bash
pip install diag-pythoncode
```

## 基本使用

```python
from diag_pythoncode import DiagProxy, create_security_access_proxy

# 创建安全访问代理
proxy = create_security_access_proxy()

# 执行诊断操作
result = proxy.execute()
```

