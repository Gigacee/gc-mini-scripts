# encoding: utf-8
################################################################################
# Google スプレッドシートを見に行くテストです。
################################################################################

require "fileutils"
require "google_drive"
require "json"

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# 設定ファイルのパス
settings_file_path = "#{WORKING_DIRECTORY_PATH}/settings.json"

# 設定ファイルが存在しない場合、テンプレートからコピーする
if !File.exist?(settings_file_path)
  FileUtils.cp_r("#{WORKING_DIRECTORY_PATH}/settings.json.templete", settings_file_path)

  puts "settings.json が見つからなかったため、settings.json を初期化しました。"
  exit
end

# 設定を読み込む
begin
  settings = File.open(settings_file_path) { |f| JSON.load(f) }
rescue
  puts "settings.json を読み込めませんでした。"
  exit
end

# Google ドライブにアクセス
begin
  session = GoogleDrive::Session.from_config(File.expand_path(settings["google_api_config"]))
rescue
  puts "Google ドライブにアクセスできませんでした。google_api_config が誤っている可能性があります。"
  exit
end

# 設定された Google スプレッドシートを読み込む
begin
  spreadsheet = session.spreadsheet_by_key(settings["gsheet_key"])
rescue
  puts "Google スプレッドシートを読み込めませんでした。gsheet_key が誤っている可能性があります。"
  exit
end

ws = spreadsheet.worksheets[0]
puts ws[1, 1]
