# HPC インフラ構成ドキュメントサイト

HPCシステムのインフラ構成を「機能・サービス視点」で可視化するドキュメントサイト。

## 概要

本サイトはMkDocs Materialを使用した静的サイトとして構築され、GitHub Pagesでホスティングされる。GitHub Actionsによる自動デプロイパイプラインを備え、コンテンツの変更がレビュー・マージ後に自動でサイトに反映される。

## コンテンツカテゴリ

- **ユーザーアクセス・認証・ポータル** — ユーザー管理、認証基盤、利用ポータルの構成情報
- **計算リソース・ジョブ管理** — 計算リソースの構成とジョブ管理の設計情報
- **アプリケーション・ライセンス** — CAEソフトウェアやライセンスサーバの構成情報
- **データ管理・基盤サービス・運用管理** — ストレージ、DNS、監視、バックアップ等の基盤サービス構成
- **ネットワーク** — HPCネットワークの論理構成とアドレス管理情報

## 技術スタック

| コンポーネント | 技術 |
|---|---|
| SSGエンジン | MkDocs Material 9.x |
| ダイアグラム | Mermaid（pymdownx.superfences） |
| 検索 | MkDocs内蔵検索（lunr.js） |
| CI/CD | GitHub Actions |
| ホスティング | GitHub Pages |

## ローカル開発

```bash
pip install -r requirements.txt
mkdocs serve
```

## ビルド

```bash
mkdocs build --strict
```
