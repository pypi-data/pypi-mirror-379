# 📖 Guide

## 1️⃣ Install

1. install `brew`: https://brew.sh/

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. install `pipx`

```
brew install pipx
pipx ensurepath
```

3. install `v-cr`

```
方式一：安装 PyPI 远程仓库包
pipx install v-magic-code-review

方式二（推荐）：安装本地项目包
# 进入你的项目根目录
cd /path/to/your/v-magic-code-review

# 使用可编辑模式(-e)安装
pipx install -e .
```

## 2️⃣ Setup environment variables

### 基础环境变量

设置以下环境变量，可直接写入到 ~/.zshrc 里：

```shell
# jira
export JIRA_HOST=https://jira.********.com
export JIRA_TOKEN=OTY**************************Y4

# confluence
export CONFLUENCE_HOST=https://wiki.********.com
export CONFLUENCE_TOKEN=MDQ2**************************1u

# gitlab
export GITLAB_HOST=https://gitlab.********.com
export GITLAB_TOKEN=_PH*****************UiW
```

如何获取这些变量：

| Variable                             | How to Get                                                                                       |
|--------------------------------------|--------------------------------------------------------------------------------------------------|
| `JIRA_TOKEN`                         | Go to Jira → 右上角头像点击 Profile → Personal Access Tokens → Create token                             |
| `CONFLUENCE_TOKEN`                   | Go to Confluence → 右上角头像点击 Settings → Personal Access Tokens → Create token                      |
| `GITLAB_TOKEN`                       | Go to GitLab → 左上角头像点击 Preferences → Access Tokens → Add new token                               |

### Gemini Cookie

Gemini Cookie 可以手动配置，也可以自动获取，下面列出这两种方法

#### 自动获取（推荐）

在浏览器中登陆 Gemini 后，使用命令就可以自动获取浏览器中的 Cookie，如果遇到权限提示，输入密码放行即可。

默认从 Chrome 浏览器获取 Cookie，如果你使用其他浏览器，请设置环境变量 `BROWSER_NAME`：

```shell
export BROWSER_NAME='arc'
```

支持的浏览器：
* chrome
* firefox
* brave
* edge
* safari
* arc

#### 手动设置

设置以下环境变量，可直接写入到 ~/.zshrc 里：

```shell
# gemini(可不配置，不配置默认会从浏览器自动获取。建议不配置)
export GEMINI_COOKIE_SECURE_1PSID=g.a0KAaMS************************************************AROiSJgW0076
export GEMINI_COOKIE_SECURE_1PSIDTS=sidts-CjAB*****************************KZn7ScYuMQAA
```

如何获取这些变量：

| Variable                             | How to Get                                                                                       |
|--------------------------------------|--------------------------------------------------------------------------------------------------|
| `GEMINI_COOKIE_SECURE_1PSID`(可忽略)    | Login to Gemini → F12 打开 Developer Tools → Application → Cookies → Copy value：`__Secure-1PSID`   |
| `GEMINI_COOKIE_SECURE_1PSIDTS` (可忽略) | Login to Gemini → F12 打开 Developer Tools → Application → Cookies → Copy value：`__Secure-1PSIDTS` |

## 3️⃣ Usage

```
$ v-cr -h
usage: cli.py [-h] [-m MR_ID] [-o] [-c] [--prompt-template PROMPT_TEMPLATE] [--list-prompt-template] [--debug] [--version] [JIRA_KEY]

Magic Code Review

positional arguments:
  JIRA_KEY              jira issue key

options:
  -h, --help            show this help message and exit
  -m MR_ID, --mr-id MR_ID
                        merge request id
  -o, --only-code       only review code diff
  -c, --copy-prompt     copy prompt to clipboard
  --prompt-template PROMPT_TEMPLATE
                        specific prompt template
  --list-prompt-template
                        list all prompt templates
  --debug
  --version
```

### 自动发送给 Gemini

```
$ v-cr ORI-100000
```

### 手动发送给 Gemini

```
$ v-cr ORI-100000 -c
......
......
2025-06-12 11:13:32,126 - INFO - ✨ issue comments length: 420
2025-06-12 11:13:33,231 - INFO - ✨ code  diff length: 990
2025-06-12 11:13:33,387 - INFO - ✨ prompt length: 28737, tokens num: 13015
✅ Prompt 已复制到剪贴板
```

### 自定义 Prompt

#### 创建

```
$ cd ~/.local/share/v-cr/prompts
```

```
$ touch my-prompt.txt
```

#### 变量说明

| 变量                     | 说明                         |
|------------------------|----------------------------|
| `{issue_summary}`      | Jira Issue 标题              |
| `{issue_requirements}` | Jira Issue Description     |
| `{issue_design}`       | Jira Issue 关联的设计 Wiki      |
| `{issue_comments}`     | Jira Issue 的评论             |
| `{mr_description}`     | Gitlab Merge Request 的描述   |
| `{mr_diff}`            | Gitlab Merge Request 的代码变更 |

#### Prompt 示例

```
帮我优化一下代码变量命名

{mr_diff}
```

```
帮我看下需求和实现的代码是否一致，是否漏了需求

<section>需求</section>
{issue_requirements}

<section>代码实现 Diff</section>
{mr_diff}
```

#### 列出可用的 Prompts

```
$ v-cr --list-prompt-template
Avalible Prompt Templates:

 • DEFAULT
 • my-prompt
```

#### 指定 Prompt

```
$ v-cr ORI-100000 --prompt-template my-prompt
```

# 🤝 Contributing

1. install `uv`

```
brew install uv
```

2. install virtualenv and dependencies

```
uv venv
uv sync --all-extras
```
