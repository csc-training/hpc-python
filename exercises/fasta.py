#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
"""
Simple parser for Fasta sequence files.

    Copyright (C) 2016  Martti Louhivuori

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.
"""

class Fasta:
    """
    Read an amino acid sequence from a Fasta file.

      self.chains  --  a dict of chains where key is chain ID and value the
                       amino acid sequence
      self.filename -- name of the Fasta file
      self.marker   -- marks the beginning of a chain ID line (default: >)
      self.pdb      -- ID of the PDB entry (if able to parse it)

    Example usage:
      from fasta import Fasta
      fasta = Fasta('5ire.fasta.txt')
      print fasta['A']
      for chain in fasta:
          print chain
    """
    def __init__(self, filename, marker='>'):
        self.pdb = None
        self.marker = marker
        self.read(filename)
    def read(self, filename):
        """
        Parse a Fasta file and extract the amino acid sequence for each
        separate chain.
        """
        self.filename = filename
        file = open(filename)
        self.chains = {}
        self.__order__ = []
        key = None
        chain = ''
        for line in file:
            if line[0] is self.marker:
                if key is not None:
                    self.__order__.append(key)
                    self.chains[key] = chain
                line = line[1:].strip()
                if line[4] == ':':
                    self.pdb = line[:3]
                    line = line[5:]
                key = line.split('|')[0]
                chain = ''
            else:
                chain += line.strip()
        if key is not None:
            self.chains[key] = chain
        file.close()
    def __iter__(self):
        for key in self.__order__:
            yield self.chains[key]
    def __getitem__(self, key):
        if key in self.chains:
            return self.chains[key]
        elif type(key) is int and key < len(self.chains):
            return self.chains[self.__order__[key]]
        else:
            raise KeyError('Invalid chain ID')
    def __len__(self):
        return len(self.chains)
    def __repr__(self):
        return 'Fasta(%s, marker=%s)' % (self.filename, self.marker)
    def __str__(self):
        if self.pdb:
            name = self.pdb + ':%s'
        else:
            name = '%s'
        txt = ''
        for key in self.__order__:
            txt += self.marker + name % key + '\n'
            txt += self.chains[key] + '\n'
        return txt

