# 靶向测序分型芯片服务套件

[English](README.md) | 中文

将现有的基因分型芯片注册为配置文件，并使用 `validate-profile` 进行检查。芯片设计位于 [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip)；葡萄 167K 运行示例为 [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)。演示报告：[ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html)。

仓库标识符：[`gtbs-chip-service-kit`](https://github.com/Xuzhen-Li/gtbs-chip-service-kit)。包导入名称：`gtbs_kit`。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 文件

| 路径 | 作用 |
| --- | --- |
| `platform/` | 契约文档（SPI 位于 `gtbs_kit.spi`） |
| `src/gtbs_kit/` | 加载/验证配置文件 |
| `profiles/` | 模式 + [`examples/grapevine_167k`](profiles/examples/grapevine_167k/) |
| `templates/` | 空配置文件 cookiecutter |
| [`docs/REPO_LAYOUT.md`](docs/REPO_LAYOUT.md) | 保留/删除规则 |

不包含脚本、二进制文件、基因组、FASTQ 和剂量矩阵。

## 葡萄流程演示

分析说明位于 [steps/](steps/)，每个步骤一个文件，从 `00a` 到 `14b`。[Xuzhen-Li/grapeancestry](https://github.com/Xuzhen-Li/grapeancestry) 是可运行的葡萄 167K 实际示例。

## 用法

六个配置文件步骤位于 [docs/steps.md](docs/steps.md)。分析顺序位于 [steps/README.md](steps/README.md)。[steps/](steps/) 中的命令调用的脚本不在此克隆版本中。

## 快速开始

这些命令与公开克隆版本中的 `pyproject.toml`（`gtbs-kit = gtbs_kit.cli:main`）和 `src/gtbs_kit/cli.py` 相匹配：`validate-profile` 加载配置文件 YAML，`list-examples` 列出 `profiles/examples` 下包含 `profile.yaml` 的目录。

```bash
pip install -e .
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
gtbs-kit list-examples
```

## 许可证

MIT，请参阅 [LICENSE](LICENSE)。Xuzhen Li，[ORCID](https://orcid.org/0000-0003-3670-6657)
