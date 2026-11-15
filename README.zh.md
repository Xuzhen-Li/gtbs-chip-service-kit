# 靶向测序分型芯片服务套件

[English](README.md) | 中文

用一个小的 `profile.yaml` 描述一张基因分型芯片（捕获 panel），并检查这个文件。Python 包名是 `gtbs_kit`，命令是 `gtbs-kit`。

本仓库不做样本分型。它只有：配置文件格式、葡萄 167K panel 的示例配置、新芯片用的空白模板，以及 [steps/](steps/) 里写好的分析顺序。这些步骤调用的脚本不在本仓库。能从头跑通的葡萄示例在 [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)（演示报告：[ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html)）。葡萄位点是怎么选出来的，见 [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip)。

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

第二条命令会把示例配置按 JSON 打印出来，其中 `panel_n_sites` 为 167433，`coordinate_system` 为 `VS-1`（2026-11-15 实测，完整输出见英文 README）。

## 加入自己的芯片

```bash
cp -R templates profiles/examples/my_chip
# 编辑 profiles/examples/my_chip/profile.yaml：profile_id、label、panel_n_sites、coordinate_system
gtbs-kit validate-profile profiles/examples/my_chip/profile.yaml
python -m pytest -q tests
```

`validate-profile` 只检查 `profile_id` 和 `panel_n_sites` 是否存在。测试会按 `profiles/profile.schema.json` 检查 `profiles/examples/` 下每个配置的必填键、顶层类型和最小值（比如 `panel_n_sites` 必须是不小于 1 的整数），并检查 `profile_id` 与文件夹名一致，所以刚复制的模板在填好之前会测试失败。分步说明见 [docs/steps.md](docs/steps.md)。

基因组、FASTQ、VCF 和剂量矩阵留在自己的机器上，用 `sites_bed`、`panel_info`、`dosage_cache` 指过去，不要提交到仓库。

## 文件

| 路径 | 内容 |
|------|------|
| `src/gtbs_kit/` | 配置加载和 `gtbs-kit` 命令 |
| `profiles/profile.schema.json` | 配置格式 |
| `profiles/examples/grapevine_167k/` | 示例配置 |
| `templates/` | 可复制的空白配置 |
| `steps/` | 分析顺序，`00a` 到 `14b`（不含脚本） |
| `platform/` | 接口说明（`gtbs_kit.spi`） |
| `app.py` | 可选的网页版检查（先 `pip install streamlit`，再 `streamlit run app.py`） |
| [`docs/REPO_LAYOUT.md`](docs/REPO_LAYOUT.md) | 哪些内容公开，哪些不公开 |

## 许可证

MIT，见 [LICENSE](LICENSE)。Xuzhen Li，[ORCID](https://orcid.org/0000-0003-3670-6657)。
