# https://www.acmicpc.net/problem/24060

from sys import stdin

N, K = map(int, stdin.readline().split())

input_list = [map(int, stdin.readline().split())]

def merge_sort():
    