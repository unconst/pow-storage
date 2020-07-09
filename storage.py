from cryptography.hazmat.backends import default_backend

import random
from functools import cmp_to_key

import storage_pb2_grpc


class Storage(storage_pb2_grpc.StorageServicer):
    def __init__(self, N: int):
        self._storage = []
        self._N = N
        self._block = 0

    def score(self, entry):
        difficulty = len(entry.pow) - len(entry.pow.rstrip('0'))
        delta_block = self._block - entry.block
        return difficulty / delta_block

    def compare(self, a, b):
        a_score = self.score(a)
        b_score = self.score(b)
        if a_score > b_score:
            return 1
        elif a_score == b_score:
            return 0
        else:
            return -1

    def Gossip(self, request, context):
        self.add(request)

    def add(self, entry):
        self._storage.append(entry)
        if len(self._storage) >= 1.25 * self._N:
            print("trim")
            self._storage = sorted(self._storage, key=cmp_to_key(self.compare))
            self._storage = self._storage[:self._N]
