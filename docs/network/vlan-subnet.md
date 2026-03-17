---
title: VLAN/サブネット構成
description: HPCシステムにおけるサブネットおよびVLAN構成図に関する情報
---

# VLAN/サブネット構成

## 概要

本ページでは、HPCシステムにおけるVLAN設計とサブネット構成を記述する。各VLANの用途、割り当てサブネット、およびVLAN間の関係を構成図とともに示す。

## VLAN一覧

<!-- 実際のVLAN情報を記載 -->

| VLAN ID | VLAN名 | 用途 | サブネット | 備考 |
|---|---|---|---|---|
| （要記入） | （要記入） | HPCネットワーク | （要記入） | （要記入） |
| （要記入） | （要記入） | 管理ネットワーク | （要記入） | （要記入） |
| （要記入） | （要記入） | InfiniBand管理 | （要記入） | （要記入） |
| （要記入） | （要記入） | 基幹接続 | （要記入） | （要記入） |
| （要記入） | （要記入） | ストレージ | （要記入） | （要記入） |

## サブネット構成

<!-- 実際のサブネット情報を記載 -->

| サブネット | CIDR | VLAN | 用途 | ゲートウェイ |
|---|---|---|---|---|
| （要記入） | （要記入） | （要記入） | （要記入） | （要記入） |
| （要記入） | （要記入） | （要記入） | （要記入） | （要記入） |
| （要記入） | （要記入） | （要記入） | （要記入） | （要記入） |

## VLAN/サブネット構成図

```mermaid
flowchart TD
    subgraph CORE["コアスイッチ"]
        TRUNK["トランクポート"]
    end

    subgraph VLAN_HPC["VLAN: HPC"]
        HPC_SUB["サブネット: （要記入）"]
        HPC_NODES["計算ノード群"]
        HPC_LOGIN["ログインノード"]
    end

    subgraph VLAN_MGMT["VLAN: 管理"]
        MGMT_SUB["サブネット: （要記入）"]
        MGMT_BMC["BMC/IPMI"]
        MGMT_SRV["管理サーバ"]
    end

    subgraph VLAN_STORAGE["VLAN: ストレージ"]
        STR_SUB["サブネット: （要記入）"]
        STR_LUSTRE["Lustreサーバ"]
        STR_NAS["NAS-GW"]
    end

    subgraph VLAN_BACKBONE["VLAN: 基幹接続"]
        BB_SUB["サブネット: （要記入）"]
        BB_GW["ゲートウェイ"]
    end

    TRUNK --> VLAN_HPC
    TRUNK --> VLAN_MGMT
    TRUNK --> VLAN_STORAGE
    TRUNK --> VLAN_BACKBONE

    HPC_SUB --> HPC_NODES
    HPC_SUB --> HPC_LOGIN
    MGMT_SUB --> MGMT_BMC
    MGMT_SUB --> MGMT_SRV
    STR_SUB --> STR_LUSTRE
    STR_SUB --> STR_NAS
    BB_SUB --> BB_GW
```

## VLAN間ルーティング

<!-- 実際のルーティング情報を記載 -->

| 送信元VLAN | 宛先VLAN | 許可/拒否 | 備考 |
|---|---|---|---|
| （要記入） | （要記入） | （要記入） | （要記入） |
| （要記入） | （要記入） | （要記入） | （要記入） |
| （要記入） | （要記入） | （要記入） | （要記入） |

## 運用手順

- VLAN追加/変更手順: （要記入）
- サブネット追加手順: （要記入）
- VLAN間通信トラブルシューティング: （要記入）

## 関連ページ

- [論理構成](logical-design.md)
- [IPアドレス管理](ip-management.md)
- [DNS/NTP](../data-ops/dns-ntp.md)
