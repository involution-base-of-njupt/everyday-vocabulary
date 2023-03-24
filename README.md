# 背单词系统

## 流程图

```mermaid
graph LR

Sys(背单词系统) --> gui[图形化界面]
Sys --> cli[命令行交互界面]
cli --> gui
gui --> Admin[管理员]
gui --> User[用户]
cli --> Admin[管理员]
cli --> User[用户]

Admin --> 文件导入
Admin --> 单词添加
Admin --> 单词删除
Admin --> 单词修改
Admin --> 单词搜索
Admin --> 单词展示

Admin --> 密码修改
User --> 密码修改

User --> 单词搜索
User --> 单词展示
User --> 英译汉测试
User --> 汉译英测试
User --> 错词本测试

错词本测试 --> s[单词搜索]
错词本测试 --> d[单词删除]
```

## 运行

```shell
python -m pip install -r requirements.txt # 安装依赖
python __init__.py
```

## 构建

```shell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt # 安装依赖
python -m pip install nuitka # 安装nuitka来构建
python -m nuitka --onefile --standalone --enable-plugin=pyqt5 --output-dir=build __init__.py # 构建
```
