# encoding: utf-8
################################################################################
# wav ファイルを mp3 にエンコードします。
################################################################################

require "json"
require "open3"

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# 設定をロード
begin
  config = File.open("#{WORKING_DIRECTORY_PATH}/config.json") { |f| JSON.load(f) }
rescue
  puts "config.json を読み込めませんでした。"
  exit
end

# 設定された引数を配列に変換
lame_args = config["lame_arg"].split(" ")

# エンコードに失敗したファイルを記憶しておく配列
failed_files = []

# 作業ディレクトリと同階層にあるすべての wav ファイルに対して処理を行う
Dir.glob("#{WORKING_DIRECTORY_PATH}/*.wav").each do |wav|
  dest = "#{File.dirname(wav)}/#{File.basename(wav, ".wav")}.mp3"

  command = []
  command.push(config["lame_path"])
  command.concat(lame_args)
  command.push(wav)
  command.push(dest)

  print "Encoding #{wav} ... "

  # エンコードを実行
  o, e, s = Open3.capture3(*command)

  if s.exited?
    puts "OK"
  else
    puts "NG"
    failed_files.push(wav)
  end
end

if failed_files.empty?
  puts "すべてのファイルが正常にエンコードされました。"
else
  puts "以下のファイルのエンコードに失敗しました："
  puts failed_files
end
