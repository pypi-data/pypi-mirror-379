################################################################################
#
# solid_dmft - A versatile python wrapper to perform DFT+DMFT calculations
#              utilizing the TRIQS software library
#
# Copyright (C) 2018-2020, ETH Zurich
# Copyright (C) 2021, The Simons Foundation
#      authors: A. Hampel, M. Merkel, and S. Beck
#
# solid_dmft is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# solid_dmft is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# solid_dmft (in the file COPYING.txt in this directory). If not, see
# <http://www.gnu.org/licenses/>.
#
################################################################################

version = "3.3.3"
triqs_hash = "0a3ce9651e4b043eb24c0f7eae52e6538b36b752"
solid_dmft_hash = "282d8435c4ccdc1c9061451f5d777f374de8c238"

def show_version():
  print("\nYou are using solid_dmft version %s\n"%version)

def show_git_hash():
  print("\nYou are using solid_dmft git hash %s based on triqs git hash %s\n"%("282d8435c4ccdc1c9061451f5d777f374de8c238", triqs_hash))
