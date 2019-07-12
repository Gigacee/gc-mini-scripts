# encoding: utf-8
################################################################################
# Google スプレッドシートを見に行くテストです。
################################################################################

require "fileutils"
require "google_drive"
require "json"

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# 設定をロード
begin
  config = File.open("#{WORKING_DIRECTORY_PATH}/config.json") { |f| JSON.load(f) }
rescue
  puts "config.json を読み込めませんでした。"
  exit
end

# Google ドライブにアクセス
begin
  session = GoogleDrive::Session.from_config(File.expand_path(config["google_api_config"]))
rescue
  puts "Google ドライブにアクセスできませんでした。google_api_config が誤っている可能性があります。"
  exit
end

# 設定された Google スプレッドシートを読み込む
begin
  spreadsheet = session.spreadsheet_by_key(config["gsheet_key"])
rescue
  puts "Google スプレッドシートを読み込めませんでした。gsheet_key が誤っている可能性があります。"
  exit
end

ws = spreadsheet.worksheets[0]
puts ws[1, 1]
