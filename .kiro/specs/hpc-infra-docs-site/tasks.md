# 実装計画: HPC インフラドキュメントサイト

## 概要

MkDocs Material + GitHub Pages + GitHub Actionsを使用したHPCインフラドキュメントサイトを段階的に構築する。プロジェクト基盤の構築から始め、設定ファイル、CI/CDワークフロー、コンテンツファイル、テストの順で実装する。

## タスク

- [x] 1. プロジェクト基盤の構築
  - [x] 1.1 ディレクトリ構造とrequirements.txtの作成
    - 設計ドキュメントに定義されたディレクトリ構造を作成する
    - `docs/`配下の全サブディレクトリ（`user-access/`, `compute/`, `applications/`, `data-ops/`, `network/`, `manuals/`, `faq/`, `status/`）を作成
    - `.github/workflows/`ディレクトリを作成
    - `requirements.txt`に`mkdocs-material>=9.0`を記述
    - `README.md`にプロジェクト概要を記述
    - _要件: 1.1, 12.3_

  - [x] 1.2 mkdocs.ymlの作成
    - 設計ドキュメントのmkdocs.yml設定を実装する
    - テーマ設定: Material、日本語、レスポンシブ対応
    - ナビゲーション機能: `navigation.tabs`, `navigation.sections`, `navigation.expand`, `navigation.path`, `navigation.indexes`
    - 検索プラグイン: `lang: ja, en`
    - Markdown拡張: `pymdownx.superfences`（Mermaidカスタムフェンス）、`admonition`、`pymdownx.details`、`attr_list`、`toc`
    - nav構造: 5つのトップレベルカテゴリ + 補助コンテンツ（マニュアル、FAQ、稼働状況）の全ページパスを定義
    - _要件: 1.1, 3.1, 3.2, 3.3, 3.4, 4.1, 4.3, 5.1, 5.2_

- [x] 2. GitHub Actionsワークフローの作成
  - [x] 2.1 PRビルド検証ワークフロー（ci.yml）の作成
    - `.github/workflows/ci.yml`を作成
    - トリガー: `pull_request`（mainブランチ、`docs/**`, `mkdocs.yml`, `requirements.txt`のパスフィルタ）
    - ステップ: checkout → setup-python 3.12 → pip install → `mkdocs build --strict`
    - `--strict`フラグでビルド警告をエラーとして扱う
    - _要件: 2.2, 2.3, 12.2_

  - [x] 2.2 デプロイワークフロー（deploy.yml）の作成
    - `.github/workflows/deploy.yml`を作成
    - トリガー: `push`（mainブランチ、`docs/**`, `mkdocs.yml`, `requirements.txt`のパスフィルタ）
    - permissions: `pages: write`, `id-token: write`
    - ステップ: checkout → setup-python 3.12 → pip install → `mkdocs build --strict` → upload-pages-artifact → deploy-pages
    - GitHub Pages公式デプロイアクションを使用
    - _要件: 2.1, 2.3, 2.4_

- [x] 3. チェックポイント - プロジェクト基盤の検証
  - mkdocs.ymlの構文が正しいことを確認
  - GitHub Actionsワークフローの構文が正しいことを確認
  - 問題があればユーザーに確認する

- [x] 4. コンテンツファイルの作成（ユーザーアクセス・認証・ポータル）
  - [x] 4.1 ユーザーアクセスカテゴリのコンテンツファイルを作成
    - `docs/user-access/index.md`: カテゴリ概要ページ
    - `docs/user-access/registration-flow.md`: ユーザー登録フロー（Mermaidフロー図を含む）
    - `docs/user-access/user-db.md`: ユーザー管理DB一覧
    - `docs/user-access/hr-sync.md`: 人事・組織変更との同期連携
    - `docs/user-access/account-audit.md`: ユーザー定期棚卸方法
    - `docs/user-access/admin-privileges.md`: 管理者権限の割り当て方針
    - `docs/user-access/uid-gid-policy.md`: UID/GID採番ルールとグループポリシー
    - `docs/user-access/account-lifecycle.md`: アカウントロック・削除手順
    - `docs/user-access/ldap-ad.md`: LDAP/AD参照構成と認証情報同期
    - `docs/user-access/portal.md`: 利用ポータル機能一覧・SSH接続・保守手順・API連携
    - 各ファイルは設計ドキュメントのテンプレートに従い、frontmatter（title, description）を含む
    - _要件: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10_

