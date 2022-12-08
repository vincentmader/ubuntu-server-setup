ubuntu-server-setup:
	cd ./bin/ && ./ubuntu-server-setup
all:
	make p1
	make p2
p1:
	cd ./src/p1_initial_server_setup/bin/ && ./p1_initial_server_setup
p2:
	cd ./src/p2_nginx_reverse_proxy/bin/ && ./p2_nginx_reverse_proxy
