
files = $(shell find . -iname '*.proto')
all:
	python3 -c "import os,glob; [os.system('protoc --python_out=../adsmsg/protobuf/ {file}'.format(file=x)) for x in glob.glob('*.proto')]"
	# protoc does not express imports in a relative form, which messes up with our package structure
	# thus we force relative imports by changing the generated files with the next sed command:
	# 	https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-369324250
	sed -i 's/^import \([^ ]*\)_pb2 as \([^ ]*\)$$/from . import \1_pb2 as \2/' ../adsmsg/protobuf/*_pb2.py
clean:
	python3 -c "import os,glob; [os.system('rm -fr ../adsmsg/protobuf/{file}_pb2.py*'.format(file=x.split('.proto')[0])) for x in glob.glob('*.proto')]"