- [x] 5. コンテンツファイルの作成（計算リソース・アプリケーション）
  - [x] 5.1 計算リソース・ジョブ管理カテゴリのコンテンツファイルを作成
    - `docs/compute/index.md`: カテゴリ概要ページ
    - `docs/compute/node-types.md`: ノードタイプ・論理スペック定義
    - `docs/compute/virtual-infra.md`: 仮想基盤・仮想マシン構成
    - `docs/compute/queue-design.md`: キュー設計・パーティション定義
    - `docs/compute/scheduler.md`: ジョブスケジューラ優先順位・Prolog/Epilogスクリプト
    - `docs/compute/container.md`: Docker利用方法・イメージ管理
    - _要件: 7.1, 7.2, 7.3, 7.4, 7.5_

  - [x] 5.2 アプリケーション・ライセンスカテゴリのコンテンツファイルを作成
    - `docs/applications/index.md`: カテゴリ概要ページ
    - `docs/applications/cae-software.md`: CAEソフトバージョン管理・ライセンスポリシー・module設定
    - `docs/applications/license-server.md`: FlexLM/RLMライセンスサーバ構成
    - `docs/applications/github-server.md`: GitHub Server構成・運用・認証・バックアップ
    - _要件: 8.1, 8.2, 8.3_

- [x] 6. コンテンツファイルの作成（データ管理・ネットワーク・補助）
  - [x] 6.1 データ管理・基盤サービス・運用管理カテゴリのコンテンツファイルを作成
    - `docs/data-ops/index.md`: カテゴリ概要ページ
    - `docs/data-ops/shared-storage.md`: 共有ストレージ（Lustre）クォータ・パージポリシー
    - `docs/data-ops/nas-gw.md`: ファイル共有（NAS-GW）アクセス権設定
    - `docs/data-ops/dns-ntp.md`: DNS/NTPフォワーディング設定・ホスト登録
    - `docs/data-ops/monitoring.md`: 監視項目一覧・通知設定
    - `docs/data-ops/backup.md`: バックアップ対象・頻度・リストア手順
    - `docs/data-ops/billing.md`: 課金ロジック・稼働統計集計
    - _要件: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6_

  - [x] 6.2 ネットワークカテゴリのコンテンツファイルを作成
    - `docs/network/index.md`: カテゴリ概要ページ
    - `docs/network/logical-design.md`: HPC/管理/InfiniBand/基幹ネットワーク論理構成
    - `docs/network/vlan-subnet.md`: サブネット・VLAN構成図（Mermaid記法）
    - `docs/network/ip-management.md`: IPアドレス管理情報
    - _要件: 10.1, 10.2, 10.3_

  - [x] 6.3 補助コンテンツとトップページの作成
    - `docs/index.md`: サイトトップページ（HPCインフラドキュメントサイトの概要・各カテゴリへのリンク）
    - `docs/manuals/index.md`: マニュアル・チュートリアルセクション
    - `docs/faq/index.md`: FAQセクション
    - `docs/status/index.md`: システム稼働状況の公開レベル定義・表示方法
    - _要件: 11.1, 11.2, 11.3_

- [x] 7. チェックポイント - コンテンツとビルドの検証
  - 全コンテンツファイルが作成されていることを確認
  - mkdocs.ymlのnav設定と実ファイルの整合性を確認
  - 問題があればユーザーに確認する

