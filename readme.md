# PDFページ番号追加スクリプト

このスクリプトは、PDFファイルの各ページの左下または右下にページ番号を追加します。ただし、最初のページは除きます。

## 必要条件

- Python 3.6+
- `PyPDF2`
- `reportlab`

## インストール

1. リポジトリをクローンします:
    ```bash
    git clone https://github.com/yourusername/pdf-page-numbering.git
    cd pdf-page-numbering
    ```

2. 仮想環境を作成して有効化します（推奨）:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
    ```

3. 必要なパッケージをインストールします:
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. 入力PDFファイルをプロジェクトディレクトリに配置し、`input.pdf` にリネームします。

2. スクリプトを実行します:
    ```bash
    python main.py
    ```

3. 出力ファイル `output_with_page_numbers.pdf` がプロジェクトディレクトリに作成されます。
