# 話者分離機能付き音声文字起こしツール

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

OpenAIのWhisperモデルと話者分離技術を使用して、音声ファイルを自動的に文字起こしし、会話内の異なる話者を識別するWebアプリケーション。

## 機能

- **モダンなユーザーインターフェース:**
  * ドラッグ＆ドロップによるファイルアップロード機能を備えた、クリーンで直感的なWebインターフェース
  * 文字起こし処理中のリアルタイム進捗追跡
  * 様々なデバイスに対応したレスポンシブデザイン
  * 18言語のユーザーインターフェースサポート

- **強力な文字起こしエンジン:**
  * OpenAIのWhisper音声認識モデルの統合
  * 速度と精度のバランスを考慮した複数のモデルサイズ（tiny、base、small、medium、large）
  * 会話内の異なる話者を識別・分離する話者分離機能
  * 様々な音声形式（MP3、WAV、OGG、FLAC、M4A）のサポート

- **柔軟な出力オプション:**
  * 複数の形式（TXT、JSON、SRT、VTT）での文字起こし結果のダウンロード
  * 話者識別付きのタイムスタンプ文字起こし
  * 読みやすく後処理しやすいクリーンなフォーマット

## インストール

1. リポジトリのクローン:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. 依存関係のインストール:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. アプリケーションの実行:
```bash
python app_diarize.py
```

アプリケーションは `http://localhost:5001` で利用可能です

## 使用方法

1. Webブラウザを開き、`http://localhost:5001` にアクセス
2. ドラッグ＆ドロップインターフェースまたはファイル選択ダイアログを使用して音声ファイルをアップロード
3. 希望するモデルサイズと話者数を選択
4. 文字起こしの完了を待つ
5. 希望する形式で結果をダウンロード

## トラブルシューティング

- ポート5001が既に使用中の場合は、`app_diarize.py` でポートを変更できます
- 大きな音声ファイルの場合は、処理を高速化するために小さいモデルサイズの使用を検討してください
- 一時ファイル用に十分なディスク容量があることを確認してください

## ライセンス

このプロジェクトはMITライセンスの下で提供されています - 詳細はLICENSEファイルを参照してください。

## 作者

李志恩 