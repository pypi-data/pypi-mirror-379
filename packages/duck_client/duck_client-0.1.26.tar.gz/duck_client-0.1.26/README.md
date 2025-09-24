# DuckDB 连接器文档

## DataBase 类

### 类说明
用于连接和管理DuckDB数据库，处理币安交易数据的存储、因子计算和查询操作

---

### 初始化方法
```python
def __init__(
    self,
    share_folder_path: str | None = None,
    db_path: str | None = None,
    read_only: bool = True
)
```
参数说明：
- `share_folder_path`: 本地share文件夹路径（可选）| 如果需要获取新闻数据，则需要指定share文件夹路径
- `db_path`: DuckDB数据库文件路径（可选，内存数据库如果未指定）
- `read_only`: 是否以只读模式打开数据库（默认True）

---

### 主要公有方法

#### News Data
```python
def news(
    self,
    source: Literal["BWEnews", "ChainCatcher", "ChainNews", "FCNews", "ForeSight", "ODaily", "PANews", "TechFlow", "WuBlock"] = "BWEnews",
    start_date: str | None = None,
    end_date: str | None = None,
)
```
参数说明：
- `source`: 新闻源（默认BWEnews）
- `start_date/end_date`: 时间范围（ISO格式字符串）

返回：
- 包含新闻数据的DataFrame


#### 更新K线数据
```python
def update_klines(self)
```
功能：
- 遍历所有资产类别和时间频率，创建/更新K线数据表
- 自动处理不同时间粒度的数据聚合
- 进度条显示处理进度

#### 更新因子数据
```python
def update_factors(self)
```
功能：
- 计算动量（momentum）、波动率（volatility）、贝塔（beta）等因子
- 使用滑动窗口计算（窗口大小自动适配不同时间频率）
- 进度条显示处理进度

#### 获取因子数据
```python
def df_factors(
    self,
    symbols: list[str] | None = None,
    freq: Literal["1m", "3m", "15m", "30m", "1h", "4h", "12h", "1d"] = "1m",
    asset_class: Literal["spot", "um"] = "um",
    start_date: str | None = None,
    end_date: str | None = None,
    order_by_timestamp: bool = False,
) -> pd.DataFrame
```
参数说明：
- `symbols`: 交易对列表（可选，默认全部）
- `freq`: 时间频率（默认1分钟）
- `asset_class`: 资产类别（默认永续合约）
- `start_date/end_date`: 时间范围（ISO格式字符串）
- `order_by_timestamp`: 是否按时间排序

返回：
- 包含以下字段的DataFrame：
  timestamp, symbol, close, return, momentum, volatility, beta

#### 获取原始K线数据
```python
def df_klines(
    self,
    symbols: list[str] | None = None,
    freq: Literal["1m", "3m", "15m", "30m", "1h", "4h", "12h", "1d"] = "1m",
    asset_class: Literal["spot", "um"] = "um",
    start_date: str | None = None,
    end_date: str | None = None,
    order_by_timestamp: bool = False,
) -> pd.DataFrame
```
参数同`df_factors`

返回：
- 包含以下字段的DataFrame：
  symbol, timestamp, open, high, low, close, volume, quote_volume, 
  taker_buy_volume, taker_buy_quote_volume

#### 获取因子矩阵
```python
def factors_matrix(
    self,
    symbols: list[str] | None = None,
    factor: Literal["return", "momentum", "volatility", "beta"] = "return",
    freq: Literal["1m", "3m", "15m", "30m", "1h", "4h", "12h", "1d"] = "1m",
    asset_class: Literal["spot", "um"] = "um",
    start_date: str | None = None,
    end_date: str | None = None,
) -> pd.DataFrame
```
特殊说明：
- 返回以时间为索引、交易对为列名的二维矩阵
- 使用PIVOT操作将纵向数据转换为横向矩阵
- 适合量化分析中的因子研究

#### 获取所有交易对
```python
def list_all_symbols(self, asset_class: Literal["spot", "um"] = "um", data_type: Literal["klines", "metrics"] = "klines") -> list[str]:
```
参数说明：
- `asset_class`: 资产类别（默认永续合约）
- `data_type`: 数据类型（默认K线数据）

返回：
- 包含所有交易对的列表


---

### 异常类型
- `DBReadOnlyError`: 尝试在只读模式下执行写操作时抛出
- `DBError`: 参数错误或无效操作时抛出

---

### 使用示例
```python
from duck_client import DataBase


def main():
    db = DataBase(share_folder_path="/usr/local/share", db_path="/usr/local/share/binance_data/data.db")  # connect to db and the share folder path

    symbols = db.list_all_symbols(asset_class="um")
    print(symbols)

    # 获取因子数据
    df = db.df_factors(
        freq="1h",
        asset_class="spot",
    )
    print(df)

    # 获取K线数据
    df = db.df_klines(
        freq="1h",
        asset_class="spot",
    )
    print(df)

    # 获取因子Matrix
    df = db.factors_matrix(
        freq="1h",
        asset_class="spot",
    )
    print(df)
    
    # 获取K线Matrix
    df = db.klines_matrix(
        freq="1h",
        asset_class="spot",
        field="volume",
    )
    print(df)
    
    # 获取新闻数据
    df = db.news(
        source="ChainCatcher",
    )
    print(df)
    
    


if __name__ == "__main__":
    main()
```

