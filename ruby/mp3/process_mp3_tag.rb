# encoding: utf-8
################################################################################
# mp3 ファイルのタグを扱うテストです。
################################################################################

require "mp3info"

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# 作業ディレクトリと同階層にあるすべての mp3 ファイルに対して処理を行う
Dir.glob("#{WORKING_DIRECTORY_PATH}/*.mp3").each do |f|
  Mp3Info.open(f) do |mp3|
    puts "#{f}"

    # トラック番号を設定
    # mp3.tag2.TRCK = File.basename(f, ".*").gsub(/[^0-9 _\-]*/, "").split(/[ _\-]/).last

    # タグ情報を出力
    p mp3.tag2
  end

  puts
end
