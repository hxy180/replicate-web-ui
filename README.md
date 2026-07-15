<div align="center">

# Replicate Web UI

**将参考网站的视觉、布局和交互效果，重新实现到你自己的前端项目中。**

[![简体中文](https://img.shields.io/badge/简体中文-111827?style=for-the-badge)](./README.md)
[![English](https://img.shields.io/badge/English-E5E7EB?style=for-the-badge)](./README_EN.md)

一个可跨 AI 编程代理使用的前端视觉迁移 Agent Skill。

</div>

## 这是什么

`replicate-web-ui` 遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)。你只需要提供参考网址或截图，以及自己的项目路径，支持 Skill 的 AI 编程代理就会分析参考页面的设计系统，并使用目标项目现有的技术栈重新实现。

它不绑定某个模型或产品。可以用于支持 Agent Skills 的工具，也可以让任意具备文件读取、浏览器和终端能力的 AI 代理直接读取 `SKILL.md` 后执行。

它不是简单下载网页源码，而是完成一套可验证的前端迁移流程：

1. 分析布局、字体、颜色、间距、圆角、阴影和动画
2. 识别桌面端、平板和移动端的响应式变化
3. 将参考设计映射到你的品牌和内容
4. 在现有 React、Vue、Next.js 或其他前端项目中实现
5. 启动项目并截图，对比参考效果后继续修正

## 使用场景

- 参考一个优秀落地页，为自己的产品制作相似的视觉体验
- 根据网页截图还原某个卡片、导航栏、弹窗或完整页面
- 将其他网站的滚动动画、悬停反馈或响应式布局迁移到现有项目
- 把旧项目页面升级成某种明确的设计风格
- 在获得授权后，高精度还原自己公司已有的网站
- 提取参考网站的设计语言，而不是复制其品牌内容

## 通用安装

推荐安装到项目级通用目录 `.agents/skills/`。在项目根目录运行：

```powershell
git clone https://github.com/hxy180/replicate-web-ui.git .agents/skills/replicate-web-ui
```

支持 Agent Skills 的工具可以自动发现该目录。不同客户端也可能使用自己的 Skill 目录，请以对应工具的文档为准。

### 不支持 Skill 自动发现的工具

将仓库克隆到任意位置：

```powershell
git clone https://github.com/hxy180/replicate-web-ui.git
```

然后在提示词中要求代理先读取：

```text
replicate-web-ui/SKILL.md
```

只要代理能够读取文件、访问参考网页、编辑目标项目并运行命令，就能使用这套工作流。

## 使用方法

支持 Skill 调用语法时，可以这样使用：

```text
使用 $replicate-web-ui

参考网址：https://example.com
目标项目：D:\projects\my-app
目标页面：首页
还原程度：close
要求：保留滚动动画，替换成我的品牌，并适配手机端。
```

也可以直接提供 `SKILL.md` 路径，适用于任何 AI 编程代理：

```text
先读取并遵循 D:\skills\replicate-web-ui\SKILL.md，
把 https://example.com 的 Hero 区域迁移到我当前的 React 项目。
```

## 使用案例

### 案例一：迁移落地页

```text
使用 $replicate-web-ui，参考 https://example.com 的首页，
在 D:\projects\product-site 中制作一个相同视觉节奏的产品落地页。
保留布局和动画，但替换 Logo、图片、文案和颜色。
```

### 案例二：根据截图还原组件

```text
使用 $replicate-web-ui，根据我提供的截图，
在当前 Vue 项目中还原这个定价卡片。
需要包含 hover 状态和移动端布局。
```

### 案例三：复制交互效果

```text
使用 $replicate-web-ui，分析参考网址中的滚动显现和卡片视差效果，
将这些交互加入当前 Next.js 首页，不改变现有内容结构。
```

### 案例四：授权页面的高精度迁移

```text
这个页面属于我们公司，我有权复刻。
使用 $replicate-web-ui 以 exact-authorized 模式迁移到新项目，
验证 1440px、768px 和 390px 三种宽度。
```

## 还原模式

| 模式 | 适用情况 | 处理方式 |
| --- | --- | --- |
| `inspired` | 只想借鉴设计风格 | 保留设计语言，明显调整布局和品牌 |
| `close` | 希望获得接近的视觉效果 | 匹配布局、层级和动效，替换品牌资产 |
| `exact-authorized` | 页面属于你或已获得授权 | 进行高精度实现和多尺寸视觉验证 |

未说明时默认使用 `close`。

## Skill 会做什么

- 优先沿用目标项目现有框架、组件和设计变量
- 使用真实浏览器检查页面与交互状态
- 覆盖桌面端和移动端响应式布局
- 保留语义化 HTML、键盘操作和减少动画支持
- 运行项目现有的测试、Lint 和构建命令
- 使用截图差异脚本辅助视觉验证

## 安全与版权边界

Skill 不会复制私有源码、压缩后的生产 Bundle、跟踪代码、凭据或隐藏接口。未经授权时，也不会直接使用原网站的 Logo、商标、付费字体、专有图片和文案。

不得用于制作冒充真实服务的登录、支付、钱包、银行、政府或账户恢复页面。完整规则见 [`references/compliance-boundaries.md`](./references/compliance-boundaries.md)。

## 项目结构

```text
replicate-web-ui/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── visual-analysis.md
│   └── compliance-boundaries.md
└── scripts/
    └── compare_screenshots.py
```

`SKILL.md`、`references/` 和 `scripts/` 是通用部分。`agents/openai.yaml` 仅用于支持该元数据格式的 OpenAI/Codex 客户端，不影响其他代理使用。

## 依赖

Skill 需要一个能够读取文件、使用浏览器、编辑代码并运行终端命令的 AI 代理。截图差异脚本需要 Python 3 和 Pillow：

```powershell
python -m pip install Pillow
```

## License

暂未选择开源许可证。仓库所有者保留所有权利。
