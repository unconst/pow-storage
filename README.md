# A Proof of Work Storage Cache.

TL;DR: Provides a sybil resistant continually updating shared storage object.

1. Nodes gossip new entries to each other with an attached timestamped proof-of-work (POW).
2. Only the N entries with largest (POW-difficulty)/(now - timestamp) remain in the storage.

Attackers seeking to block the network by subscribing many spurious nodes are forced to pay 
continually for placement in the system. If X = (POW-difficulty)/(now - timestamp) is the maximum
computational cost willing to be paid by the non-malicious users of the system for each entry,
then the attacker must provide continual computational power equivalent to X * N in order to fill
the cache.

# Uses

1. Service discovery: Computers would like to be discovered by their peers by advertising their
unique (IP, port) by gossiping it through the network. However, an attacker may flood 
the network with false peer information obscuring or overflowing the storage of other peers. By 
attaching timestamped POW to new entries being gossiped, an attacker must continually perform 
computation to overflow the buffer and online peers can increase their POW to resist the attack. 
