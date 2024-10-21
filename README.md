# pytest-result_sender


## 第三天：测开平台之持续集成自动部署篇
### 1.为插件提供配置的功能
1.什么时候发送

### 2.添加配置

### 3.识别配置
```
pytest_addoption(parser):
```
### 4.使用配置
```
使用钩子pytest_configure
```
## 2.补全测试用例
为谁编写测试？
1.为插件
2.为pytest
> 插件不能脱离pytest单独运行

### 1.pytest如何测试pytest
git控制自己的代码的版本：git管理git
linux编译自己的代码：linux编译linux

pytest核心、特色：
- fixture： pytester
- hook