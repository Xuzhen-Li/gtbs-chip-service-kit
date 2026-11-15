# 靶向测序分型芯片服务套件

[English](README.md) | 中文

用一份精简的 `profile.yaml` 描述基因分型芯片（捕获 panel），并对该文件进行校验。Python 包名为 `gtbs_kit`，命令行工具为 `gtbs-kit`。

本仓库不执行样本分型，仅包含配置文件格式、葡萄 167K panel 的示例配置、新芯片空白模板，以及 [steps/](steps/) 中整理好的分析步骤顺序；这些步骤所调用的脚本不在此仓库内。能够完整跑通的葡萄分析示例见 [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)（演示报告：[ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html)），葡萄位点的筛选方法见 [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip)。

## 安装

需要 Python 3.11 或更新版本。

```bash
git clone https://github.com/Xuzhen-Li/gtbs-chip-service-kit.git
cd gtbs-chip-service-kit
python3 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
```

## 试一下

```bash
gtbs-kit list-examples
gtbs-kit validate-profile profiles/examples/grapevine_167k/profile.yaml
```

第二条命令会以 JSON 格式输出示例配置，其中 `panel_n_sites` 为 167433，`coordinate_system` 为 `VS-1`（2026-11-15 实测，完整输出见英文 README）。

## 加入自己的芯片

```bash
cp -R templates profiles/examples/my_chip
# 编辑 profiles/examples/my_chip/profile.yaml：profile_id、label、panel_n_sites、coordinate_system
gtbs-kit validate-profile profiles/examples/my_chip/profile.yaml
python -m pytest -q tests
```

`validate-profile` 仅检查 `profile_id` 和 `panel_n_sites` 是否存在。测试套件会依据 `profiles/profile.schema.json` 检查 `profiles/examples/` 下所有配置的必填键、顶层类型和最小值（例如 `panel_n_sites` 必须是不小于 1 的整数），并核对 `profile_id` 是否与文件夹名一致，因此刚复制的模板在填写完成前不会通过测试。分步说明见 [docs/steps.md](docs/steps.md)。

基因组、FASTQ、VCF 和剂量矩阵请保存在本地机器上，通过 `sites_bed`、`panel_info`、`dosage_cache` 指向本地路径，不要提交到仓库中。

## 文件

| 路径 | 内容 |
|------|------|
| `src/gtbs_kit/` | 配置加载与 `gtbs-kit` 命令 |
| `profiles/profile.schema.json` | 配置格式 |
| `profiles/examples/grapevine_167k/` | 示例配置 |
| `templates/` | 可复制的空白配置 |
| `steps/` | 分析顺序，`00a` 到 `14b`（不含脚本） |
| `platform/` | 接口说明（`gtbs_kit.spi`） |
| `app.py` | 可选的网页版检查（先运行 `pip install streamlit`，再运行 `streamlit run app.py`） |
| [`docs/REPO_LAYOUT.md`](docs/REPO_LAYOUT.md) | 哪些内容公开，哪些不公开 |

## 许可证

MIT，见 [LICENSE](LICENSE)。Xuzhen Li，[ORCID](https://orcid.org/0000-0003-3670-6657)。
