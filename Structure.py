#!/usr/bin/env python
# -*- coding: utf-8 -*-

# implement the Queue
#   structure model
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)
# implement the Stack
#   structure model
class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop(-1)

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)
