# encoding: utf-8
################################################################################
# CSV に入力された名前のディレクトリを生成します。
################################################################################

require "csv"
require "fileutils"

# 作業ディレクトリのパスを取得
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# CSV を読み込む
table = CSV.read("#{WORKING_DIRECTORY_PATH}/table.csv")

table.each do |row|
  FileUtils.mkdir_p("#{WORKING_DIRECTORY_PATH}/#{row[0]}")
  puts "#{row[0]} is made."
end
