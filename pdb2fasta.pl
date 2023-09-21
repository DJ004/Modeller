#!/usr/bin/perl
# This script looks for the ATOM tag in a line and converts
# the pdb file to fasta format. Separate chain identifiers 
# are written as well.
#
# Author: Ranjit Vijayan
# Created: 11/03/2006
# Version: $Id$

# The lookup table
%lookup=(
           
             'ALA' => 'A',
             'ASX' => 'B',
             'CYS' => 'C',
             'ASP' => 'D',
             'GLU' => 'E',
             'PHE' => 'F',
             'GLY' => 'G',
             'HIS' => 'H',
             'ILE' => 'I',
             'LYS' => 'K',
             'LEU' => 'L',
             'MET' => 'M',
             'ASN' => 'N',
             'PRO' => 'P',
             'GLN' => 'Q',
             'ARG' => 'R',
             'SER' => 'S',
             'THR' => 'T',
             'VAL' => 'V',
             'TRP' => 'W',
             'XXX' => 'X',
             'TYR' => 'Y',
             'GLX' => 'Z',
             '...' => '.',
	     'TER' => '/',
             'END' => '*' 
             );

die "Usage: pdb2fasta <pdbfile>\n"
    unless ($#ARGV==0);

open(PDBFILE, "<$ARGV[0]") || die "Could not open $ARGV[0]";

# Keep track of the previous residue and chain ID
$prevResidueID = "NONE";
$prevChainID = "NONE";

# Keep track of the number of residues in the chain
$counter=0;


# Go through the pdb file line by line
foreach (<PDBFILE>)
{
   # If the line is an ATOM record get the residue details
   if (/^ATOM/)
   {
       # Store the previous values for comparing later
       $prevResidueID = $residueID;
       $prevChainID = $chainID;

       # Get the residue, residue id and chain ID
       $residue = substr($_, 17,3);
       $residueID = substr($_, 22,4);
       $chainID = substr($_, 21,1);
  
       # Check if the chain ID is different, if yes, write a tag
       if ($chainID ne $prevChainID)
       {
          print "\n>Chain_$chainID\n";
          $counter = 0;
       }


       # If the current residue ID is different from the previous residue ID, write it out
       if ($residueID ne $prevResidueID)
       {
          $counter++;
          print $lookup{uc($residue)};
          # Create a newline after every 60 residues
          if ($counter%60 == 0)
          {
            print "\n";
          }
       }
   }
}
close(PDBFILE);
print "\n";
