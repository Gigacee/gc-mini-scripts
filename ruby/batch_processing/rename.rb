################################################################################
# 同階層に存在する CSV の 1 列目のファイル名を、2 列目のファイル名にリネームします。
################################################################################

require "csv"
require "fileutils"

# 作業ディレクトリのパスを取得
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# CSV を読み込む
table = CSV.read("#{WORKING_DIRECTORY_PATH}/table.csv")

Dir.glob("#{WORKING_DIRECTORY_PATH}/*") do |src|
  table.each do |row|
    if src == "#{WORKING_DIRECTORY_PATH}/#{row[0]}"
      FileUtils.mv(src, "#{WORKING_DIRECTORY_PATH}/#{row[1]}")
      puts "\"#{row[0]}\" is renamed to \"#{row[1]}\"."
    end
  end
end
