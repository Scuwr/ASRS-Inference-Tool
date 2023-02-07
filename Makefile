start:
# CLI: redis-cli -p 6397
# 6397
	redis-7.0.8/src/redis-server redis.conf

install:
	wget https://download.redis.io/releases/redis-7.0.8.tar.gz
	tar xvzf redis-7.0.8.tar.gz
	rm redis-7.0.8.tar.gz
	(cd redis-7.0.8; make)

update:
	scp cmarnold@victoria.csail.mit.edu:/storage/cmarnold/data_archive/dump_recent.rdb ./dump.rdb