import os
import wifi
from scapy.all import srp, Ether, ARP, conf
import argparse


def scan_ips(interface='wlan0', ips='192.168.1.0/24'):
	try:
		print 'Starting'
		conf.verb = 0
		ether = Ether(dst='ff:ff:ff:ff:ff:ff')
		arp = ARP(pdst=ips)
		answer, unanswered = srp(ether/arp, timeout = 2, iface = interface, inter = 0.1)
		
		for sent, received in answer:
			print received.summary()

	except KeyboardInterrupt:
		print 'Quitting'
		sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--scan', action='store_true', help='Scan the network')
args = parser.parse_args()

if args.scan:
	scan_ips()