- [x] 8. テストの実装
  - [x] 8.1 テスト基盤のセットアップ
    - `tests/`ディレクトリを作成
    - `requirements.txt`にテスト依存パッケージ（`pytest`, `hypothesis`, `pyyaml`）を追加
    - `tests/conftest.py`に共通フィクスチャ（mkdocs.yml読み込み、プロジェクトルートパス等）を定義
    - _要件: 1.1_

  - [x] 8.2 mkdocs.yml構造のユニットテストを作成
    - `tests/test_config.py`を作成
    - テスト: 5つのトップレベルカテゴリが正しい名前で存在すること
    - テスト: `navigation.path` featureが有効であること（パンくずリスト）
    - テスト: searchプラグインが有効で日本語対応であること
    - テスト: `pymdownx.superfences`のカスタムフェンスにmermaidが設定されていること
    - _要件: 3.1, 3.4, 4.3, 5.1_

  - [x] 8.3 GitHub Actionsワークフローのユニットテストを作成
    - `tests/test_workflows.py`を作成
    - テスト: ci.ymlが`pull_request`トリガーを持つこと
    - テスト: deploy.ymlが`push`（mainブランチ）トリガーを持つこと
    - テスト: deploy.ymlに`pages: write`パーミッションが設定されていること
    - _要件: 2.1, 2.2_

  - [ ]* 8.4 Property 1: Markdownビルドラウンドトリップのプロパティテストを作成
    - **Property 1: Markdownビルドラウンドトリップ**
    - `tests/test_properties.py`にテストを追加
    - HypothesisでランダムなMarkdownコンテンツを生成し、ビルド後のHTMLに本文テキストが含まれることを検証
    - タグ: `Feature: hpc-infra-docs-site, Property 1: Markdownビルドラウンドトリップ`
    - **検証対象: 要件 1.1, 1.4**

  - [ ]* 8.5 Property 2: ナビゲーション階層構造のプロパティテストを作成
    - **Property 2: ナビゲーション階層構造**
    - `tests/test_properties.py`にテストを追加
    - mkdocs.ymlのnav構造を解析し、全トップレベルカテゴリが子要素を持つことを検証
    - タグ: `Feature: hpc-infra-docs-site, Property 2: ナビゲーション階層構造`
    - **検証対象: 要件 3.2**

  - [ ]* 8.6 Property 3: 検索インデックス完全性のプロパティテストを作成
    - **Property 3: 検索インデックス完全性**
    - `tests/test_properties.py`にテストを追加
    - docs/内のファイルリストと検索インデックスのエントリを照合し、全ファイルがインデックスに含まれることを検証
    - タグ: `Feature: hpc-infra-docs-site, Property 3: 検索インデックス完全性`
    - **検証対象: 要件 4.1, 4.2**

  - [ ]* 8.7 Property 4: Mermaidビルド統合のプロパティテストを作成
    - **Property 4: Mermaidビルド統合**
    - `tests/test_properties.py`にテストを追加
    - ランダムなMermaidダイアグラムを含むMarkdownを生成し、ビルド後のHTMLに`class="mermaid"`が含まれることを検証
    - タグ: `Feature: hpc-infra-docs-site, Property 4: Mermaidビルド統合`
    - **検証対象: 要件 5.1, 5.2**

  - [ ]* 8.8 Property 5: コンテンツページ完全性のプロパティテストを作成
    - **Property 5: コンテンツページ完全性**
    - `tests/test_properties.py`にテストを追加
    - nav設定の全ファイルパスに対応するファイルがdocs/ディレクトリに存在することを検証
    - タグ: `Feature: hpc-infra-docs-site, Property 5: コンテンツページ完全性`
    - **検証対象: 要件 6.1-6.10, 7.1-7.5, 8.1-8.3, 9.1-9.6, 10.1-10.3, 11.1-11.3, 12.3**

- [x] 9. 最終チェックポイント - 全テスト実行と最終検証
  - 全テストが通ることを確認する
  - 問題があればユーザーに確認する

## 備考

- `*`マーク付きのタスクはオプションであり、MVP実装時にはスキップ可能
- 各タスクは対応する要件番号を参照しトレーサビリティを確保
- チェックポイントで段階的に検証を実施
- プロパティテストは設計ドキュメントの正当性プロパティに対応
- ユニットテストは具体的なケースとエッジケースに焦点を当てる
