# Line_SquareNoteAPI

CHRLINEを使用してLINE SQUAREに投稿するためのAPIです。
アカウントがBANされる可能性がとても高いので使うことは推奨しません
SquareMidの取得方法については、`src/line_client/get_square_mid_from_ticket`をご覧ください。

認証番号の入力は、最初の1回のみで済みます。
certificateファイルやE2EE Keyファイルなどは、`src/CHRLINE-Square/.*`に保存されています。

## 必要条件

- Python 3.x
- CHRLINE

## インストール

1. リポジトリをクローンします：
   ```bash
   git clone https://github.com/ユーザー名/LINE_SQUARE.git
   ```

2. プロジェクトディレクトリに移動します：
   ```bash
   cd LINE_SQUARE
   ```

3. 仮想環境を作成し、アクティベートします：
   ```bash
   python -m venv env
   source env/bin/activate  # Linuxの場合
   # または
   env\Scripts\activate  # Windowsの場合
   ```

4. 必要なパッケージをインストールします：
   ```bash
   pip install -r requirements.txt
   ```

5. `.env`ファイルを作成し、以下の環境変数を設定します：

   ```
   Mailaddress=your_line_Mailaddress
   Password=your_line_Password
   SQUARE_ID=your_square_id
   ```

## 使用方法

1. 環境変数が正しく設定されていることを確認します。
2. 以下のコマンドを実行して、LINE SQUAREに投稿します：
   ```bash
   python3.x src/main.py
   ```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。