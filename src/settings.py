class Settings:
    BASE_URL = "https://yakkun.com"
    STATUS_LIST_URL = BASE_URL + "/swsh/stats_list.htm?mode=all"

    ENCODING = "EUC-JP"

    STATUS = {
        "HP": "hitpoint",
        "こうげき": "attack",
        "ぼうぎょ": "block",
        "とくこう": "contact",
        "とくぼう": "defense",
        "すばやさ": "speed",
        "合計": "total"
    }

    REGIONS = {
        1: "カントー",
        2: "ジョウト",
        3: "ホウエン",
        4: "シンオウ",
        5: "イッシュ",
        6: "カロス",
        7: "アローラ",
        8: "ガラル",
    }

    COLUMNS = [
        "No.",
        "なまえ",
        "タイプ1",
        "タイプ2",
        "とくせい1",
        "とくせい2",
        "ゆめとくせい",
        "HP",
        "こうげき",
        "ぼうぎょ",
        "とくこう",
        "とくぼう",
        "すばやさ",
        "合計",
        "最終進化",
        "地方",
        "メガシンカ",
        "同一種族値"
    ]

    MEGA_EVOLUTION_NAMES = [
        "メガフシギバナ",
        "メガリザードンX",
        "メガリザードンY",
        "メガカメックス",
        "メガスピアー",
        "メガピジョット",
        "メガフーディン",
        "メガヤドラン",
        "メガゲンガー",
        "メガガルーラ",
        "メガカイロス",
        "メガギャラドス",
        "メガプテラ",
        "メガミュウツーX",
        "メガミュウツーY",
        "メガニウム",
        "メガデンリュウ",
        "メガハガネール",
        "メガハッサム",
        "メガヘラクロス",
        "メガヘルガー",
        "メガバンギラス",
        "メガジュカイン",
        "メガバシャーモ",
        "メガラグラージ",
        "メガサーナイト",
        "メガヤミラミ",
        "メガクチート",
        "メガボスゴドラ",
        "メガチャーレム",
        "メガライボルト",
        "メガサメハダー",
        "メガバクーダ",
        "メガチルタリス",
        "メガジュペッタ",
        "メガアブソル",
        "メガオニゴーリ",
        "メガボーマンダ",
        "メガメタグロス",
        "メガラティアス",
        "メガラティオス",
        "ゲンシカイオーガ",
        "ゲンシグラードン",
        "メガレックウザ",
        "メガミミロップ",
        "メガガブリアス",
        "メガルカリオ",
        "メガユキノオー",
        "メガエルレイド",
        "メガタブンネ",
        "メガディアンシー",
    ]
