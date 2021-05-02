if [ $# -eq 0 ]; then
	echo "No argument specified."
	exit
fi

if [ $2 == "clean" ]; then
	rm -rf $1 BestNews.exe
	exit
fi

filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"

cp ../MalwareDatabase-master/ransomwares/$1 .
7z x -pmysubsarethebest $1
mv Endermanch@$filename.exe BestNews.exe
