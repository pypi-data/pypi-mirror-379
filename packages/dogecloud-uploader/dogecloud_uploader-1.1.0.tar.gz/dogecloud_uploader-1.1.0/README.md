# dogecloud-uploader

多吉云上传工具 - 支持图片和文件上传到多吉云存储

## 特性

- 🚀 **简单易用** - 提供简化的API接口，开箱即用
- 🖼️ **图片优化** - 自动WebP转换，减少存储空间
- 🔐 **安全可靠** - 完善的权限控制和错误处理
- 📦 **多种格式** - 支持图片、HTML、通用文件上传
- 🌐 **多种来源** - 支持本地文件、HTTP/HTTPS URL、Base64 data URL
- ⚡ **异步支持** - 基于asyncio的高性能异步API
- 🛠️ **CLI工具** - 提供命令行工具，方便集成到工作流中

## 安装

```bash
pip install dogecloud-uploader
```

## 快速开始

### 环境配置

首先设置多吉云认证信息：

```bash
# 方式1: 使用环境变量
export DOGECLOUD_ACCESS_KEY="your_access_key"
export DOGECLOUD_SECRET_KEY="your_secret_key"
export DOGECLOUD_BUCKET_NAME="your_bucket"
export DOGECLOUD_CDN_DOMAIN="https://your.cdn.domain"
```

```bash
# 方式2: 使用CLI配置工具
dogecloud config --access-key your_key --secret-key your_secret
```

### Python API

#### 简单图片上传

```python
import asyncio
from dogecloud_uploader import upload_image

async def main():
    # 上传网络图片
    result = await upload_image("https://example.com/image.jpg")
    print(f"上传成功: {result['file_url']}")

    # 上传Base64图片
    base64_url = "data:image/jpeg;base64,/9j/4AAQSkZJRgABA..."
    result = await upload_image(base64_url, custom_filename="my_image.webp")
    print(f"上传成功: {result['file_url']}")

asyncio.run(main())
```

#### 文件上传

```python
import asyncio
from dogecloud_uploader import upload_file

async def main():
    # 上传HTML报告
    result = await upload_file("report.html", filename="report.html")
    print(f"报告地址: {result['file_url']}")

asyncio.run(main())
```

#### 高级API

```python
import asyncio
from dogecloud_uploader import DogecloudClient

async def main():
    # 创建客户端实例
    client = DogecloudClient(
        access_key="your_key",
        secret_key="your_secret",
        bucket_name="your_bucket",
        enable_compression=True  # 启用WebP压缩
    )

    # 上传图片
    result = await client.upload_file("image.jpg", "optimized_image.webp", "image")
    print(f"上传成功: {result['file_url']}")

asyncio.run(main())
```

### 命令行工具

#### 基本用法

```bash
# 上传本地图片
dogecloud upload image.jpg

# 上传网络图片
dogecloud upload https://example.com/image.jpg --filename custom.webp

# 上传HTML文件
dogecloud upload report.html --type html

# 禁用WebP转换
dogecloud upload image.png --no-webp

# 详细输出
dogecloud upload image.jpg --verbose
```

#### 测试连接

```bash
# 测试多吉云连接
dogecloud test

# 查看版本
dogecloud version
```

## API参考

### upload_image()

```python
async def upload_image(
    image_url: str,
    custom_filename: Optional[str] = None,
    enable_webp_conversion: bool = True,
    client: Optional[DogecloudClient] = None
) -> Dict[str, Any]
```

**参数:**
- `image_url`: 图片URL，支持HTTP/HTTPS URL或Base64 data URL
- `custom_filename`: 自定义文件名（可选）
- `enable_webp_conversion`: 是否启用WebP转换（默认True）
- `client`: 多吉云客户端实例（可选）

**返回值:**
```python
{
    'success': True,
    'file_url': 'https://cdn.example.com/image.webp',
    'object_key': 'images/image.webp',
    'filename': 'image.webp',
    'size': 12345,
    'format': 'WEBP',
    'original_md5': 'abc123...'
}
```

### upload_file()

```python
async def upload_file(
    file_path: str,
    filename: Optional[str] = None,
    file_type: str = 'html',
    client: Optional[DogecloudClient] = None
) -> Dict[str, Any]
```

**参数:**
- `file_path`: 本地文件路径
- `filename`: 上传后的文件名（可选）
- `file_type`: 文件类型 ('html', 'image' 等)
- `client`: 多吉云客户端实例（可选）

### DogecloudClient

```python
class DogecloudClient:
    def __init__(
        self,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        bucket_name: Optional[str] = None,
        cdn_domain: Optional[str] = None,
        enable_compression: Optional[bool] = None
    )
```

## 配置选项

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `DOGECLOUD_ACCESS_KEY` | 多吉云访问密钥 | 必需 |
| `DOGECLOUD_SECRET_KEY` | 多吉云密钥 | 必需 |
| `DOGECLOUD_BUCKET_NAME` | 存储桶名称 | `default-bucket` |
| `DOGECLOUD_CDN_DOMAIN` | CDN域名 | 无 |
| `DOGECLOUD_ENABLE_COMPRESSION` | 启用压缩 | `true` |

### 配置文件

也可以在 `~/.dogecloud/config` 文件中配置：

```
DOGECLOUD_ACCESS_KEY=your_access_key
DOGECLOUD_SECRET_KEY=your_secret_key
DOGECLOUD_BUCKET_NAME=your_bucket
DOGECLOUD_CDN_DOMAIN=https://your.cdn.domain
```

## 错误处理

```python
from dogecloud_uploader import upload_image
from dogecloud_uploader.exceptions import (
    DogecloudError,
    AuthenticationError,
    ValidationError,
    UploadError,
    ConfigurationError
)

async def safe_upload():
    try:
        result = await upload_image("https://example.com/image.jpg")
        return result
    except AuthenticationError as e:
        print(f"认证失败: {e}")
    except ValidationError as e:
        print(f"验证失败: {e}")
    except UploadError as e:
        print(f"上传失败: {e}")
    except DogecloudError as e:
        print(f"多吉云错误: {e}")
```

## 开发

### 安装开发依赖

```bash
git clone https://github.com/overseas-report/dogecloud-uploader.git
cd dogecloud-uploader
pip install -e ".[dev]"
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_client.py

# 生成覆盖率报告
pytest --cov=dogecloud_uploader --cov-report=html
```

### 代码格式化

```bash
# 格式化代码
black dogecloud_uploader tests

# 排序import
isort dogecloud_uploader tests

# 类型检查
mypy dogecloud_uploader
```

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v1.0.0 (2024-01-XX)

- 🎉 首次发布
- ✨ 支持图片和文件上传
- ✨ WebP自动转换
- ✨ CLI工具
- ✨ 异步API支持
- 🔒 完善的安全措施

## 支持

如果你遇到问题或有建议，请：

1. 查看[文档](https://github.com/overseas-report/dogecloud-uploader#readme)
2. 搜索[已有Issues](https://github.com/overseas-report/dogecloud-uploader/issues)
3. 创建[新Issue](https://github.com/overseas-report/dogecloud-uploader/issues/new)