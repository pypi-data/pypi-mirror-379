# Tushare MCP Server

[English](./README.md) | [中文](./README_zh.md)

This project is a Model Context Protocol (MCP) server based on the [Tushare](https://tushare.pro/) data interface. It provides rich and comprehensive financial market data for mainland China, designed to be used with AI assistants.

## 🌟 Features

- **Stock Data**: Access to basic stock information, daily/weekly/monthly quotes, and historical data.
- **Market Data**: Includes Top List (Longhubang), Margin Trading, Block Trades, and Money Flow data.
- **Financial Data**: Retrieve financial statements and key indicators for listed companies.
- **Index Data**: Get quotes and historical data for major market indices.
- **Fund & ETF Data**: Access to ETF quotes, fund NAV, holdings, and ratings.
- **Bond Data**: Provides basic information and market data for bonds and convertible bonds.
- **Macroeconomics**: Offers data on GDP, CPI, interest rates, exchange rates, PMI, and money supply.
- **Smart Search**: Search for stocks by name or code.
- **High Performance**: Built with asynchronous processing to support efficient queries.

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/tushare_mcp.git
    cd tushare_mcp
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

To use this server, you need to provide a Tushare API Token. You can get a free token by registering on the [Tushare Pro website](https://tushare.pro/).

There are two ways to configure your token:

#### Method 1: Environment Variable (Recommended)

This is the most secure and flexible method. The server is designed to automatically read the token from an environment variable named `TUSHARE_TOKEN`.

-   **On macOS/Linux:**
    ```bash
    export TUSHARE_TOKEN="your_tushare_token_here"
    ```
    To make this setting permanent, add the line to your shell's profile file (e.g., `~/.bash_profile`, `~/.zshrc`).

-   **On Windows:**
    ```bash
    set TUSHARE_TOKEN="your_tushare_token_here"
    ```
    To set it permanently, you can use the System Properties > Environment Variables panel.

#### Method 2: Configuration File (for MCP Clients)

If you are using an MCP client that launches the server for you (like Claude Desktop), you should use the `mcp_config.json` file.

1.  **Create the config file** by copying the template:
    ```bash
    cp mcp_config.json.template mcp_config.json
    ```

2.  **Edit `mcp_config.json`**:
    Open the file and replace the placeholder values.
    -   `cwd`: Set this to the **absolute path** of the `tushare_mcp` project directory.
    -   `TUSHARE_TOKEN`: Paste your Tushare token here.

    **Example `mcp_config.json`:**
    ```json
    {
      "mcpServers": {
        "tushare": {
          "command": "python",
          "args": ["server.py"],
          "cwd": "/path/to/your/tushare_mcp",
          "env": {
            "TUSHARE_TOKEN": "YOUR_TUSHARE_TOKEN_HERE"
          }
        }
      }
    }
    ```

> **Note**: If the `TUSHARE_TOKEN` is not set by any of these methods, the server will fall back to the free, non-Pro version of the Tushare API, which has significant limitations on data access.

## ▶️ Usage

There are two primary ways to run the server:

#### 1. Standalone Mode

You can run the server directly from your terminal. This is useful for testing or for connecting with clients that attach to a running process.

1.  **Set your API token** using the environment variable method described above.
2.  **Start the server**:
    ```bash
    python server.py
    ```
3.  **Verify**: Upon successful startup, you will see one of the following messages:
    -   `✅ Tushare Token has been set.` (If you configured a token)
    -   `⚠️ Tushare Token is not set, using free interface (limited functionality).` (If no token is found)
    
    The server is now running and waiting for a client to connect.

#### 2. With an MCP Client (e.g., Claude Desktop)

Most MCP clients will manage the server process for you.

1.  **Configure `mcp_config.json`** as described in the configuration section, making sure the `cwd` and `TUSHARE_TOKEN` are set correctly.
2.  **Point your client** to this `mcp_config.json` file.
3.  **The client will automatically start** the `server.py` process when you interact with one of its tools. You do not need to run `python server.py` manually.

## 🛠️ Available Tools

This server exposes a comprehensive set of tools to access financial data. Here are some of the categories:

-   **Basic Stock Data**: `get_stock_basic`, `get_daily_data`, `get_weekly_data`, `get_monthly_data`, etc.
-   **Market Reference Data**: `get_top_list`, `get_money_flow`, `get_margin_detail`, `get_block_trade`.
-   **Financial Data**: `get_financial_data`, `get_balance_sheet`, `get_cash_flow`, `get_fina_indicator`.
-   **Index Data**: `get_index_data`, `get_index_basic`, `get_index_weight`.
-   **ETF & Fund Data**: `get_etf_basic`, `get_etf_daily`, `get_fund_daily`, `get_fund_portfolio`.
-   **Bond Data**: `get_bond_basic`, `get_bond_daily`, `get_cb_basic`, `get_cb_daily`.
-   **Macroeconomic Data**: `get_gdp_data`, `get_cpi_data`, `get_interest_rate`, `get_exchange_rate`.

For a complete list of tools and their parameters, please refer to the `handle_list_tools` function in `server.py`.

## 📄 License

This project is open-sourced under the [GPL v3.0 License](./LICENSE).

---

# Tushare MCP 服务器

[English](./README.md) | [中文](./README_zh.md)

本项目是一个基于 [Tushare](https://tushare.pro/) 数据接口的模型上下文协议 (MCP) 服务器，为 AI 助手提供丰富、全面的中国内地金融市场数据。

## 🌟 功能特性

- **股票数据**: 提供股票基本信息、日线/周线/月线行情及历史数据。
- **市场数据**: 包含龙虎榜、融资融券、大宗交易、资金流向等数据。
- **财务数据**: 获取上市公司的财务报表和关键财务指标。
- **指数数据**: 获取主要市场指数的行情和历史数据。
- **基金与ETF**: 提供 ETF 行情、基金净值、持仓、评级等信息。
- **债券数据**: 提供债券和可转债的基本信息及行情数据。
- **宏观经济**: 提供 GDP、CPI、利率、汇率、PMI、货币供应量等数据。
- **智能搜索**: 支持按名称或代码搜索股票。
- **高性能**: 采用异步处理，支持高效查询。

## 📦 安装指南

1.  克隆代码仓库：
    ```bash
    git clone https://github.com/your-username/tushare_mcp.git
    cd tushare_mcp
    ```

2.  安装所需依赖：
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ 配置说明

1.  您需要一个 Tushare API 令牌。请访问 [Tushare Pro 官网](https://tushare.pro/) 注册账户以获取您的令牌。

2.  将 Tushare 令牌设置为环境变量。这是推荐的最安全方式。

    -   在 macOS/Linux 系统中：
        ```bash
        export TUSHARE_TOKEN="your_tushare_token_here"
        ```
    -   在 Windows 系统中：
        ```bash
        set TUSHARE_TOKEN="your_tushare_token_here"
        ```

3.  或者，您也可以在 `mcp_config.json` 文件中配置（不推荐）。复制模板文件并填入您的信息：
    ```bash
    cp mcp_config.json.template mcp_config.json
    ```
    然后编辑 `mcp_config.json`，填入您的令牌和正确的项目路径。

## ▶️ 如何使用

通过以下命令运行服务器：

```bash
python server.py
```

服务器将启动并等待来自 MCP 客户端（例如 Claude Desktop）的连接。

如果未设置 `TUSHARE_TOKEN`，服务器将使用免费接口，其功能会受到限制。

## 🛠️ 可用工具

该服务器提供了一套全面的工具集，用于访问金融数据。以下是部分工具类别：

-   **基础股票数据**: `get_stock_basic`, `get_daily_data`, `get_weekly_data`, `get_monthly_data` 等。
-   **市场参考数据**: `get_top_list`, `get_money_flow`, `get_margin_detail`, `get_block_trade`。
-   **财务数据**: `get_financial_data`, `get_balance_sheet`, `get_cash_flow`, `get_fina_indicator`。
-   **指数数据**: `get_index_data`, `get_index_basic`, `get_index_weight`。
-   **ETF与基金数据**: `get_etf_basic`, `get_etf_daily`, `get_fund_daily`, `get_fund_portfolio`。
-   **债券数据**: `get_bond_basic`, `get_bond_daily`, `get_cb_basic`, `get_cb_daily`。
-   **宏观经济数据**: `get_gdp_data`, `get_cpi_data`, `get_interest_rate`, `get_exchange_rate`。

关于完整的工具列表及其参数，请参考 `server.py` 文件中的 `handle_list_tools` 函数。

## 📄 开源协议

本项目采用 [MIT 许可证](./LICENSE) 开源。