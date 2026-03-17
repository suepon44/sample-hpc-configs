"""Unit tests for mkdocs.yml configuration structure.

Validates: Requirements 3.1, 3.4, 4.3, 5.1
"""


EXPECTED_TOP_LEVEL_CATEGORIES = [
    "ユーザーアクセス・認証・ポータル",
    "計算リソース・ジョブ管理",
    "アプリケーション・ライセンス",
    "データ管理・基盤サービス・運用管理",
    "ネットワーク",
]


def _get_nav_category_names(nav: list) -> list[str]:
    """Extract top-level category names from the nav list.

    Nav entries are either plain strings (e.g. "ホーム: index.md")
    or dicts whose key is the category name.  We only care about
    the dict-based entries that map to a list of children (i.e.
    the 5 main content categories).
    """
    names: list[str] = []
    for entry in nav:
        if isinstance(entry, dict):
            for key, value in entry.items():
                if isinstance(value, list):
                    names.append(key)
    return names


def test_top_level_categories(mkdocs_config: dict) -> None:
    """5つのトップレベルカテゴリが正しい名前で存在すること (要件 3.1)."""
    category_names = _get_nav_category_names(mkdocs_config["nav"])
    for expected in EXPECTED_TOP_LEVEL_CATEGORIES:
        assert expected in category_names, (
            f"トップレベルカテゴリ '{expected}' がnavに存在しません"
        )
    assert len([n for n in category_names if n in EXPECTED_TOP_LEVEL_CATEGORIES]) == 5


def test_navigation_path_feature(mkdocs_config: dict) -> None:
    """navigation.path featureが有効であること — パンくずリスト (要件 3.4)."""
    features = mkdocs_config["theme"]["features"]
    assert "navigation.path" in features, (
        "navigation.path がtheme.featuresに含まれていません"
    )


def test_search_plugin_japanese(mkdocs_config: dict) -> None:
    """searchプラグインが有効で日本語対応であること (要件 4.3)."""
    plugins = mkdocs_config["plugins"]
    search_config = None
    for plugin in plugins:
        if isinstance(plugin, dict) and "search" in plugin:
            search_config = plugin["search"]
            break
        elif plugin == "search":
            # search enabled without explicit config
            search_config = {}
            break

    assert search_config is not None, "searchプラグインが有効になっていません"
    lang = search_config.get("lang", [])
    assert "ja" in lang, "searchプラグインのlangに'ja'が含まれていません"


def test_mermaid_custom_fence(mkdocs_config: dict) -> None:
    """pymdownx.superfencesのカスタムフェンスにmermaidが設定されていること (要件 5.1)."""
    extensions = mkdocs_config["markdown_extensions"]
    superfences_config = None
    for ext in extensions:
        if isinstance(ext, dict) and "pymdownx.superfences" in ext:
            superfences_config = ext["pymdownx.superfences"]
            break

    assert superfences_config is not None, (
        "pymdownx.superfences がmarkdown_extensionsに存在しません"
    )
    custom_fences = superfences_config.get("custom_fences", [])
    mermaid_fences = [f for f in custom_fences if f.get("name") == "mermaid"]
    assert len(mermaid_fences) > 0, (
        "pymdownx.superfencesのcustom_fencesにmermaid設定がありません"
    )
