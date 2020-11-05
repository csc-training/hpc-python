#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
"""
Simple parser for reading atoms from a PDB file.

    Copyright (C) 2016  Martti Louhivuori

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.
"""
import re
from numpy import array, zeros

class Atom:
    """
    Container for atom coordinates with the possibility to store additional
    information (element and chain ID).

      self.x        --  X coordinate
      self.y        --  Y coordinate
      self.z        --  Z coordinate
      self.element  --  atom type
      self.chain    --  chain ID of the atom
    """
    def __init__(self, x, y, z, element=None, chain=None):
        """
        Initialize a new chain.

        Args:
            self: (todo): write your description
            x: (int): write your description
            y: (int): write your description
            z: (int): write your description
            element: (todo): write your description
            chain: (int): write your description
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.element = element or None
        self.chain = chain or None
    def tolist(self):
        """
        Returns a copy of this vector

        Args:
            self: (todo): write your description
        """
        return [self.x, self.y, self.z]
    def toarray(self):
        """
        Convert this array into a numpy array.

        Args:
            self: (todo): write your description
        """
        return array(self.tolist())
    def __repr__(self):
        """
        Return a repr representation.

        Args:
            self: (todo): write your description
        """
        element = self.element or 'None'
        return 'Atom(%f, %f, %f, element=%s)' % \
                (self.x, self.y, self.z, element)
    def __str__(self):
        """
        Return the string representation of this element.

        Args:
            self: (todo): write your description
        """
        if self.element:
            return self.element + ': ' + str(self.tolist())
        else:
            return str(self.tolist())

class PDB:
    """
    Read atom coordinates from a PDB file.

      self.atoms        --  List of Atom() objects containing all ATOM records
      self.coordinates  --  NumPy array of atom coordinates

    Example usage:
      from pdb import PDB
      pdb = PDB('5ire.pdb')
      print pdb.coordinates
      for atom in pdb:
          print atom
    """
    def __init__(self, filename):
        """
        Initialize a root file.

        Args:
            self: (todo): write your description
            filename: (str): write your description
        """
        self.__ro_atom__ = re.compile('^ATOM ')
        self.read(filename)
    def read(self, filename):
        """
        Parse a PDB file and store all ATOM records.
        """
        self.filename = filename
        file = open(filename)
        self.atoms = []
        for line in file:
            if not self.__ro_atom__.match(line):
                continue
            x = line[30:38].strip()
            y = line[38:46].strip()
            z = line[46:54].strip()
            e = line[76:78].strip()
            c = line[21]
            self.atoms.append(Atom(x, y, z, element=e, chain=c))
        file.close()
        self.__prep_coords__()
    def __prep_coords__(self):
        """
        Prepare the coordinates. coordinates.

        Args:
            self: (todo): write your description
        """
        self.coordinates = zeros((len(self.atoms), 3), float)
        for i, atom in enumerate(self.atoms):
            self.coordinates[i] = atom.toarray()
    def __iter__(self):
        """
        Iterate over all atomically.

        Args:
            self: (todo): write your description
        """
        for atom in self.atoms:
            yield atom
    def __getitem__(self, key):
        """
        Return the value of the given key.

        Args:
            self: (todo): write your description
            key: (str): write your description
        """
        if type(key) is int and key < len(self.atoms):
            return self.atoms[key]
        else:
            raise KeyError('Invalid chain ID')
    def __len__(self):
        """
        Returns the length of the byte.

        Args:
            self: (todo): write your description
        """
        return len(self.atoms)
    def __repr__(self):
        """
        Return a human - readable representation of this object.

        Args:
            self: (todo): write your description
        """
        return 'PDB(%s)' % self.filename
    def __str__(self):
        """
        Return a string representation of the file.

        Args:
            self: (todo): write your description
        """
        txt = '%d atoms from %s\n' % (len(self.atoms), self.filename)
        txt += '---\n'
        for atom in self.atoms:
            txt += str(atom) + '\n'
        return txt

