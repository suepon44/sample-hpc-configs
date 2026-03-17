---
title: アプリケーション・ライセンス
description: HPCシステムにおけるCAEソフトウェア、ライセンスサーバ、GitHub Serverの構成・運用に関する情報を一元的にまとめたカテゴリページ
---

# アプリケーション・ライセンス

## 概要

本カテゴリでは、HPCシステムで利用するアプリケーションソフトウェアとライセンス管理に関する構成情報を記述する。CAEソフトウェアのバージョン管理・moduleコマンド設定、FlexLM/RLMライセンスサーバの構成、GitHub Serverの運用をカバーする。

## 対象範囲

- CAEソフトウェアのバージョン管理・ライセンスポリシー・module設定
- FlexLM/RLMライセンスサーバの構成・冗長化・アクセス制限
- GitHub Serverの構成・認証・バックアップ

## カテゴリ構成図

```mermaid
graph TD
    APP["アプリケーション・ライセンス"]
    APP --> CAE["CAEソフトウェア"]
    APP --> LIC["ライセンスサーバ"]
    APP --> GH["GitHub Server"]

    CAE --> CAE1["バージョン管理"]
    CAE --> CAE2["ライセンスポリシー"]
    CAE --> CAE3["module設定"]

    LIC --> LIC1["FlexLM/RLM構成"]
    LIC --> LIC2["冗長化"]
    LIC --> LIC3["アクセス制限"]

    GH --> GH1["認証方式"]
    GH --> GH2["リポジトリ管理"]
    GH --> GH3["バックアップ"]
```

## 各ページ一覧

| ページ | 概要 |
|---|---|
| [CAEソフトウェア](cae-software.md) | CAEソフトのバージョン管理・ライセンスポリシー・module設定 |
| [ライセンスサーバ](license-server.md) | FlexLM/RLMライセンスサーバの構成・利用状況確認・アクセス制限 |
| [GitHub Server](github-server.md) | GitHub Serverの構成・運用・認証・バックアップ |

## 関連ページ

- [計算リソース・ジョブ管理](../compute/index.md)
- [ユーザーアクセス・認証・ポータル](../user-access/index.md)
- [データ管理・基盤サービス・運用管理](../data-ops/index.md)
